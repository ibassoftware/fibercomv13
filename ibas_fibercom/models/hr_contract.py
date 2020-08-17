# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from num2words import num2words


import logging
_logger = logging.getLogger(__name__)


class IbasHRPayrollStructure(models.Model):
    _inherit = 'hr.payroll.structure'

    type_id = fields.Many2one('hr.payroll.structure.type', required=False)


class IbasHRContract(models.Model):
    _inherit = 'hr.contract'

    type_id = fields.Char(string='Contract Type')
    struct_id = fields.Many2one(
        'hr.payroll.structure', string='Salary Structure')

    # Monthly Advantages in Cash

    amount_in_words = fields.Char(
        string='Wage In Words', compute='_onchange_amount', store=True)

    work_days = fields.Selection([
        ('six', 'Six Days'),
        ('five', 'Five Days')
    ], string='Work Days')

    daily_wage = fields.Float(string='Daily Rate')

    daily_wage_in_words = fields.Char(
        string='Daily Rate In Words', compute='_onchange_daily_wage', store=True)

    allowance = fields.Float(string='Untaxable Allowance')

    probationary_period = fields.Float(string='Probationary Period in Months')

    # Statutory Contribution

    sss_ec = fields.Float(string='SSS EC')
    sss_er = fields.Float(string='SSS ER')
    sss_ee = fields.Float(string='SSS EE')
    philhealth_personal = fields.Float(string='Philhealth Personal Share')
    philhealth_company = fields.Float(string='Philhealth Company Share')
    hdmf_personal = fields.Float(string='HDMF Personal Share', default=100)
    hdmf_company = fields.Float(string='HDMF Company Share', default=100)

    schedule_pay = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi-annually', 'Semi-annually'),
        ('annually', 'Annually'),
        ('weekly', 'Weekly'),
        ('bi-weekly', 'Bi-weekly'),
        ('bi-monthly', 'Bi-monthly'),
        ('per-trip', 'Per-Trip'),
        ('daily', 'Daily'),
    ], string='Scheduled Pay', index=True, default='monthly', help="Defines the frequency of the wage payment.")

    @api.depends('wage')
    def _onchange_amount(self):
        for rec in self:
            whole = num2words(int(rec.wage)) + ' Pesos '
            whole = whole.replace(' and ', ' ')
            if "." in str(rec.wage):
                decimal_no = str(rec.wage).split(".")[1]
            if decimal_no:
                whole = whole + "and " + decimal_no + '/100'
            whole = whole.replace(',', '')
            rec.amount_in_words = whole.upper() + " ONLY"

    @api.depends('daily_wage')
    def _onchange_daily_wage(self):
        for rec in self:
            whole = num2words(int(rec.daily_wage)) + ' Pesos '
            whole = whole.replace(' and ', ' ')
            if "." in str(rec.daily_wage):
                decimal_no = str(rec.daily_wage).split(".")[1]
            if decimal_no:
                whole = whole + "and " + decimal_no + '/100'
            whole = whole.replace(',', '')
            rec.daily_wage_in_words = whole.upper() + " ONLY"
