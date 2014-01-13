# -*- coding: utf-8 -*-

from decimal import Decimal
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from acc import Base, Account

engine = create_engine('sqlite:///test_data.db', echo=True)
session = sessionmaker(bind=engine)()
Base.metadata.bind = engine
Base.metadata.create_all()

# Create accounts
activo = Account(code=u'1', name=u'Activo')
ac_co = Account(code=u'1', name=u'Activo Corriente', parent=activo)
ac_nc = Account(code=u'2', name=u'Activo No Corriente', parent=activo)

cyb = Account(code=u'1', name=u'Caja y Bancos', parent=ac_co)
caja = Account(code=u'1', name=u'Caja', parent=cyb)
caja_1 = Account(code=u'1', name=u'Caja General', parent=caja)
caja_2 = Account(code=u'2', name=u'Caja Beltrán', parent=caja)
caja_3 = Account(code=u'3', name=u'Caja Colón', parent=caja)

bancos = Account(code=u'1', name=u'Bancos', parent=cyb)
b1 = Account(code=u'1', name=u'Banco Santander Río Cta Cte', parent=bancos)
b2 = Account(code=u'2', name=u'Banco Credicoop Cta Cte', parent=bancos)
b3 = Account(code=u'3', name=u'Banco Nación Caja Seguridad', parent=bancos)
vd = Account(code=u'4', name=u'Valores a depósitar', parent=bancos)

cred = Account(code=u'2', name=u'Créditos', parent=ac_co)

dxp = Account(code=u'1', name=u'Deudores por Ventas', parent=cred)
cliente_a = Account(code=u'1', name=u'Cliente clase A', parent=dxp)
cliente_b = Account(code=u'2', name=u'Cliente clase B', parent=dxp)
cliente_c = Account(code=u'3', name=u'Cliente clase C', parent=dxp)
tarjeta_1 = Account(code=u'4', name=u'Tarjeta VISA', parent=dxp)
tarjeta_2 = Account(code=u'5', name=u'Tarjeta Mastercard', parent=dxp)
tarjeta_3 = Account(code=u'6', name=u'Tarjeta Nevada', parent=dxp)

cac = Account(code=u'2', name=u'Créditos Fiscales', parent=cred)
ivadb = Account(code=u'1', name=u'IVA Crédito Fiscal', parent=cac)
ivaret = Account(code=u'2', name=u'Retenciones sufridas IVA', parent=cac)
iibbret = Account(code=u'3', name=u'Retenciones sufridas Ingresos Brutos', parent=cac)
ganret = Account(code=u'4', name=u'Retenciones sufridas Imp. Ganancias', parent=cac)
sussrt = Account(code=u'5', name=u'Retenciones sufridas SUSS', parent=cac)
otras = Account(code=u'6', name=u'Otras retenciones sufridas', parent=cac)

oc = Account(code=u'3', name=u'Otros Créditos', parent=cred)
ads = Account(code=u'1', name=u'Adelantos de Sueldo', parent=oc)
adp = Account(code=u'2', name=u'Adelantos a Proveedores', parent=oc)
add = Account(code=u'3', name=u'Adelantos a Socios', parent=oc)
ad_c = Account(code=u'1', name=u'Adelantos a Carlos R.', parent=add)
ad_a = Account(code=u'2', name=u'Adelantos a Augusto R.', parent=add)
ad_g = Account(code=u'3', name=u'Adelantos a Germán R.', parent=add)

merca = Account(code=u'3', name=u'Bienes de Cambio', parent=ac_co)
merca_1 = Account(code=u'1', name=u'Mercadería Ciudad', parent=merca)
merca_2 = Account(code=u'2', name=u'Mercadería Godoy Cruz', parent=merca)
merca_3 = Account(code=u'3', name=u'Mercadería en Transito', parent=merca)

rodados = Account(code=u'1', name=u'Rodados', parent=ac_nc)
inm = Account(code=u'2', name=u'Inmuebles e instalaciones', parent=ac_nc)
terr = Account(code=u'1', name=u'Terrenos', parent=inm)
inmuebles = Account(code=u'2', name=u'Inmuebles', parent=inm)
inst = Account(code=u'3', name=u'Instalaciones comerciales', parent=inm)
ofic = Account(code=u'4', name=u'Equipos de Oficina', parent=inm)
act_f = Account(code=u'3', name=u'Otros Activos Fijos', parent=ac_nc)

pasivo = Account(code=u'2', name=u'Pasivo')
p_co = Account(code=u'1', name=u'Pasivo Corriente', parent=pasivo)
p_nc = Account(code=u'2', name=u'Pasivo No Corriente', parent=pasivo)

pn = Account(code=u'3', name=u'Patrimonio Neto')
capital = Account(code=u'1', name=u'Capital', parent=pn)
reser = Account(code=u'2', name=u'Reservas', parent=pn)
res_ac = Account(code=u'3', name=u'Resultados Acumulados', parent=pn)
eje_ac = Account(code=u'4', name=u'Resultados Acumulados Ejercicios Anteriores', parent=pn)

session.add(activo)
session.commit()
