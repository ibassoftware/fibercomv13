# -*- coding: utf-8 -*-
# Copyright YEAR(2020), AUTHOR(IBAS)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Added comment for commit
from odoo import fields, models, api

import logging
_logger = logging.getLogger(__name__)


class IbasHrPayslip(models.Model):
    _inherit = 'hr.payslip'

    deduct_sss = fields.Boolean(string='Deduct SSS')
    deduct_hdmf = fields.Boolean(string='Deduct HDMF')
    deduct_philhealth = fields.Boolean(string='Deduct Philhealth')
    deduct_mpl = fields.Boolean(string='Deduct MPL')
    generate_backpay = fields.Boolean(string='Generate 13th Month Pay/BackPay')
    deduct_healthcard = fields.Boolean(string='Deduct Healthcard')
