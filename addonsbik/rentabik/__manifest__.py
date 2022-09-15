# -*- coding: utf-8 -*-
{
    'name': "rentabik",

    'summary': """
        odoo module for rentabike""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'report/wizzard_penjualanreport_template.xml',
        'wizzard/kendaraandatang_wizzard.xml',
        'wizzard/penjualanreport_wizzard.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/kelompoksepeda.xml',
        'views/kendaraan.xml',
        'views/person.xml',
        'views/kasir.xml',
        'views/konsumen.xml',
        'views/supplier.xml',
        'views/direksi.xml',
        'views/penjualan.xml',
        'report/report.xml',
        'report/penjualanpdf.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
