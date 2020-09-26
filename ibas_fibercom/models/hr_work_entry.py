# -*- coding: utf-8 -*-
# Copyright YEAR(2020), AUTHOR(IBAS)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Added comment for commit
from odoo import fields, models, api

import logging
_logger = logging.getLogger(__name__)

class IbasHrWorkEntryType(models.Model):
    _inherit = 'hr.work.entry.type'

    is_payslip_display = fields.Boolean(string="Appears in Work Days")