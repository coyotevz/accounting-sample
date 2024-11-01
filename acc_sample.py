# -*- coding: utf-8 -*-

from decimal import Decimal
from sqlalchemy.engine import create_engine
from acc import Base, Session, Account, AccountTransaction
from pp import print_account, print_transaction

A = Account

engine = create_engine("sqlite:///test_data_1.db")

Base.metadata.create_all(engine)

session = Session(bind=engine)

# Create accounts
# Estado Patrimonial
activo = A(
    code="1",
    name="Activo",
    type=A.TYPE_CREDIT,
    children=[
        A(
            code="1",
            name="Activo Corriente",
            children=[
                A(
                    code="1",
                    name="Caja y Bancos",
                    children=[
                        A(code="1", name="Caja General"),
                        A(code="2", name="Caja Beltrán"),
                        A(code="3", name="Caja Colón"),
                        A(code="4", name="Banco Santander Río Cta Cte"),
                        A(code="5", name="Banco Credicoop Cta Cte"),
                        A(code="6", name="Banco Nación Caja Seguridad"),
                        A(code="7", name="Valores a depósitar"),
                    ],
                ),
                A(
                    code="2",
                    name="Deudores por Ventas",
                    children=[
                        A(code="1", name="Cliente Clase A"),
                        A(code="2", name="Cliente Clase B"),
                        A(code="3", name="Cliente Clase C"),
                        A(code="4", name="Documentos a cobrar"),
                        A(code="5", name="Tarjeta VISA"),
                        A(code="6", name="Tarjeta Mastercard"),
                        A(code="7", name="Tarjeta Nevada"),
                    ],
                ),
                A(
                    code="3",
                    name="Créditos Fiscales",
                    children=[
                        A(code="1", name="IVA Crédito Fiscal"),
                        A(code="2", name="Retenciones sufridas IVA"),
                        A(code="3", name="IVA Saldo a Favor"),
                        A(code="4", name="Retenciones sufridas Ingresos Brutos"),
                        A(code="5", name="Ingresos Brutos Saldo a Favor"),
                        A(code="6", name="Retenciones sufridas Imp. Ganancias"),
                        A(code="7", name="Anticipo Imp. Ganancias"),
                        A(code="8", name="Retenciones sufridas SUSS"),
                        A(code="9", name="Otras retenciones sufridas"),
                    ],
                ),
                A(
                    code="4",
                    name="Otros Créditos",
                    children=[
                        A(code="1", name="Alquileres pagados por adelantado"),
                        A(code="2", name="Seguros pagados por adelantado"),
                        A(code="3", name="Anticipos de Sueldo"),
                        A(code="4", name="Adelantos a Proveedores"),
                        A(code="5", name="Anticipo Honorarios"),
                        A(
                            code="6",
                            name="Adelantos Cuenta Particular",
                            children=[
                                A(code="1", name="Adelantos a Carlos R."),
                                A(code="2", name="Adelantos a Augusto R."),
                                A(code="3", name="Adelantos a Germán R."),
                            ],
                        ),
                    ],
                ),
                A(
                    code="5",
                    name="Bienes de Cambio",
                    children=[
                        A(code="1", name="Mercadería Ciudad"),
                        A(code="2", name="Mercadería Godoy Cruz"),
                        A(code="3", name="Mercadería en Transito"),
                    ],
                ),
                A(
                    code="6",
                    name="Inversiones",
                    children=[
                        A(code="1", name="Plazo Fijo"),
                        A(code="2", name="Int. Plazo Fijo a devengar"),
                        A(code="3", name="Prestamos a cobrar"),
                        A(code="4", name="Int. Prestamos a devengar"),
                        A(code="5", name="Acciones"),
                        A(code="6", name="Otras Inversiones"),
                    ],
                ),
            ],
        ),
        A(
            code="2",
            name="Activo No Corriente",
            children=[
                A(code="1", name="Rodados"),
                A(
                    code="2",
                    name="Inmuebles e instalaciones",
                    children=[
                        A(code="1", name="Terrenos"),
                        A(code="2", name="Inmuebles"),
                        A(code="3", name="Instalaciones comerciales"),
                        A(code="4", name="Equipos de Oficina"),
                        A(code="5", name="Equipos de Computación"),
                    ],
                ),
                A(code="3", name="Otros Activos Fijos"),
            ],
        ),
    ],
)

pasivo = A(
    code="2",
    name="Pasivo",
    type=A.TYPE_DEBIT,
    children=[
        A(
            code="1",
            name="Pasivo Corriente",
            children=[
                A(
                    code="1",
                    name="Deudas Comerciales",
                    children=[
                        A(code="1", name="Proveedores Clase A"),
                        A(code="2", name="Proveedores Clase B"),
                        A(code="3", name="Proveedores Clase C"),
                        A(code="4", name="Acreedores Varios"),
                        A(code="5", name="Obligaciones a Pagar"),
                    ],
                ),
                A(
                    code="2",
                    name="Deudas Financieras",
                    children=[
                        A(code="1", name="Prestamos Bancarios"),
                        A(code="2", name="Intereses a Devengar"),
                    ],
                ),
                A(
                    code="3",
                    name="Deudas Fiscales",
                    children=[
                        A(code="1", name="IVA Débito Fiscal"),
                        A(code="2", name="IVA a Pagar"),
                        A(code="3", name="IVA Retenciones a Depositar"),
                        A(code="4", name="Ingresos Brutos a Pagar"),
                        A(code="5", name="Moratoria AFIP"),
                        A(code="6", name="Provisión Imp. Ganancias"),
                    ],
                ),
                A(
                    code="4",
                    name="Deudas Sociales",
                    children=[
                        A(code="1", name="Sueldos a Pagar"),
                        A(code="2", name="Cargas Sociales a Pagar"),
                        A(code="3", name="Sindicato a Pagar"),
                        A(code="4", name="Seguro de Vida a Pagar"),
                        A(code="5", name="FAECYS e INACAP a Pagar"),
                        A(code="6", name="SAC a Pagar"),
                        A(code="7", name="Vacaciones a Pagar"),
                        A(code="8", name="Provisión SAC y Vacaciones"),
                    ],
                ),
                A(
                    code="5",
                    name="Otras Deudas",
                    children=[
                        A(code="1", name="Honorarios a Pagar"),
                        A(code="2", name="Dividendos en Efectivo a Pagar"),
                        A(
                            code="3",
                            name="Prestamos Cuenta Particular",
                            children=[
                                A(code="1", name="Prestamos de Carlos R."),
                                A(code="2", name="Prestamos de Augusto R."),
                                A(code="3", name="Prestamos de Germán R."),
                            ],
                        ),
                        A(code="4", name="Anticipo Clientes"),
                    ],
                ),
            ],
        ),
        A(code="2", name="Pasivo No Corriente"),
    ],
)

