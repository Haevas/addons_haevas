# -*- coding: utf-8 -*-
# Categories can be used to filter modules in modules listing
# github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
{
    'name': "lead demo report",

    'summary': """Create py3o reports for your leads (only interesting
    for training and demo""",

    'description': """
        Only use this module to learn how to use report_py3o
    """,

    'author': "XCG Consulting",
    'website': "http://odoo.consulting/",

    'category': 'Tools',
    'version': '0.1',
    'depends': [
        'base',
        'crm',
        'report_py3o',
    ],
    'data': [
        'reports/reports.xml',
    ],
}
