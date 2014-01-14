# -*- coding: utf-8 -*-

from decimal import Decimal
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from acc import Base, Account

A = Account

engine = create_engine('sqlite:///test_data_2.db', echo=True)
session = sessionmaker(bind=engine)()
Base.metadata.bind = engine
Base.metadata.create_all()

activo = A(code=u'1', name=u'Activo', type=A.TYPE_CREDIT, children=[
    A(code=u'1', name=u'Activo Corriente', children=[
        A(code=u'1', name=u'Caja y Bancos', children=[
            A(code=u'1', name=u'Caja General'),
            A(code=u'2', name=u'Caja Beltrán'),
            A(code=u'3', name=u'Caja Godoy Cruz'),
            A(code=u'4', name=u'Banco Santander Río Cta Cte'),
            A(code=u'5', name=u'Banco Credicoop Cta Cte'),
            A(code=u'6', name=u'Banco Nacion Caja Seguridad'),
            A(code=u'7', name=u'Valores a Depositar'),
        ]),
        A(code=u'2', name=u'Deudores por Venta', children=[
            A(code=u'1', name=u'Clientes clase A'),
            A(code=u'2', name=u'Clientes clase B'),
            A(code=u'3', name=u'Clientes clase C'),
            A(code=u'4', name=u'Documentos a cobrar'),
            A(code=u'5', name=u'Tarjeta VISA'),
            A(code=u'6', name=u'Tarjeta Mastercard'),
            A(code=u'7', name=u'Tarjeta Nevada'),
        ]),
        A(code=u'3', name=u'Inversiones', children=[
            A(code=u'1', name=u'Plazo Fijo'),
            A(code=u'2', name=u'Int. Plazo Fijo a Devengar'),
            A(code=u'3', name=u'Prestamos a Cobrar'),
            A(code=u'4', name=u'Int. Prestamos a Devengar'),
            A(code=u'5', name=u'Acciones'),
            A(code=u'6', name=u'Otras Inversiones'),
        ]),
        A(code=u'4', name=u'Otros Créditos', children=[
            A(code=u'1', name=u'IVA Crédito Fiscal'),
            A(code=u'2', name=u'IVA Saldo a Favor'),
            A(code=u'3', name=u'IVA Retenciones a Favor'),
            A(code=u'4', name=u'Alquileres pagados por Adelantado'),
            A(code=u'5', name=u'Seguros pagados por Adeltantado'),
            A(code=u'6', name=u'Anticipos al Personal'),
            A(code=u'7', name=u'Adelanto de Vacaciones'),
            A(code=u'8', name=u'Anticipo a Proveedores'),
            A(code=u'9', name=u'Anticipo Impuesto a Ganancias'),
            A(code=u'10', name=u'Anticipo Honorarios'),
            A(code=u'11', name=u'Cuenta Particular'),
        ]),
        A(code=u'5', name=u'Bienes de Cambio', children=[
            A(code=u'1', name=u'Mercadería Clase A'),
            A(code=u'2', name=u'Mercadería Clase B'),
            A(code=u'3', name=u'Mercadería Calse C'),
        ])
    ]),
    A(code=u'2', name=u'Activo No Corriente', children=[
        A(code=u'1', name=u'Bienes de Uso', children=[
            A(code=u'1', name=u'Rodados'),
            A(code=u'2', name=u'Amortización Acumulada Rodados'),
            A(code=u'3', name=u'Equipos de Computación'),
            A(code=u'4', name=u'Amortización Acumulada Equipos de Computación'),
            A(code=u'5', name=u'Muebles y Útiles'),
            A(code=u'6', name=u'Amortización Acumulada Muebles y Útiles'),
            A(code=u'7', name=u'Instalaciones'),
            A(code=u'8', name=u'Amortización Acumulada Instalaciones'),
            A(code=u'9', name=u'Inmuebles'),
            A(code=u'10', name=u'Amortización Acumulada Inmuebles'),
        ])
    ])
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
            A(code=u'6', name=u'Provisión Impuesto Ganancias'),
        ]),
        A(code=u'4', name=u'Deudas Sociales a Pagar', children=[
            A(code=u'1', name=u'Sueldos a Pagar'),
            A(code=u'2', name=u'Cargas Sociales a Pagar'),
            A(code=u'3', name=u'Sindicato a Pagar'),
            A(code=u'4', name=u'Seguro de Vida a Pagar'),
            A(code=u'5', name=u'SAC a Pagar'),
            A(code=u'6', name=u'Vacaciones a Pagar'),
            A(code=u'7', name=u'Provisión SAC y Vacaciones'),
        ]),
        A(code=u'5', name=u'Otras Deudas', children=[
            A(code=u'1', name=u'Honorarios a Pagar'),
            A(code=u'2', name=u'Dividendos en Efectivo a Pagar'),
            A(code=u'3', name=u'Anticipo Clientes'),
        ])
    ]),
    A(code=u'2', name=u'Pasvio No Corriente', children=[
    ]),
])

patrimonio = A(code=u'3', name=u'Patrimonio Neto', type=A.TYPE_DEBIT, children=[
    A(code=u'1', name=u'Capital Social', children=[
        A(code=u'1', name=u'Capital')
    ]),
    A(code=u'2', name=u'Resultados Acumulados', children=[
        A(code=u'1', name=u'Reserva Legal'),
        A(code=u'2', name=u'Resultados No Asignados'),
        A(code=u'3', name=u'Resultados del Ejercicio'),
    ])
])

session.add_all([activo, pasivo, patrimonio])
session.commit()
