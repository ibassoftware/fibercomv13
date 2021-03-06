# -*- coding: utf-8 -*-
{
    'name': "ibas_fibercom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "IBAS",
    'website': "http://www.ibasuite.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'purchase', 'asset', 'hr', 'hr_payroll', 'hr_holidays', 'wk_odoo_directly_print_reports'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/time_off_security.xml',
        'data/ir_sequence_data.xml',
        'data/report_paperformat_data.xml',
        'data/hr_payslip_email_template.xml',
        'data/wk_printer.xml',
        'data/report_data.xml',
        'data/hr_payroll_data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/stock.xml',
        'views/action_server.xml',
        'views/sale_order.xml',
        'views/account_move_views.xml',
        'views/product.xml',
        'views/hr_employee_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_contract_type_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_loan_views.xml',
        'views/hr_work_entry_type_views.xml',
        'report/delivery_slip.xml',
        'report/purchase_order.xml',
        'report/report_account_stp.xml',
        'report/report_transfer_barcode_zpl.xml',
        'report/report_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
