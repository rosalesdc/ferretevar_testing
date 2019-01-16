# -*- coding: utf-8 -*-
{
    'name': "Cuenta Analitica",
    'description': """
        Agrega el tipo de cuenta analitica a las facturas de proveedor
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': ['base','account','account_invoicing','purchase'],
    'data': [
        'views/account_invoice_supplier_form.xml',
        ],
    'installable':True,
    'auto_install':False,
}
