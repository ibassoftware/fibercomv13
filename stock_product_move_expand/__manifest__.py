# -*- coding: utf-8 -*-
{
    'name': 'Stock Product Move expand',
    'category': 'Stock',
    'depends': ['stock'],
    'data': [
        'views/templates.xml',
        'views/stock_move_line_views.xml',
    ],
    'qweb': [
        "static/src/xml/product_moves_views.xml",
    ],
    'auto_install': True,
}
