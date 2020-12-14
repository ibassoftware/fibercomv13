# -*- coding: utf-8 -*-
{
    'name': 'Payroll Report',
    'category': 'Human Resources',
    'depends': ['ibas_fibercom', 'report_xlsx'],
    'data': [
        'views/views.xml',
        'wizard/payroll_report_wizard_view.xml',
    ],
    'qweb': [
    ],
    'auto_install': True,
}
