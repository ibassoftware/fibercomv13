# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Respartner(models.Model):
    
    _inherit = 'res.partner'

    analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account')