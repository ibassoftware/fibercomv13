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
        bank_account = data['form']['bank_account'] and data['form']['bank_account'].upper()
        struct_id = data['form']['struct_id']

        format1 = workbook.add_format(
            {'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9', 'text_wrap': True})

        format2 = workbook.add_format(
            {'align': 'centre_across', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9', 'text_wrap': True})

        format3 = workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': '#D9D9D9'})

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
        sheet.set_column('C:BE', 12)
        sheet.set_column('BG:BG', 10)
        sheet.set_column('BI:BI', 10)
        sheet.set_column('BK:BO', 10)
        sheet.set_column('BR:BS', 10)
        sheet.set_column('BY:CB', 10)

        sheet.set_row(2, 80)
        sheet.write(0, 1, "PAYROLL PERIOD:", format1)

        sheet.write(1, 4, "Rate", format1)
        sheet.merge_range('D2:F2', 'Basic', format1)
        sheet.merge_range('G2:BB2', 'Premiums', format1)
        sheet.merge_range('BC2:BE2', 'Allowance', format1)
        sheet.merge_range('BG2:BK2', 'Deductions', format1)
        sheet.merge_range('BL2:BO2', 'Employee Contributions', format1)
        sheet.merge_range('BP2:BX2', 'Loans', format1)
        sheet.merge_range('BY2:CA2', 'Adjustments', format1)

        sheet.write(3, 0, "")
        sheet.merge_range('B3:B4', 'Name', format1)
        sheet.merge_range('C3:C4', 'Department', format1)

        sheet.merge_range('D3:E3', 'Basic Pay', format1)
        sheet.write(3, 3, "Worked Days", format2)
        sheet.write(3, 4, "Computation", format3)
        sheet.merge_range('F3:F4', 'Other Allowance', format1)

        sheet.merge_range('G3:H3', 'Regular Overtime', format1)
        sheet.write(3, 6, "Worked Days", format2)
        sheet.write(3, 7, "Computation", format3)

        sheet.merge_range('I3:J3', 'Regular Holiday Overtime', format1)
        sheet.write(3, 8, "Worked Days", format2)
        sheet.write(3, 9, "Computation", format3)

        sheet.merge_range('K3:L3', 'Special Holiday Overtime', format1)
        sheet.write(3, 10, "Worked Days", format2)
        sheet.write(3, 11, "Computation", format3)

        sheet.merge_range('M3:N3', 'Rest Day Overtime', format1)
        sheet.write(3, 12, "Worked Days", format2)
        sheet.write(3, 13, "Computation", format3)

        sheet.merge_range('O3:P3', 'Rest Day Regular Holiday Overtime', format1)
        sheet.write(3, 14, "Worked Days", format2)
        sheet.write(3, 15, "Computation", format3)

        sheet.merge_range('Q3:R3', 'Rest Day Special Holiday Overtime', format1)
        sheet.write(3, 16, "Worked Days", format2)
        sheet.write(3, 17, "Computation", format3)

        sheet.merge_range('S3:T3', 'Night Shift Overtime', format1)
        sheet.write(3, 18, "Worked Days", format2)
        sheet.write(3, 19, "Computation", format3)

        sheet.merge_range('U3:V3', 'Rest Day Night Shift Overtime', format1)
        sheet.write(3, 20, "Worked Days", format2)
        sheet.write(3, 21, "Computation", format3)

        sheet.merge_range('W3:X3', 'Special Holiday Night Shift Overtime', format1)
        sheet.write(3, 22, "Worked Days", format2)
        sheet.write(3, 23, "Computation", format3)

        sheet.merge_range('Y3:Z3', 'Rest Day Special Holiday Night Shift Overtime', format1)
        sheet.write(3, 24, "Worked Days", format2)
        sheet.write(3, 25, "Computation", format3)

        sheet.merge_range('AA3:AB3', 'Regular Holiday Night Shift Overtime', format1)
        sheet.write(3, 26, "Worked Days", format2)
        sheet.write(3, 27, "Computation", format3)

        sheet.merge_range('AC3:AD3', 'Rest Day Regular Holiday Night Shift Overtime', format1)
        sheet.write(3, 28, "Worked Days", format2)
        sheet.write(3, 29, "Computation", format3)

        sheet.merge_range('AE3:AF3', 'Regular Holiday', format1)
        sheet.write(3, 30, "Worked Days", format2)
        sheet.write(3, 31, "Computation", format3)

        sheet.merge_range('AG3:AH3', 'Special Holiday', format1)
        sheet.write(3, 32, "Worked Days", format2)
        sheet.write(3, 33, "Computation", format3)

        sheet.merge_range('AI3:AJ3', 'Rest Day', format1)
        sheet.write(3, 34, "Worked Days", format2)
        sheet.write(3, 35, "Computation", format3)

        sheet.merge_range('AK3:AL3', 'Rest Day Regular Holiday', format1)
        sheet.write(3, 36, "Worked Days", format2)
        sheet.write(3, 37, "Computation", format3)

        sheet.merge_range('AM3:AN3', 'Rest Day Special Holiday', format1)
        sheet.write(3, 38, "Worked Days", format2)
        sheet.write(3, 39, "Computation", format3)

        sheet.merge_range('AO3:AP3', 'Night Differential', format1)
        sheet.write(3, 40, "Worked Days", format2)
        sheet.write(3, 41, "Computation", format3)

        sheet.merge_range('AQ3:AR3', 'Regular Holiday Night Shift', format1)
        sheet.write(3, 42, "Worked Days", format2)
        sheet.write(3, 43, "Computation", format3)

        sheet.merge_range('AS3:AT3', 'Special Holiday Night Shift', format1)
        sheet.write(3, 44, "Worked Days", format2)
        sheet.write(3, 45, "Computation", format3)

        sheet.merge_range('AU3:AV3', 'Rest Day Night Differential', format1)
        sheet.write(3, 46, "Worked Days", format2)
        sheet.write(3, 47, "Computation", format3)

        sheet.merge_range('AW3:AX3', 'Rest Day Regular Holiday Night Shift', format1)
        sheet.write(3, 48, "Worked Days", format2)
        sheet.write(3, 49, "Computation", format3)

        sheet.merge_range('AY3:AZ3', 'Double Holiday Night Shift', format1)
        sheet.write(3, 50, "Worked Days", format2)
        sheet.write(3, 51, "Computation", format3)

        sheet.merge_range('BA3:BB3', 'Rest Day Double Holiday Night Shift', format1)
        sheet.write(3, 52, "Worked Days", format2)
        sheet.write(3, 53, "Computation", format3)

        sheet.merge_range('BC3:BC4', "Rice Allowance", title2)
        sheet.merge_range('BD3:BD4', "Clothing Allowance", title2)
        sheet.merge_range('BE3:BE4', "Additional Allowance", title2)

        sheet.merge_range('BF3:BF4', "Gross Pay", bg_gross_title)

        sheet.merge_range('BG3:BG4', "Withholding Tax", title2)
        sheet.merge_range('BH3:BH4', "Lates", title2)
        sheet.merge_range('BI3:BI4', "Undertime", title2)
        sheet.merge_range('BJ3:BJ4', "Absent", title2)
        sheet.merge_range('BK3:BK4', "Total Deductions", bg_tot_deduct_title)

        sheet.merge_range('BL3:BL4', "SSS Employee Share", title2)
        sheet.merge_range('BM3:BM4', "HDMF Employee Share", title2)
        sheet.merge_range('BN3:BN4', "Additional HDMF Employee Share", title2)
        sheet.merge_range('BO3:BO4', "Philhealth Employee Share", title2)

        sheet.merge_range('BP3:BP4',  "SSS Loan", title2)
        sheet.merge_range('BQ3:BQ4', "HDMF Loan", title2)
        sheet.merge_range('BR3:BR4', "Bayanihan Loan", title2)
        sheet.merge_range('BS3:BS4', "Bayanihan", title2)
        sheet.merge_range('BT3:BT4', "Personal Charges", title2)
        sheet.merge_range('BU3:BU4', "Health Card", title2)
        sheet.merge_range('BV3:BV4', "Calamity Loan", title2)
        sheet.merge_range('BW3:BW4', "Other Loan", title2)
        sheet.merge_range('BX3:BX4', "Company Loan", title2)

        sheet.merge_range('BY3:BY4', "Adjustment", title2)
        sheet.merge_range('BZ3:BZ4', "Loan Adjustment", title2)
        sheet.merge_range('CA3:CA4', "Withholding Tax Adjustment", title2)

        sheet.merge_range('CB3:CB4', "Advances", title2)

        sheet.merge_range('CC3:CC4', "Net Salary", bg_net_pay_title)

        domain = []
        if status:
            domain.append(('state', '=', status))
        if date_from:
            domain.append(('date_from', '>=', date_from))
        if date_to:
            domain.append(('date_to', '<=', date_to))
        if struct_id:
            domain.append(('struct_id', '=', struct_id))
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

        sheet.merge_range('C1:CC1', range_date, format1)

        def render_rows(row, sheet, lines, work_lines, cell_format={}):
            sheet.write(row, 3, sum(work_lines.filtered(
                lambda r: r.code == 'BASICPAY').mapped('number_of_days')), cell_format or bg_flesh)
            sheet.write(row, 4, sum(lines.filtered(
                lambda r: r.code == 'BASICPAY').mapped('total')), cell_format or bg_flesh)
            sheet.write(row, 5, sum(lines.filtered(
                lambda r: r.code == 'OALW').mapped('total')), cell_format)

            sheet.write(row, 6, sum(work_lines.filtered(
                lambda r: r.code == 'OT').mapped('number_of_days')), cell_format)
            sheet.write(row, 7, sum(work_lines.filtered(
                lambda r: r.code == 'OT').mapped('amount')), cell_format)
            sheet.write(row, 8, sum(work_lines.filtered(
                lambda r: r.code == 'RHOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 9, sum(work_lines.filtered(
                lambda r: r.code == 'RHOT').mapped('amount')), cell_format)
            sheet.write(row, 10, sum(work_lines.filtered(
                lambda r: r.code == 'SHOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 11, sum(work_lines.filtered(
                lambda r: r.code == 'SHOT').mapped('amount')), cell_format)
            sheet.write(row, 12, sum(work_lines.filtered(
                lambda r: r.code == 'RDOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 13, sum(work_lines.filtered(
                lambda r: r.code == 'RDOT').mapped('amount')), cell_format)
            sheet.write(row, 14, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 15, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHOT').mapped('amount')), cell_format)
            sheet.write(row, 16, sum(work_lines.filtered(
                lambda r: r.code == 'RDSHOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 17, sum(work_lines.filtered(
                lambda r: r.code == 'RDSHOT').mapped('amount')), cell_format)
            sheet.write(row, 18, sum(work_lines.filtered(
                lambda r: r.code == 'NSOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 19, sum(work_lines.filtered(
                lambda r: r.code == 'NSOT').mapped('amount')), cell_format)
            sheet.write(row, 20, sum(work_lines.filtered(
                lambda r: r.code == 'RDNSOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 21, sum(work_lines.filtered(
                lambda r: r.code == 'RDNSOT').mapped('amount')), cell_format)
            sheet.write(row, 22, sum(work_lines.filtered(
                lambda r: r.code == 'SHNSOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 23, sum(work_lines.filtered(
                lambda r: r.code == 'SHNSOT').mapped('amount')), cell_format)
            sheet.write(row, 24, sum(work_lines.filtered(
                lambda r: r.code == 'RDSHNSOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 25, sum(work_lines.filtered(
                lambda r: r.code == 'RDSHNSOT').mapped('amount')), cell_format)
            sheet.write(row, 26, sum(work_lines.filtered(
                lambda r: r.code == 'RHNSOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 27, sum(work_lines.filtered(
                lambda r: r.code == 'RHNSOT').mapped('amount')), cell_format)
            sheet.write(row, 28, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHNSOT').mapped('number_of_days')), cell_format)
            sheet.write(row, 29, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHNSOT').mapped('amount')), cell_format)
            sheet.write(row, 30, sum(work_lines.filtered(
                lambda r: r.code == 'RH').mapped('number_of_days')), cell_format)
            sheet.write(row, 31, sum(work_lines.filtered(
                lambda r: r.code == 'RH').mapped('amount')), cell_format)
            sheet.write(row, 32, sum(work_lines.filtered(
                lambda r: r.code == 'SH').mapped('number_of_days')), cell_format)
            sheet.write(row, 33, sum(work_lines.filtered(
                lambda r: r.code == 'SH').mapped('amount')), cell_format)
            sheet.write(row, 34, sum(work_lines.filtered(
                lambda r: r.code == 'RD').mapped('number_of_days')), cell_format)
            sheet.write(row, 35, sum(work_lines.filtered(
                lambda r: r.code == 'RD').mapped('amount')), cell_format)
            sheet.write(row, 36, sum(work_lines.filtered(
                lambda r: r.code == 'RDRH').mapped('number_of_days')), cell_format)
            sheet.write(row, 37, sum(work_lines.filtered(
                lambda r: r.code == 'RDRH').mapped('amount')), cell_format)
            sheet.write(row, 38, sum(work_lines.filtered(
                lambda r: r.code == 'RDSH').mapped('number_of_days')), cell_format)
            sheet.write(row, 39, sum(work_lines.filtered(
                lambda r: r.code == 'RDSH').mapped('amount')), cell_format)
            sheet.write(row, 40, sum(work_lines.filtered(
                lambda r: r.code == 'NS').mapped('number_of_days')), cell_format)
            sheet.write(row, 41, sum(work_lines.filtered(
                lambda r: r.code == 'NS').mapped('amount')), cell_format)
            sheet.write(row, 42, sum(work_lines.filtered(
                lambda r: r.code == 'RHNS').mapped('number_of_days')), cell_format)
            sheet.write(row, 43, sum(work_lines.filtered(
                lambda r: r.code == 'RHNS').mapped('amount')), cell_format)
            sheet.write(row, 44, sum(work_lines.filtered(
                lambda r: r.code == 'SHNS').mapped('number_of_days')), cell_format)
            sheet.write(row, 45, sum(work_lines.filtered(
                lambda r: r.code == 'SHNS').mapped('amount')), cell_format)
            sheet.write(row, 46, sum(work_lines.filtered(
                lambda r: r.code == 'RDNS').mapped('number_of_days')), cell_format)
            sheet.write(row, 47, sum(work_lines.filtered(
                lambda r: r.code == 'RDNS').mapped('amount')))
            sheet.write(row, 48, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHNS').mapped('number_of_days')))
            sheet.write(row, 49, sum(work_lines.filtered(
                lambda r: r.code == 'RDRHNS').mapped('amount')))
            sheet.write(row, 50, sum(work_lines.filtered(
                lambda r: r.code == 'DHNS').mapped('number_of_days')))
            sheet.write(row, 51, sum(work_lines.filtered(
                lambda r: r.code == 'DHNS').mapped('amount')))
            sheet.write(row, 52, sum(work_lines.filtered(
                lambda r: r.code == 'RDDHNS').mapped('number_of_days')))
            sheet.write(row, 53, sum(work_lines.filtered(
                lambda r: r.code == 'RDDHNS').mapped('amount')), cell_format)

            sheet.write(row, 54, sum(lines.filtered(
                lambda r: r.code == 'RALW').mapped('total')), cell_format)
            sheet.write(row, 55, sum(lines.filtered(
                lambda r: r.code == 'CALW').mapped('total')), cell_format)
            sheet.write(row, 56, sum(lines.filtered(
                lambda r: r.code == 'ADDALLOWANCE').mapped('total')), cell_format)

            sheet.write(row, 57, sum(lines.filtered(
                lambda r: r.code == 'GROSS').mapped('total')), cell_format or bg_gross)

            sheet.write(row, 58, sum(lines.filtered(
                lambda r: r.code == 'WT').mapped('total')), cell_format)
            sheet.write(row, 59, sum(lines.filtered(
                lambda r: r.code == 'LATE').mapped('total')), cell_format)
            sheet.write(row, 60, sum(lines.filtered(
                lambda r: r.code == 'UNDERTIME').mapped('total')), cell_format)
            sheet.write(row, 61, sum(lines.filtered(
                lambda r: r.code == 'ABSENT').mapped('total')), cell_format)
            sheet.write(row, 62, sum(lines.filtered(
                lambda r: r.category_id.code == 'DED').mapped('total')), cell_format or bg_tot_deduct)

            sheet.write(row, 63, sum(lines.filtered(
                lambda r: r.code == 'SSSEE').mapped('total')), cell_format)
            sheet.write(row, 64, sum(lines.filtered(
                lambda r: r.code == 'HDMFEE').mapped('total')), cell_format)
            sheet.write(row, 65, sum(lines.filtered(
                lambda r: r.code == 'HDMFAEE').mapped('total')), cell_format)
            sheet.write(row, 66, sum(lines.filtered(
                lambda r: r.code == 'PHILEE').mapped('total')), cell_format)

            sheet.write(row, 67, sum(lines.filtered(
                lambda r: r.code == 'SSSLOAN').mapped('total')), cell_format)
            sheet.write(row, 68, sum(lines.filtered(
                lambda r: r.code == 'HDMFLOAN').mapped('total')), cell_format)
            sheet.write(row, 69, sum(lines.filtered(
                lambda r: r.code == 'BAYANLOAN').mapped('total')), cell_format)
            sheet.write(row, 70, sum(lines.filtered(
                lambda r: r.code == 'BAYAN').mapped('total')), cell_format)
            sheet.write(row, 71, sum(lines.filtered(
                lambda r: r.code == 'PC').mapped('total')), cell_format)
            sheet.write(row, 72, sum(lines.filtered(
                lambda r: r.code == 'HC').mapped('total')), cell_format)
            sheet.write(row, 73, sum(lines.filtered(
                lambda r: r.code == 'CALLOAN').mapped('total')), cell_format)
            sheet.write(row, 74, sum(lines.filtered(
                lambda r: r.code in ['OTHERLOAN', 'OTHLOAN']).mapped('total')), cell_format)
            sheet.write(row, 75, sum(lines.filtered(
                lambda r: r.code in ['COMPLOAN', 'COMPANYLOAN']).mapped('total')), cell_format)

            sheet.write(row, 76, sum(lines.filtered(
                lambda r: r.code == 'ADJ').mapped('total')), cell_format)
            sheet.write(row, 77, sum(lines.filtered(
                lambda r: r.code == 'LADJ').mapped('total')), cell_format)
            sheet.write(row, 78, sum(lines.filtered(
                lambda r: r.code == 'WHTADJ').mapped('total')), cell_format)

            sheet.write(row, 79, sum(lines.filtered(
                lambda r: r.code == 'ADV').mapped('total')), cell_format)
            sheet.write(row, 80, sum(lines.filtered(
                lambda r: r.code == 'NET').mapped('total')), cell_format or bg_net_pay)

        n = 4
        d = 1
        for i, ps in enumerate(payslips):
            row = n
            lines = ps.line_ids
            work_lines = ps.worked_days_line_ids
            department = ps.sudo().employee_id.department_id and ps.sudo(
            ).employee_id.department_id.name or False
            sheet.set_row(row, 55)
            sheet.write(row, 0, d)
            sheet.write(row, 1, ps.employee_id.name, format1)
            sheet.write(row, 2, department, title2)
            render_rows(row, sheet, lines, work_lines)
            n += 1
            d += 1
        sheet.write(n, 1, 'Total', format1)
        render_rows(n, sheet, payslips.line_ids, payslip.worked_days_line_ids, format1)
