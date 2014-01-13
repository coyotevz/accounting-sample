# -*- coding: utf-8 -*-

from decimal import Decimal

from sqlalchemy import Column, Integer, Numeric, Unicode, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class InvaidArgumentError(ValueError):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    fullname = Column(Unicode)
    password = Column(Unicode)

    def __repr__(self):
        return "<User(name={}, fullname={}, password={})>".format(
                self.name, self.fullname, self.password)


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    lcode = Column(Unicode, nullable=False)
    name = Column(Unicode, unique=True, nullable=False)
    description = Column(Unicode)
    lbalance = Column(Numeric(10,2), default=None)

    parent_id = Column(Integer, ForeignKey('account.id'))
    parent = relationship("Account", remote_side=[id], backref="children")

    @property
    def code(self):
        return ".".join([a.lcode for a in self.get_path()])

    @code.setter
    def code(self, value):
        self.lcode = value

    @property
    def balance(self):
        if self.children:
            return sum([c.balance for c in self.children])
        return self.lbalance or Decimal('0')

    @balance.setter
    def balance(self, value):
        if self.children:
            raise InvaidArgumentError("Can't set balance value to an account"
                                      " with childrens")
        self.lbalance = value

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
