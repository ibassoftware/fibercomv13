# -*- coding: utf-8 -*-

from odoo import fields, models


class Payslip(models.Model):
    _inherit = 'hr.payslip'

    is_imported = fields.Boolean(readonly=True, default=False)
