# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    Unicode,
    DateTime,
    Enum,
    ForeignKey,
    event,
)
from sqlalchemy.orm import (
    relationship,
    backref,
    object_session,
    Query,
    sessionmaker,
    scoped_session,
)
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Session = scoped_session(sessionmaker())
Base = declarative_base()


class InvaidArgumentError(ValueError):
    pass


class ValidationError(ValueError):
    pass


class AccountQuery(Query):

    def __init__(self, mapper, session):
        self.mapper = mapper
        self.session = session

    def get_by_code(self, code):
        codes = list(reversed(code.split(".")))
        query = self.session.query(Account).filter(Account.code == codes[0])
        for c in codes[1:]:
            query = query.join(Account.parent).filter(Account.code == c)
        query = query.filter(Account.parent == None)
        print(query)
        return query.one()


class Account(Base):
    __tablename__ = "account"

    query = Session.query_property(query_cls=AccountQuery)

    #: Este tipo de cuenta se incrementa por la columna 'debe'
    TYPE_CREDIT = "credit"

    #: Este tipo de cuenta se incrementa por la columna 'haber'
    TYPE_DEBIT = "debit"

    _type_str = {
        TYPE_CREDIT: "Incrementa por Debe",
        TYPE_DEBIT: "Incrementa por Haber",
    }

    id = Column(Integer, primary_key=True)
    _code = Column("code", Unicode, nullable=False)
    name = Column(Unicode, unique=True, nullable=False)
    description = Column(Unicode)
    _balance = Column("balance", Numeric(10, 2), default=None)
    _type = Column(
        "type", Enum(*list(_type_str.keys()), name="account_type"), default=None
    )

    parent_id = Column(Integer, ForeignKey("account.id"))
    parent = relationship("Account", remote_side=[id], backref="children")

    @hybrid_property
    def code(self):
        return ".".join([a._code for a in self.get_path()])

    @code.setter
    def code(self, value):
        self._code = value

    @code.expression
    def code(self):
        return self._code

    @property
    def balance(self):
        if self.children:
            return sum([c.balance for c in self.children])
        return self._balance or Decimal("0")

    @balance.setter
    def balance(self, value):
        if self.children:
            raise InvaidArgumentError(
                "Can't set balance value to an account" " with childrens"
            )
        self._balance = value

    @property
    def type(self):
        if self._type is not None:
            return self._type
        else:
            return self.parent.type

    @type.setter
    def type(self, value):
        if self.parent:
            raise InvalidArgumentError(
                "Can only set type attribute to top" " level accounts"
            )
        self._type = value

    def increment(self, amount):
        if self.type == self.TYPE_CREDIT:
            self.balance += amount
        else:
            self.balance -= amount

    def decrement(self, amount):
        if self.type == self.TYPE_CREDIT:
            self.balance -= amount
        else:
            self.balance += amount

    def get_path(self):
        parent = self
        path = []
        while parent:
            path.append(parent)
            parent = parent.parent
        return reversed(path)

    def get_children_recursively(self):
        children = set(self.children)
        if not len(children):
            return set()
        for child in self.children:
            children |= child.get_children_recursively()
        return children

    def __repr__(self):
        return "<Account(name={}, code={}, balance={})>".format(
            self.name, self.code, self.balance
        )


class AccountTransaction(Base):
    __tablename__ = "account_transaction"

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)

    @property
    def source(self):
        return self._get_entries(AccountTransactionEntry.TYPE_SOURCE)

    @source.setter
    def source(self, value):
        self._create_entries(value, AccountTransactionEntry.TYPE_SOURCE)

    @property
    def dest(self):
        return self._get_entries(AccountTransactionEntry.TYPE_DEST)

    @dest.setter
    def dest(self, value):
        self._create_entries(value, AccountTransactionEntry.TYPE_DEST)

    def verify(self):
        credit = sum([e.amount for e in self.dest])
        debit = sum([e.amount for e in self.source])
        if (credit - debit) != 0:
            raise ValidationError("credit and debit must be equals")

    def _get_entries(self, e_type):
        s = object_session(self)
        return (
            s.query(AccountTransactionEntry)
            .filter_by(transaction=self)
            .filter_by(type=e_type)
            .all()
        )

    def _create_entries(self, value, e_type):
        # value = [(account, amount)]
        if not isinstance(value, list):
            value = [value]
        for v in value:
            e = AccountTransactionEntry(
                type=e_type, target=v[0], transaction=self, amount=Decimal(v[1])
            )


class AccountTransactionEntry(Base):
    __tablename__ = "account_transaction_entry"

    TYPE_SOURCE = "source"
    TYPE_DEST = "dest"

    id = Column(Integer, primary_key=True)
    target_id = Column(Integer, ForeignKey("account.id"), nullable=False)
    target = relationship(Account, backref="transaction_entries")
    transaction_id = Column(
        Integer, ForeignKey("account_transaction.id"), nullable=False
    )
    transaction = relationship(AccountTransaction, backref="entries")
    type = Column(Enum(TYPE_SOURCE, TYPE_DEST, name="entry_type"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)

    def __repr__(self):
        return "<AccountTransactionEntry(type={})".format(self.type)


def entry_instances(iter_):
    for obj in iter_:
        if isinstance(obj, AccountTransactionEntry):
            yield obj


def _entry_before_commit(session):
    changed = list(session.new)
    for entry in entry_instances(changed):
        etype = entry.type
        target = entry.target
        amount = entry.amount
        if etype == AccountTransactionEntry.TYPE_SOURCE:
            target.decrement(amount)
        elif etype == AccountTransactionEntry.TYPE_DEST:
            target.increment(amount)
        else:
            raise TypeError("Unknown transaction type")


event.listen(Session, "before_commit", _entry_before_commit)


def transaction_instaces(iter_):
    for obj in iter_:
        if isinstance(obj, AccountTransaction):
            yield obj


def _verify_transaction(session):
    changed = list(session.new) + list(session.dirty)
    for transaction in transaction_instaces(changed):
        transaction.verify()


event.listen(Session, "before_commit", _verify_transaction)
