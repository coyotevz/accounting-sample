# -*- coding: utf-8 -*-

from functools import partial

def d(v):
    if v == '': return v
    return "{:.2f}".format(v)

def print_account(acc, depth=None):
    width = 80
    col2 = 9
    col3 = 9
    col1 = width - (col2 + col3 + 3)
    patt = partial(u" {0:<{col1}} {1:>{col2}} {2:>{col3}}".format,
                   **{'col1': col1, 'col2': col2, 'col3': col3})
    #print(patt('', 'DEBE', 'HABER'))
    #print('-'*width)
    print_lines(acc, patt, depth)

def print_lines(acc, patt, depth=None):
    print_line(acc, patt)
    for c in acc.children:
        if depth > 0 or depth is None:
            print_lines(c, patt, (depth-1) if depth else None)

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

def print_transaction(t):
    for dest in t.dest:
        print(u"  {:<57} {:9} {:9}".format(dest.target.name, d(dest.amount), ""))
    for src in t.source:
        print(u"       a {:<50} {:9} {:9}".format(src.target.name, "", d(src.amount)))
