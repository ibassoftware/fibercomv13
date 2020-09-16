# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _


class Loan(models.Model):
    _name = "hr.contract.type"
    _description = 'Employee Contract Type'

    name = fields.Char(string="Contract Type")
