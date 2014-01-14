# -*- coding: utf-8 -*-

from decimal import Decimal
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from acc import Base, Account

A = Account

engine = create_engine('sqlite:///test_data_1.db', echo=True)
session = sessionmaker(bind=engine)()
Base.metadata.bind = engine
Base.metadata.create_all()

# Create accounts
activo = A(code=u'1', name=u'Activo', type=A.TYPE_CREDIT, children=[
    A(code=u'1', name=u'Activo Corriente', children=[
        A(code=u'1', name=u'Caja y Bancos', children=[
            A(code=u'1', name=u'Caja', children=[
                A(code=u'1', name=u'Caja General'),
                A(code=u'2', name=u'Caja Beltrán'),
                A(code=u'3', name=u'Caja Colón'),
            ]),
            A(code=u'2', name=u'Bancos', children=[
                A(code=u'1', name=u'Banco Santander Río Cta Cte'),
                A(code=u'2', name=u'Banco Credicoop Cta Cte'),
                A(code=u'3', name=u'Banco Nación Caja Seguridad'),
                A(code=u'4', name=u'Valores a depósitar'),
            ]),
        ]),
        A(code=u'2', name=u'Créditos', children=[
            A(code=u'1', name=u'Deudores por Ventas', children=[
                A(code=u'1', name=u'Cliente clase A'),
                A(code=u'2', name=u'Cliente clase B'),
                A(code=u'3', name=u'Cliente clase C'),
                A(code=u'4', name=u'Tarjeta VISA'),
                A(code=u'5', name=u'Tarjeta Mastercard'),
                A(code=u'6', name=u'Tarjeta Nevada'),
            ]),
            A(code=u'2', name=u'Créditos Fiscales', children=[
                A(code=u'1', name=u'IVA Crédito Fiscal'),
                A(code=u'2', name=u'Retenciones sufridas IVA'),
                A(code=u'3', name=u'Retenciones sufridas Ingresos Brutos'),
                A(code=u'4', name=u'Retenciones sufridas Imp. Ganancias'),
                A(code=u'5', name=u'Retenciones sufridas SUSS'),
                A(code=u'6', name=u'Otras retenciones sufridas'),
            ]),
            A(code=u'3', name=u'Otros Créditos', children=[
                A(code=u'1', name=u'Adelantos de Sueldo'),
                A(code=u'2', name=u'Adelantos a Proveedores'),
                A(code=u'3', name=u'Adelantos a Socios', children=[
                    A(code=u'1', name=u'Adelantos a Carlos R.'),
                    A(code=u'2', name=u'Adelantos a Augusto R.'),
                    A(code=u'3', name=u'Adelantos a Germán R.'),
                ]),
            ]),
        ]),
        A(code=u'3', name=u'Bienes de Cambio', children=[
            A(code=u'1', name=u'Mercadería Ciudad'),
            A(code=u'2', name=u'Mercadería Godoy Cruz'),
            A(code=u'3', name=u'Mercadería en Transito'),
        ])
    ]),

    A(code=u'2', name=u'Activo No Corriente', children=[
        A(code=u'1', name=u'Rodados'),
        A(code=u'2', name=u'Inmuebles e instalaciones', children=[
            A(code=u'1', name=u'Terrenos'),
            A(code=u'2', name=u'Inmuebles'),
            A(code=u'3', name=u'Instalaciones comerciales'),
            A(code=u'4', name=u'Equipos de Oficina'),
        ]),
        A(code=u'3', name=u'Otros Activos Fijos'),
    ]),
])

pasivo = A(code=u'2', name=u'Pasivo', type=A.TYPE_DEBIT, children=[
    A(code=u'1', name=u'Pasivo Corriente'),
    A(code=u'2', name=u'Pasivo No Corriente'),
])

patrimonio = A(code=u'3', name=u'Patrimonio Neto', type=A.TYPE_DEBIT, children=[
    A(code=u'1', name=u'Capital'),
    A(code=u'2', name=u'Reservas'),
    A(code=u'3', name=u'Resultados Acumulados'),
    A(code=u'4', name=u'Resultados Acumulados Ejercicios Anteriores'),
])

session.add_all([activo, pasivo, patrimonio])
session.commit()
