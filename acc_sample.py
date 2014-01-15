# -*- coding: utf-8 -*-

from decimal import Decimal
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from acc import Base, Account
from pp import pretty_print

A = Account

engine = create_engine('sqlite:///test_data_1.db')
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
                A(code=u'1', name=u'Cliente Clase A'),
                A(code=u'2', name=u'Cliente Clase B'),
                A(code=u'3', name=u'Cliente Clase C'),
                A(code=u'4', name=u'Documentos a cobrar'),
                A(code=u'5', name=u'Tarjeta VISA'),
                A(code=u'6', name=u'Tarjeta Mastercard'),
                A(code=u'7', name=u'Tarjeta Nevada'),
            ]),
            A(code=u'2', name=u'Créditos Fiscales', children=[
                A(code=u'1', name=u'IVA Crédito Fiscal'),
                A(code=u'2', name=u'Retenciones sufridas IVA'),
                A(code=u'3', name=u'IVA Saldo a Favor'),
                A(code=u'4', name=u'Retenciones sufridas Ingresos Brutos'),
                A(code=u'5', name=u'Ingresos Brutos Saldo a Favor'),
                A(code=u'6', name=u'Retenciones sufridas Imp. Ganancias'),
                A(code=u'7', name=u'Anticipo Imp. Ganancias'),
                A(code=u'8', name=u'Retenciones sufridas SUSS'),
                A(code=u'9', name=u'Otras retenciones sufridas'),
            ]),
            A(code=u'3', name=u'Otros Créditos', children=[
                A(code=u'1', name=u'Alquileres pagados por adelantado'),
                A(code=u'2', name=u'Seguros pagados por adelantado'),
                A(code=u'3', name=u'Anticipos de Sueldo'),
                A(code=u'4', name=u'Adelantos a Proveedores'),
                A(code=u'5', name=u'Anticipo Honorarios'),
                A(code=u'6', name=u'Adelantos Cuenta Particular', children=[
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
        ]),
        A(code=u'4', name=u'Inversiones', children=[
            A(code=u'1', name=u'Plazo Fijo'),
            A(code=u'2', name=u'Int. Plazo Fijo a devengar'),
            A(code=u'3', name=u'Prestamos a cobrar'),
            A(code=u'4', name=u'Int. Prestamos a devengar'),
            A(code=u'5', name=u'Acciones'),
            A(code=u'6', name=u'Otras Inversiones'),
        ]),
    ]),

    A(code=u'2', name=u'Activo No Corriente', children=[
        A(code=u'1', name=u'Rodados'),
        A(code=u'2', name=u'Inmuebles e instalaciones', children=[
            A(code=u'1', name=u'Terrenos'),
            A(code=u'2', name=u'Inmuebles'),
            A(code=u'3', name=u'Instalaciones comerciales'),
            A(code=u'4', name=u'Equipos de Oficina'),
            A(code=u'5', name=u'Equipos de Computación'),
        ]),
        A(code=u'3', name=u'Otros Activos Fijos'),
    ]),
])

pasivo = A(code=u'2', name=u'Pasivo', type=A.TYPE_DEBIT, children=[
    A(code=u'1', name=u'Pasivo Corriente', children=[
        A(code=u'1', name=u'Deudas Comerciales', children=[
            A(code=u'1', name=u'Proveedores Clase A'),
            A(code=u'2', name=u'Proveedores Clase B'),
            A(code=u'3', name=u'Proveedores Clase C'),
            A(code=u'4', name=u'Acreedores Varios'),
            A(code=u'5', name=u'Obligaciones a Pagar'),
        ]),
        A(code=u'2', name=u'Deudas Financieras', children=[
            A(code=u'1', name=u'Prestamos Bancarios'),
            A(code=u'2', name=u'Intereses a Devengar'),
        ]),
        A(code=u'3', name=u'Deudas Fiscales', children=[
            A(code=u'1', name=u'IVA Débito Fiscal'),
            A(code=u'2', name=u'IVA a Pagar'),
            A(code=u'3', name=u'IVA Retenciones a Depositar'),
            A(code=u'4', name=u'Ingresos Brutos a Pagar'),
            A(code=u'5', name=u'Moratoria AFIP'),
            A(code=u'6', name=u'Provisión Imp. Ganancias'),
        ]),
        A(code=u'4', name=u'Deudas Sociales', children=[
            A(code=u'1', name=u'Sueldos a Pagar'),
            A(code=u'2', name=u'Cargas Sociales a Pagar'),
            A(code=u'3', name=u'Sindicato a Pagar'),
            A(code=u'4', name=u'Seguro de Vida a Pagar'),
            A(code=u'5', name=u'FAECYS e INACAP a Pagar'),
            A(code=u'6', name=u'SAC a Pagar'),
            A(code=u'7', name=u'Vacaciones a Pagar'),
            A(code=u'8', name=u'Provisión SAC y Vacaciones'),
        ]),
        A(code=u'5', name=u'Otras Deudas', children=[
            A(code=u'1', name=u'Honorarios a Pagar'),
            A(code=u'2', name=u'Dividendos en Efectivo a Pagar'),
            A(code=u'3', name=u'Prestamos Cuenta Particular', children=[
                A(code=u'1', name=u'Prestamos de Carlos R.'),
                A(code=u'2', name=u'Prestamos de Augusto R.'),
                A(code=u'3', name=u'Prestamos de Germán R.'),
            ]),
            A(code=u'4', name=u'Anticipo Clientes'),
        ]),
    ]),
    A(code=u'2', name=u'Pasivo No Corriente'),
])

patrimonio = A(code=u'3', name=u'Patrimonio Neto', type=A.TYPE_DEBIT, children=[
    A(code=u'1', name=u'Capital Social', children=[
        A(code=u'1', name=u'Capital'),
    ]),
    A(code=u'2', name=u'Resultados Acumulados', children=[
        A(code=u'1', name=u'Reserva Legal'),
        A(code=u'2', name=u'Resultados No Asignado'),
        A(code=u'3', name=u'Resultados del Ejercicio'),
    ]),
])

session.add_all([activo, pasivo, patrimonio])
session.commit()

pretty_print(activo)
pretty_print(pasivo)
pretty_print(patrimonio)
