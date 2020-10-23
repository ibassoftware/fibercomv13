# -*- coding: utf-8 -*-
# Copyright YEAR(2020), AUTHOR(IBAS)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Added comment for commit
from odoo import fields, models, api, _
from odoo.tools.misc import format_date
from odoo.tools import date_utils

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
    is_deduct_loans = fields.Boolean(string="Deduct loans")

    @api.onchange('employee_id', 'struct_id', 'contract_id', 'date_from', 'date_to')
    def _onchange_employee(self):
        if (not self.employee_id) or (not self.date_from) or (not self.date_to):
            return

        employee = self.employee_id
        date_from = self.date_from
        date_to = self.date_to

        self.company_id = employee.company_id
        if not self.contract_id or self.employee_id != self.contract_id.employee_id:
            contracts = employee._get_contracts(date_from, date_to)

            if not contracts or not contracts[0].struct_id:
                self.contract_id = False
                self.struct_id = False
                return
            self.contract_id = contracts[0]
            self.struct_id = contracts[0].struct_id

        payslip_name = self.struct_id.payslip_name or _('Salary Slip')
        self.name = '%s - %s - %s' % (payslip_name, self.employee_id.name or '', format_date(self.env, self.date_from, date_format="MMMM y"))

        if date_to > date_utils.end_of(fields.Date.today(), 'month'):
            self.warning_message = _("This payslip can be erroneous! Work entries may not be generated for the period from %s to %s." %
                (date_utils.add(date_utils.end_of(fields.Date.today(), 'month'), days=1), date_to))
        else:
            self.warning_message = False

        self.worked_days_line_ids = self._get_new_worked_days_lines()

    def _get_worked_day_lines(self):
        res = super(IbasHrPayslip, self)._get_worked_day_lines()

        new_res = []
        for result in res:
            work_entry_type_id = result['work_entry_type_id']
            work_entry_type_record = self.env['hr.work.entry.type'].browse(work_entry_type_id)
            is_payslip_display = work_entry_type_record.is_payslip_display
            result['number_of_minutes'] = result['number_of_days'] * (result['number_of_hours'] * 60)
            if is_payslip_display:
                new_res.append(result)

        return new_res

class IbasHrPayslipWorkedDays(models.Model):
    _inherit = 'hr.payslip.worked_days'

    number_of_minutes = fields.Float(string='Number of Minutes')