patrimonio = A(
    code="3",
    name="Patrimonio Neto",
    type=A.TYPE_DEBIT,
    children=[
        A(
            code="1",
            name="Capital Social",
            children=[
                A(code="1", name="Capital"),
            ],
        ),
        A(
            code="2",
            name="Resultados Acumulados",
            children=[
                A(code="1", name="Reserva Legal"),
                A(code="2", name="Resultados No Asignado"),
                A(code="3", name="Resultados del Ejercicio"),
            ],
        ),
    ],
)

# Estado de Resultados
ingresos = A(
    code="4",
    name="Ingresos",
    type=A.TYPE_DEBIT,
    children=[
        A(code="1", name="Ventas"),
        A(code="2", name="Intereses Positivos"),
        A(code="3", name="Descuentos Obtenidos"),
    ],
)

egresos = A(
    code="5",
    name="Egresos",
    type=A.TYPE_CREDIT,
    children=[
        A(code="1", name="Costo de Mercaderias Vendidas"),
        A(code="2", name="Amortizaciones"),
        A(code="3", name="Alquileres Pagados"),
        A(code="4", name="Seguros"),
        A(code="5", name="Sueldos"),
        A(code="6", name="Cargas Sociales"),
        A(code="7", name="Honorarios"),
        A(code="8", name="Gastos de Librería"),
        A(code="9", name="Gastos Bancarios"),
        A(code="10", name="Intereses Negativos"),
        A(code="11", name="Impuesto Ingresos Brutos"),
        A(code="12", name="Impuesto Ganancias"),
        A(code="13", name="Impuesto Inmobiliario"),
        A(code="14", name="Servicios Públicos"),
        A(code="15", name="Telefonía e Internet"),
        A(code="16", name="Gastos en Infraestructura"),
        A(code="17", name="Gastos Financieros Tarjeta de Credito"),
        A(code="18", name="Publicidad"),
        A(code="19", name="Transporte"),
        A(code="20", name="Gastos Generales"),
    ],
)

session.add_all([activo, pasivo, patrimonio, ingresos, egresos])
session.commit()

caja = Account.query.get_by_code("1.1.1.1")
capital = Account.query.get_by_code("3.1.1")
banco = Account.query.get_by_code("2.1.2.1")

t1 = AccountTransaction(source=[(capital, 20000), (banco, 42800)], dest=(caja, 62800))
session.add(t1)
session.commit()

cta_cte = Account.query.get_by_code("1.1.2.1")  # Bco. Santander Cta. Cte.

t2 = AccountTransaction(source=[(caja, 12500)], dest=[(cta_cte, 12500)])

session.add(t2)
session.commit()

prov = Account.query.get_by_code("2.1.1.2")
merc = Account.query.get_by_code("1.1.5.1")
iva_cred = Account.query.get_by_code("1.1.3.1")
ret_iibb = Account.query.get_by_code("1.1.3.4")

t3 = AccountTransaction(
    source=[(prov, Decimal("5484.52"))],
    dest=[
        (merc, Decimal("4423")),
        (iva_cred, Decimal("928.83")),
        (ret_iibb, Decimal("132.69")),
    ],
)

session.add(t3)
session.commit()

cb = Account.query.get_by_code("1.1.1.2")
ventas = Account.query.get_by_code("4.1")
cmv = Account.query.get_by_code("5.1")
iva_deb = Account.query.get_by_code("2.1.3.1")

# Venta de mercadería y cobro en efectivo, 2 operaciones entre cuentas
t4a = AccountTransaction(
    source=[(ventas, 780), (iva_deb, Decimal("163.80"))],
    dest=[(cb, Decimal("943.80"))],
)
t4b = AccountTransaction(
    source=[(merc, 600)],
    dest=[(cmv, 600)],
)

session.add_all([t4a, t4b])
session.commit()

t5 = AccountTransaction(
    source=(caja, Decimal("3280.42")),
    dest=(prov, Decimal("3280.42")),
)

session.add(t5)
session.commit()


print("ASIENTOS")
print("--------")
print_transaction(t1)
print()
print_transaction(t2)
print()
print_transaction(t3)
print()
print_transaction(t4a)
print_transaction(t4b)
print()
print_transaction(t5)
print()

print("BALANCE")
print("-------")
print_account(activo, 3)
print_account(pasivo, 3)
print_account(patrimonio, 3)
print()
print()

print("ESTADO DE RESULTADO")
print("-------------------")
print_account(ingresos)
print_account(egresos)
print()
print()
