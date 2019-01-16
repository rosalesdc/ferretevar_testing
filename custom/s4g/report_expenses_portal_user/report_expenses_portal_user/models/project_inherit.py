# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectInherit(models.Model):
    _inherit = 'project.project'

    x_expense_ids = fields.One2many(
        'hr.expense',
        'x_project_id',
        string="Expenses"
    )