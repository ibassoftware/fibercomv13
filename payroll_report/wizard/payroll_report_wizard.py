# -*- coding: utf-8 -*-
from odoo import models, fields


class PayrollReportWizard(models.TransientModel):
    _name = 'payroll.report.wizard'

    date_from = fields.Date('From Date')
    date_to = fields.Date('To Date')
    company_id = fields.Many2one('res.company', string='Company')
    bank_account = fields.Char(string='Bank Account')
    status = fields.Selection([('draft', 'Draft'),
                               ('verify', 'Waiting'),
                               ('done', 'Done'),
                               ('cancel', 'Reject'),
                               ], string="Status", default='done')
    struct_id = fields.Many2one('hr.payroll.structure', string='Structure')

    def get_report(self):
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_start': self.date_from,
                'date_end': self.date_to,
                'company_id':  self.company_id and self.company_id.id or False,
                'bank_account':  self.bank_account or False,
                'status':  self.status or False,
                'struct_id': self.struct_id.id
            },
        }
        return self.env.ref('payroll_report.report_payroll_xlsx').report_action(self, data=data)
