# -*- coding: utf-8 -*-

from decimal import Decimal

from sqlalchemy import Column, Integer, Numeric, Unicode, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class InvaidArgumentError(ValueError):
    pass


class Account(Base):
    __tablename__ = 'account'

    #: Este tipo de cuenta se incrementa por la columna 'debe'
    TYPE_CREDIT = 'credit'

    #: Este tipo de cuenta se incrementa por la columna 'haber'
    TYPE_DEBIT = 'debit'

    _type_str = {
        TYPE_CREDIT: u'Incrementa por Debe',
        TYPE_DEBIT: u'Incrementa por Haber',
    }

    id = Column(Integer, primary_key=True)
    _code = Column("code", Unicode, nullable=False)
    name = Column(Unicode, unique=True, nullable=False)
    description = Column(Unicode)
    _balance = Column("balance", Numeric(10,2), default=None)
    _type = Column("type", Enum(*_type_str.keys(), name='account_type'),
                   default=None)

    parent_id = Column(Integer, ForeignKey('account.id'))
    parent = relationship("Account", remote_side=[id], backref="children")

    @property
    def code(self):
        return ".".join([a._code for a in self.get_path()])

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def balance(self):
        if self.children:
            return sum([c.balance for c in self.children])
        return self._balance or Decimal('0')

    @balance.setter
    def balance(self, value):
        if self.children:
            raise InvaidArgumentError("Can't set balance value to an account"
                                      " with childrens")
        self._balance = value

    @property
    def type(self):
        return self._type or self.parent.type            

    @type.setter
    def type(self, value):
        if self.parent:
            raise InvalidArgumentError("Can only set type attribute to top"
                                       " level accounts")
        self._type = value

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
                self.name, self.code, self.balance)
