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

    daily_wage = fields.Float(
        string='Daily Rate', compute='_compute_daily_rate')

    daily_wage_in_words = fields.Char(
        string='Daily Rate In Words', compute='_onchange_daily_wage', store=True)

    allowance = fields.Float(string='Untaxable Allowance')

    probationary_period = fields.Float(string='Probationary Period in Months')

    # Allowance
    rice_allowance = fields.Float(string="Rice Allowance")
    clothing_allowance = fields.Float(string="Clothing Allowance")
    per_diem = fields.Float(string="Per Diem")
    internet_allowance = fields.Float(string="Internet Allowance")
    other_allowance = fields.Float(string="Other Allowance")

    # Statutory Contribution

    sss_ec = fields.Float(string='SSS EC')
    sss_er = fields.Float(string='SSS ER')
    sss_ee = fields.Float(string='SSS EE')
    philhealth_personal = fields.Float(
        string='Philhealth Personal Share')
    philhealth_company = fields.Float(
        string='Philhealth Company Share')
    hdmf_personal = fields.Float(string='HDMF Personal Share', default=100)
    hdmf_company = fields.Float(string='HDMF Company Share', default=100)

    scheduled_pay = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi-annually', 'Semi-annually'),
        ('annually', 'Annually'),
        ('weekly', 'Weekly'),
        ('bi-weekly', 'Bi-weekly'),
        ('bi-monthly', 'Bi-monthly'),
        ('per-trip', 'Per-Trip'),
        ('daily', 'Daily'),
    ], string='Scheduled Pay', default='monthly', help="Defines the frequency of the wage payment.")

    @api.onchange('wage')
    def _onchange_philhealth(self):
        for rec in self:
            rec.philhealth_personal = (rec.wage * 0.03) / 2
            rec.philhealth_company = (rec.wage * 0.03) / 2

    @api.depends('wage', 'work_days')
    def _compute_daily_rate(self):
        for rec in self:
            wage = rec.wage
            if rec.work_days == 'six':
                daily = (wage * 12) / 313
            elif rec.work_days == 'five':
                daily = (wage * 12) / 261
            else:
                daily = 0

        self.daily_wage = daily

    @api.depends('wage')
    def _onchange_amount(self):
        for rec in self:
            whole = num2words(int(rec.wage)) + ' Pesos '
            whole = whole.replace(' and ', ' ')
            if "." in str(rec.wage):
                decimal_no = str(round(rec.wage, 2)).split(".")[1]
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
                decimal_no = str(round(rec.daily_wage, 2)).split(".")[1]
            if decimal_no:
                whole = whole + "and " + decimal_no + '/100'
            whole = whole.replace(',', '')
            rec.daily_wage_in_words = whole.upper() + " ONLY"

    @api.onchange('wage')
    def _onchange_sss(self):
        for rec in self:
            if rec.wage <= 0:
                rec.sss_er = 0
                rec.sss_ee = 0
                rec.sss_ec = 0

            elif rec.wage <= 2250:
                rec.sss_er = 160
                rec.sss_ee = 80
                rec.sss_ec = 10

            elif rec.wage < 2750:
                rec.sss_er = 200
                rec.sss_ee = 100
                rec.sss_ec = 10

            elif rec.wage < 3250:
                rec.sss_er = 240
                rec.sss_ee = 120
                rec.sss_ec = 10

            elif rec.wage < 3750:
                rec.sss_er = 280
                rec.sss_ee = 140
                rec.sss_ec = 10

            elif rec.wage < 4250:
                rec.sss_er = 320
                rec.sss_ee = 160
                rec.sss_ec = 10

            elif rec.wage < 4750:
                rec.sss_er = 360
                rec.sss_ee = 180
                rec.sss_ec = 10

            elif rec.wage < 5250:
                rec.sss_er = 400
                rec.sss_ee = 200
                rec.sss_ec = 10

            elif rec.wage < 5750:
                rec.sss_er = 440
                rec.sss_ee = 220
                rec.sss_ec = 10

            elif rec.wage < 6250:
                rec.sss_er = 480
                rec.sss_ee = 240
                rec.sss_ec = 10

            elif rec.wage < 6750:
                rec.sss_er = 520
                rec.sss_ee = 260
                rec.sss_ec = 10

            elif rec.wage < 7250:
                rec.sss_er = 560
                rec.sss_ee = 280
                rec.sss_ec = 10

            elif rec.wage < 7750:
                rec.sss_er = 600
                rec.sss_ee = 300
                rec.sss_ec = 10

            elif rec.wage < 8250:
                rec.sss_er = 640
                rec.sss_ee = 320
                rec.sss_ec = 10

            elif rec.wage < 8750:
                rec.sss_er = 680
                rec.sss_ee = 340
                rec.sss_ec = 10

            elif rec.wage < 9250:
                rec.sss_er = 720
                rec.sss_ee = 360
                rec.sss_ec = 10

            elif rec.wage < 9750:
                rec.sss_er = 760
                rec.sss_ee = 380
                rec.sss_ec = 10

            elif rec.wage < 10250:
                rec.sss_er = 800
                rec.sss_ee = 400
                rec.sss_ec = 10

            elif rec.wage < 10750:
                rec.sss_er = 840
                rec.sss_ee = 420
                rec.sss_ec = 10

            elif rec.wage < 11250:
                rec.sss_er = 880
                rec.sss_ee = 440
                rec.sss_ec = 10

            elif rec.wage < 11750:
                rec.sss_er = 920
                rec.sss_ee = 460
                rec.sss_ec = 10

            elif rec.wage < 12250:
                rec.sss_er = 960
                rec.sss_ee = 480
                rec.sss_ec = 10

            elif rec.wage < 12750:
                rec.sss_er = 1000
                rec.sss_ee = 500
                rec.sss_ec = 10

            elif rec.wage < 13250:
                rec.sss_er = 1040
                rec.sss_ee = 520
                rec.sss_ec = 10

            elif rec.wage < 13750:
                rec.sss_er = 1080
                rec.sss_ee = 540
                rec.sss_ec = 10

            elif rec.wage < 14250:
                rec.sss_er = 1120
                rec.sss_ee = 560
                rec.sss_ec = 10

            elif rec.wage < 14750:
                rec.sss_er = 1160
                rec.sss_ee = 580
                rec.sss_ec = 10

            elif rec.wage < 15250:
                rec.sss_er = 1200
                rec.sss_ee = 600
                rec.sss_ec = 30

            elif rec.wage < 15750:
                rec.sss_er = 1240
                rec.sss_ee = 620
                rec.sss_ec = 30

            elif rec.wage < 16250:
                rec.sss_er = 1280
                rec.sss_ee = 640
                rec.sss_ec = 30

            elif rec.wage < 16750:
                rec.sss_er = 1320
                rec.sss_ee = 660
                rec.sss_ec = 30

            elif rec.wage < 17250:
                rec.sss_er = 1360
                rec.sss_ee = 680
                rec.sss_ec = 30

            elif rec.wage < 17750:
                rec.sss_er = 1400
                rec.sss_ee = 700
                rec.sss_ec = 30

            elif rec.wage < 18250:
                rec.sss_er = 1440
                rec.sss_ee = 720
                rec.sss_ec = 30

            elif rec.wage < 18750:
                rec.sss_er = 1480
                rec.sss_ee = 740
                rec.sss_ec = 30

            elif rec.wage < 19250:
                rec.sss_er = 1520
                rec.sss_ee = 760
                rec.sss_ec = 30

            elif rec.wage <= 19750:
                rec.sss_er = 1560
                rec.sss_ee = 780
                rec.sss_ec = 30

            else:
                rec.sss_er = 1600
                rec.sss_ee = 800
                rec.sss_ec = 30
