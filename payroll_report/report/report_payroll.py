# -*- coding: utf-8 -*-
from odoo import models
import logging
from datetime import datetime
_logger = logging.getLogger(__name__)


class PayrollXlsx(models.AbstractModel):
    _name = 'report.ibas_payroll.report_payroll'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objs):
        date_from = data['form']['date_start']
        date_to = data['form']['date_end']
        company_id = data['form']['company_id']
        status = data['form']['status']
        bank_account = data['form']['bank_account'] and data['form']['bank_account'].upper(
        )

        format1 = workbook.add_format(
            {'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9'})

        title2 = workbook.add_format(
            {'text_wrap': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9'})

        bg_flesh = workbook.add_format(
            {'bg_color': '#FDE9D9', 'border': 1, 'border_color': '#D9D9D9'})

        bg_gross_title = workbook.add_format(
            {'text_wrap': True, 'bg_color': '#92D050', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9'})

        bg_gross = workbook.add_format(
            {'bg_color': '#92D050', 'border': 1, 'border_color': '#D9D9D9'})

        bg_tot_deduct_title = workbook.add_format(
            {'text_wrap': True, 'bg_color': '#FFC000', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9'})

        bg_tot_deduct = workbook.add_format(
            {'bg_color': '#FFC000', 'border': 1, 'border_color': '#D9D9D9'})

        bg_net_pay_title = workbook.add_format(
            {'text_wrap': True, 'bg_color': 'yellow', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9'})

        bg_net_pay = workbook.add_format(
            {'bg_color': 'yellow', 'border': 1, 'border_color': '#D9D9D9'})

        sheet = workbook.add_worksheet()

        sheet.set_column('A:A', 2.22)
        sheet.set_column('B:B', 24)
        sheet.set_column('C:L', 9)
        sheet.set_column('M:M', 10)
        sheet.set_column('N:W', 9)
        sheet.set_column('X:Z', 11)

        sheet.set_row(2, 69)

        sheet.write(0, 1, "PAYROLL PERIOD:", format1)

        sheet.write(1, 4, "Rate", format1)
        sheet.merge_range('E2:F2', 'Basic', format1)
        sheet.merge_range('G2:AD2', 'Premiums', format1)
        sheet.merge_range('AE2:AF2', 'Allowance', format1)
        sheet.merge_range('AH2:AL2', 'Deductions', format1)
        sheet.merge_range('AM2:AP2', 'Employee Contributions', format1)
        sheet.merge_range('AQ2:AY2', 'Loans', format1)
        sheet.merge_range('AZ2:BB2', 'Adjustments', format1)

        sheet.write(2, 0, "")
        sheet.write(2, 1, "Name", format1)
        sheet.write(2, 2, "Remarks", title2)
        sheet.write(2, 3, "Department", title2)

        sheet.write(2, 4, "Basic Pay", title2)
        sheet.write(2, 5, "Additioanal Allowance", title2)

        sheet.write(2, 6, "Regular Overtime", title2)
        sheet.write(2, 7, "Regular Holiday Overtime", title2)
        sheet.write(2, 8, "Special Holiday Overtime", title2)
        sheet.write(2, 9, "Rest Day Overtim9", title2)
        sheet.write(2, 10, "Rest Day Regular Holiday Overtime", title2)
        sheet.write(2, 11, "Rest Day Special Holiday Overtime", title2)
        sheet.write(2, 12, "Night Shift Overtime", title2)
        sheet.write(2, 13, "Rest Day Night Shift Overtime", title2)
        sheet.write(2, 14, "Special Holiday Night Shift Overtime", title2)
        sheet.write(2, 15, "Rest Day Special Holiday Night Shift Overtime", title2)
        sheet.write(2, 16, "Regular Holiday Night Shift Overtime", title2)
        sheet.write(2, 17, "Rest Day Regular Holiday Night Shift Overtime", title2)
        sheet.write(2, 18, "Regular Holiday", title2)
        sheet.write(2, 19, "Special Holiday", title2)
        sheet.write(2, 20, "Rest Day", title2)
        sheet.write(2, 21, "Rest Day Regular Holiday", title2)
        sheet.write(2, 22, "Rest Day Special Holiday", title2)
        sheet.write(2, 23, "Night Differential", title2)
        sheet.write(2, 24, "Regular Holiday Night Shift", title2)
        sheet.write(2, 25, "Special Holiday Night Shift", title2)
        sheet.write(2, 26, "Rest Day Night Differential", title2)
        sheet.write(2, 27, "Rest Day Regular Holiday Night Shift", title2)
        sheet.write(2, 28, "Double Holiday Night Shift", title2)
        sheet.write(2, 29, "Rest Day Double Holiday Night Shift", title2)

        sheet.write(2, 30, "Rice Allowance", title2)
        sheet.write(2, 31, "Clothing Allowance", title2)

        sheet.write(2, 32, "Gross Pay", bg_gross_title)

        sheet.write(2, 33, "Withholding Tax", title2)
        sheet.write(2, 34, "Lates", title2)
        sheet.write(2, 35, "Undertime", title2)
        sheet.write(2, 36, "Absent", title2)
        sheet.write(2, 37, "Total Deductions", bg_tot_deduct)

        sheet.write(2, 38, "SSS Employee Share", title2)
        sheet.write(2, 39, "HDMF Employee Share", title2)
        sheet.write(2, 40, "Additional HDMF Employee Share", title2)
        sheet.write(2, 41, "Philhealth Employee Share", title2)

        sheet.write(2, 42, "SSS Loan", title2)
        sheet.write(2, 43, "HDMF Loan", title2)
        sheet.write(2, 44, "Bayanihan Loan", title2)
        sheet.write(2, 45, "Bayanihan", title2)
        sheet.write(2, 46, "Personal Charges", title2)
        sheet.write(2, 47, "Health Card", title2)
        sheet.write(2, 48, "Calamity Loan", title2)
        sheet.write(2, 49, "Other Loan", title2)
        sheet.write(2, 50, "Company Loan", title2)

        sheet.write(2, 51, "Adjustment", title2)
        sheet.write(2, 52, "Loan Adjustment", title2)
        sheet.write(2, 53, "Withholding Tax Adjustment", title2)

        sheet.write(2, 54, "Advances", title2)

        sheet.write(2, 55, "Net Salary", bg_net_pay_title)

        domain = []
        if status:
            domain.append(('state', '=', status))
        if date_from:
            domain.append(('date_from', '>=', date_from))
        if date_to:
            domain.append(('date_to', '<=', date_to))

        if company_id:
            domain.append(('company_id', '=', company_id))

        payslips = self.env['hr.payslip'].search(domain)

        payslip_ids = []
        for payslip in payslips:
            if bank_account:
                if not payslip.employee_id.bank_account_id.acc_number:
                    continue
                if bank_account != payslip.employee_id.bank_account_id.acc_number.upper():
                    continue
            payslip_ids.append(payslip.id)

        payslips = self.env['hr.payslip'].browse(payslip_ids)

        date_from_string = datetime.strptime(
            date_from, '%Y-%m-%d').strftime('%B %d')
        date_to_string = datetime.strptime(
            date_to, '%Y-%m-%d').strftime('%B %d %Y')

        range_date = date_from_string + " - " + date_to_string

        sheet.merge_range('C1:Z1', range_date, format1)

        n = 3
        d = 1
        for i, ps in enumerate(payslips):
            row = i + 1
            row = n
            lines = ps.line_ids
            work_lines = ps.worked_days_line_ids
            department = ps.sudo().employee_id.department_id and ps.sudo(
            ).employee_id.department_id.name or False
            sheet.set_row(row, 55)
            sheet.write(row, 0, d)
            sheet.write(row, 1, ps.employee_id.name, format1)
            sheet.write(row, 2, ps.employee_id.bank_account_id.acc_number, title2)
            sheet.write(row, 3, department, title2)

            sheet.write(row, 4, sum(lines.filtered(
                lambda r: r.code == 'BASICPAY').mapped('total')), title2)
            sheet.write(row, 5, sum(lines.filtered(
                lambda r: r.code == 'OALW').mapped('total')), title2)

            sheet.write(row, 6, sum(work_lines.filtered(
                lambda r: r.code == 'OT').mapped('amount')), title2)
            sheet.write(row, 7, sum(work_lines.filtered(
                lambda r: r.code == 'RHOT').mapped('amount')), title2)
            sheet.write(row, 8, sum(work_lines.filtered(
                lambda r: r.code == 'SHOT').mapped('amount')), title2)
            sheet.write(row, 9, sum(work_lines.filtered(
                lambda r: r.code == 'RDOT').mapped('amount')), title2)
            sheet.write(row, 10, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHOT').mapped('amount')), title2)
            sheet.write(row, 11, sum(work_lines.filtered(
                lambda r: r.code == 'RDSHOT').mapped('amount')), title2)
            sheet.write(row, 12, sum(work_lines.filtered(
                lambda r: r.code == 'NSOT').mapped('amount')), title2)
            sheet.write(row, 13, sum(work_lines.filtered(
                lambda r: r.code == 'RDNSOT').mapped('amount')), title2)
            sheet.write(row, 14, sum(work_lines.filtered(
                lambda r: r.code == 'SHNSOT').mapped('amount')), title2)
            sheet.write(row, 15, sum(work_lines.filtered(
                lambda r: r.code == 'RDSHNSOT').mapped('amount')), title2)
            sheet.write(row, 16, sum(work_lines.filtered(
                lambda r: r.code == 'RHNSOT').mapped('amount')), title2)
            sheet.write(row, 17, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHNSOT').mapped('amount')), title2)
            sheet.write(row, 18, sum(work_lines.filtered(
                lambda r: r.code == 'RH').mapped('amount')), title2)
            sheet.write(row, 19, sum(work_lines.filtered(
                lambda r: r.code == 'SH').mapped('amount')), title2)
            sheet.write(row, 20, sum(work_lines.filtered(
                lambda r: r.code == 'RD').mapped('amount')), title2)
            sheet.write(row, 21, sum(work_lines.filtered(
                lambda r: r.code == 'RDRH').mapped('amount')), title2)
            sheet.write(row, 22, sum(work_lines.filtered(
                lambda r: r.code == 'RDSH').mapped('amount')), title2)
            sheet.write(row, 23, sum(work_lines.filtered(
                lambda r: r.code == 'NS').mapped('amount')), title2)
            sheet.write(row, 24, sum(work_lines.filtered(
                lambda r: r.code == 'RHNS').mapped('amount')), title2)
            sheet.write(row, 25, sum(work_lines.filtered(
                lambda r: r.code == 'SHNS').mapped('amount')), title2)
            sheet.write(row, 26, sum(work_lines.filtered(
                lambda r: r.code == 'RDNS').mapped('amount')), title2)
            sheet.write(row, 27, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHNS').mapped('amount')), title2)
            sheet.write(row, 28, sum(work_lines.filtered(
                lambda r: r.code == 'DHNS').mapped('amount')), title2)
            sheet.write(row, 29, sum(work_lines.filtered(
                lambda r: r.code == 'RDDHNS').mapped('amount')), title2)

            sheet.write(row, 30, sum(lines.filtered(
                lambda r: r.code == 'RALW').mapped('total')), bg_flesh)
            sheet.write(row, 31, sum(lines.filtered(
                lambda r: r.code == 'CALW').mapped('total')), bg_flesh)

            sheet.write(row, 32, sum(lines.filtered(
                lambda r: r.code == 'GROSS').mapped('total')), bg_gross)

            sheet.write(row, 33, sum(lines.filtered(
                lambda r: r.code == 'WT').mapped('total')))
            sheet.write(row, 34, sum(lines.filtered(
                lambda r: r.code == 'LATE').mapped('total')))
            sheet.write(row, 35, sum(lines.filtered(
                lambda r: r.code == 'UNDERTIME').mapped('total')))
            sheet.write(row, 36, sum(lines.filtered(
                lambda r: r.code == 'ABSENT').mapped('total')))
            sheet.write(row, 37, sum(lines.filtered(
                lambda r: r.category_id.code == 'DED').mapped('total')), bg_tot_deduct)

            sheet.write(row, 38, sum(lines.filtered(
                lambda r: r.code == 'SSSEE').mapped('total')))
            sheet.write(row, 39, sum(lines.filtered(
                lambda r: r.code == 'HDMFEE').mapped('total')))
            sheet.write(row, 40, sum(lines.filtered(
                lambda r: r.code == 'HDMFAEE').mapped('total')))
            sheet.write(row, 41, sum(lines.filtered(
                lambda r: r.code == 'PHILEE').mapped('total')))

            sheet.write(row, 42, sum(lines.filtered(
                lambda r: r.code == 'SSSLOAN').mapped('total')))
            sheet.write(row, 43, sum(lines.filtered(
                lambda r: r.code == 'HDMFLOAN').mapped('total')))
            sheet.write(row, 44, sum(lines.filtered(
                lambda r: r.code == 'BAYANLOAN').mapped('total')))
            sheet.write(row, 45, sum(lines.filtered(
                lambda r: r.code == 'BAYAN').mapped('total')))
            sheet.write(row, 46, sum(lines.filtered(
                lambda r: r.code == 'PC').mapped('total')))
            sheet.write(row, 47, sum(lines.filtered(
                lambda r: r.code == 'HC').mapped('total')))
            sheet.write(row, 48, sum(lines.filtered(
                lambda r: r.code == 'CALLOAN').mapped('total')))
            sheet.write(row, 49, sum(lines.filtered(
                lambda r: r.code in ['OTHERLOAN', 'OTHLOAN']).mapped('total')))
            sheet.write(row, 50, sum(lines.filtered(
                lambda r: r.code in ['COMPLOAN', 'COMPANYLOAN']).mapped('total')))

            sheet.write(row, 51, sum(lines.filtered(
                lambda r: r.code == 'ADJ').mapped('total')))
            sheet.write(row, 52, sum(lines.filtered(
                lambda r: r.code == 'LADJ').mapped('total')))
            sheet.write(row, 53, sum(lines.filtered(
                lambda r: r.code == 'WHTADJ').mapped('total')))

            sheet.write(row, 54, sum(lines.filtered(
                lambda r: r.code == 'ADV').mapped('total')))
            sheet.write(row, 55, sum(lines.filtered(
                lambda r: r.code == 'NET').mapped('total')))

            n += 1
            d += 1
