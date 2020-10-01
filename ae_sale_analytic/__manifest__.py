# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AE Sale Analytic',
    'version': '1.1',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/sale_views.xml',
        'views/partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}