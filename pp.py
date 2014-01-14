# -*- coding: utf-8 -*-

from functools import partial

def d(v):
    if v == '': return v
    return "{:.2f}".format(v)

def pretty_print(acc):
    width = 80
    col2 = 9
    col3 = 9
    col1 = width - (col2 + col3 + 3)
    patt = partial(u" {0:<{col1}} {1:>{col2}} {2:>{col3}}".format,
                   **{'col1': col1, 'col2': col2, 'col3': col3})
    #print(patt('', 'DEBE', 'HABER'))
    #print('-'*width)
    print_lines(acc, patt)

def print_lines(acc, patt):
    print_line(acc, patt)
    for c in acc.children:
        print_lines(c, patt)

def print_line(acc, patt):
    name = unicode(acc.name)
    if acc.parent is None:
        name = name.upper()
    if acc.type == acc.TYPE_CREDIT:
        credit = acc.balance
        debit = ''
    elif acc.type == acc.TYPE_DEBIT:
        credit = ''
        debit = acc.balance
    else:
        raise ValueError(u'Unknown type for {!r} ({})'.format(acc, acc.type))
    print(patt(u'{} {}'.format(acc.code, name), d(credit), d(debit)))
