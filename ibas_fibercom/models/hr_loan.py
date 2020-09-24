# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _


class Loan(models.Model):
    _name = "hr.loan"
    _description = 'Employee Loans'

    @api.model
    def _default_currency(self):
        return self.env.user.company_id.currency_id.id

    employee_id = fields.Many2one('hr.employee', string="Employee")
    date_from = fields.Date('From Date')
    date_to = fields.Date('To Date')
    currency_id = fields.Many2one('res.currency', default=_default_currency)
    amount_total = fields.Monetary(string="Total Loan Amount")
    amount_deduct = fields.Monetary(string="Deduction Amount")
    type = fields.Selection(
        [('sss', 'SSS'), ('hdmf', 'HDMF'), ('other', 'OTHER')], string='Type')
    amount_total_deducted = fields.Monetary(string="Total Deducted Amount")
    state = fields.Selection([('draft', 'Draft'), ('open', 'In Progress'), ('done', 'Done')], string="Status",
                             default="draft", store=True)

    def action_open(self):
        self.write({'state': 'open'})

    def action_set_to_draft(self):
        self.write({'state': 'draft'})

    def name_get(self):
        result = []
        for loan in self:
            amount_str = 0.0
            if loan.currency_id.position == 'before':
                amount_str = loan.currency_id.symbol + \
                    ' ' + str(loan.amount_total)
            if loan.currency_id.position == 'after':
                amount_str = str(loan.amount_total) + ' ' + \
                    loan.currency_id.symbol
            result.append((loan.id, "[%s] %s" %
                           (amount_str, loan.employee_id.name)))
        return result
