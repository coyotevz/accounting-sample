# -*- coding: utf-8 -*-

from decimal import Decimal
from sqlalchemy.engine import create_engine
from acc import Base, Session, Account, AccountQuery, AccountTransaction
from pp import print_account, print_transaction

A = Account

engine = create_engine('sqlite:///test_data_1.db')

Base.metadata.bind = engine
Base.metadata.create_all()

session = Session(bind=engine)

# Create accounts
# Estado Patrimonial
activo = A(code=u'1', name=u'Activo', type=A.TYPE_CREDIT, children=[
    A(code=u'1', name=u'Activo Corriente', children=[
        A(code=u'1', name=u'Caja y Bancos', children=[
            A(code=u'1', name=u'Caja General'),
            A(code=u'2', name=u'Caja Beltrán'),
            A(code=u'3', name=u'Caja Colón'),
            A(code=u'4', name=u'Banco Santander Río Cta Cte'),
            A(code=u'5', name=u'Banco Credicoop Cta Cte'),
            A(code=u'6', name=u'Banco Nación Caja Seguridad'),
            A(code=u'7', name=u'Valores a depósitar'),
        ]),
        A(code=u'2', name=u'Deudores por Ventas', children=[
            A(code=u'1', name=u'Cliente Clase A'),
            A(code=u'2', name=u'Cliente Clase B'),
            A(code=u'3', name=u'Cliente Clase C'),
            A(code=u'4', name=u'Documentos a cobrar'),
            A(code=u'5', name=u'Tarjeta VISA'),
            A(code=u'6', name=u'Tarjeta Mastercard'),
            A(code=u'7', name=u'Tarjeta Nevada'),
        ]),
        A(code=u'3', name=u'Créditos Fiscales', children=[
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
        A(code=u'4', name=u'Otros Créditos', children=[
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
        A(code=u'5', name=u'Bienes de Cambio', children=[
            A(code=u'1', name=u'Mercadería Ciudad'),
            A(code=u'2', name=u'Mercadería Godoy Cruz'),
            A(code=u'3', name=u'Mercadería en Transito'),
        ]),
        A(code=u'6', name=u'Inversiones', children=[
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

# Estado de Resultados
ingresos = A(code=u'4', name=u'Ingresos', type=A.TYPE_DEBIT, children=[
    A(code=u'1', name=u'Ventas'),
    A(code=u'2', name=u'Intereses Positivos'),
    A(code=u'3', name=u'Descuentos Obtenidos'),
])

egresos = A(code=u'5', name=u'Egresos', type=A.TYPE_CREDIT, children=[
    A(code=u'1', name=u'Costo de Mercaderias Vendidas'),
    A(code=u'2', name=u'Amortizaciones'),
    A(code=u'3', name=u'Alquileres Pagados'),
    A(code=u'4', name=u'Seguros'),
    A(code=u'5', name=u'Sueldos'),
    A(code=u'6', name=u'Cargas Sociales'),
    A(code=u'7', name=u'Honorarios'),
    A(code=u'8', name=u'Gastos de Librería'),
    A(code=u'9', name=u'Gastos Bancarios'),
    A(code=u'10', name=u'Intereses Negativos'),
    A(code=u'11', name=u'Impuesto Ingresos Brutos'),
    A(code=u'12', name=u'Impuesto Ganancias'),
    A(code=u'13', name=u'Impuesto Inmobiliario'),
    A(code=u'14', name=u'Servicios Públicos'),
    A(code=u'15', name=u'Telefonía e Internet'),
    A(code=u'16', name=u'Gastos en Infraestructura'),
    A(code=u'17', name=u'Gastos Financieros Tarjeta de Credito'),
    A(code=u'18', name=u'Publicidad'),
    A(code=u'19', name=u'Transporte'),
    A(code=u'20', name=u'Gastos Generales'),
])

session.add_all([activo, pasivo, patrimonio, ingresos, egresos])
session.commit()

caja = Account.query.get_by_code(u'1.1.1.1')
capital = Account.query.get_by_code(u'3.1.1')
banco = Account.query.get_by_code(u'2.1.2.1')

t1 = AccountTransaction(
    source=[(capital, 20000), (banco, 42800)],
    dest=(caja, 62800)
)
session.add(t1)
session.commit()

cta_cte = Account.query.get_by_code(u'1.1.2.1') # Bco. Santander Cta. Cte.

t2 = AccountTransaction(
    source=[(caja, 12500)],
    dest=[(cta_cte, 12500)]
)

session.add(t2)
session.commit()

prov = Account.query.get_by_code(u'2.1.1.2')
merc = Account.query.get_by_code(u'1.1.5.1')
iva_cred = Account.query.get_by_code(u'1.1.3.1')
ret_iibb = Account.query.get_by_code(u'1.1.3.4')

t3 = AccountTransaction(
    source=[(prov, Decimal('5484.52'))],
    dest=[(merc, Decimal('4423')),
          (iva_cred, Decimal('928.83')),
          (ret_iibb, Decimal('132.69'))]
)

session.add(t3)
session.commit()

cb = Account.query.get_by_code(u'1.1.1.2')
ventas = Account.query.get_by_code(u'4.1')
cmv = Account.query.get_by_code(u'5.1')
iva_deb = Account.query.get_by_code(u'2.1.3.1')

# Venta de mercadería y cobro en efectivo, 2 operaciones entre cuentas
t4a = AccountTransaction(
    source=[(ventas, 780), (iva_deb, Decimal('163.80'))],
    dest=[(cb, Decimal('943.80'))],
)
t4b = AccountTransaction(
    source=[(merc, 600)],
    dest=[(cmv, 600)],
)

session.add_all([t4a, t4b])
session.commit()

t5 = AccountTransaction(
    source=(caja, Decimal('3280.42')),
    dest=(prov, Decimal('3280.42')),
)

session.add(t5)
session.commit()


print "ASIENTOS"
print "--------"
print_transaction(t1)
print
print_transaction(t2)
print
print_transaction(t3)
print
print_transaction(t4a)
print_transaction(t4b)
print
print_transaction(t5)
print

print "BALANCE"
print "-------"
print_account(activo, 3)
print_account(pasivo, 3)
print_account(patrimonio, 3)
print
print

print "ESTADO DE RESULTADO"
print "-------------------"
print_account(ingresos)
print_account(egresos)
print
print
