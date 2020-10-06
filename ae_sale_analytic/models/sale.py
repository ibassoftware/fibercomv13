# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_analytic_account(self):
        if self.partner_id.analytic_id:
            self.write({'analytic_account_id':self.partner_id.analytic_id})
