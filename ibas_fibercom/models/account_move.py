# -*- coding: utf-8 -*-
# Copyright YEAR(2019), AUTHOR(IBAS)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Added comment for commit
from odoo import fields, models, api

import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    bus_style = fields.Char(string='Bus. Style')
    # bs_no = fields.Char(string='B.S. No.')
    sale_no = fields.Char(string='S.O. No.')
    purchase_no = fields.Char(string='P.O. No.')
    delivery_no = fields.Char(string='D.R. No.')
    approved_by = fields.Many2one('res.users', string='Approved By')
    received_by = fields.Many2one('res.users', string='Received By')


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account',
                                          index=True)

    analytic_tag_ids = fields.Many2many(
        'account.analytic.tag', string='Analytic Tags')

    @api.onchange('analytic_account_id', 'analytic_tag_ids')
    def _onchange_analytic_account(self):
        for rec in self:
            if rec.purchase_line_id:
                rec.purchase_line_id.account_analytic_id = rec.analytic_account_id.id
                rec.purchase_line_id.analytic_tag_ids = rec.analytic_tag_ids.ids
