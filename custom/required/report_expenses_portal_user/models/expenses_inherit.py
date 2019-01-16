"""
* Created by gonzalezoscar on 6/07/18
* report_expenses_portal_user
"""

# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ExpensesInheritedFrontend(models.Model):
    _inherit = 'hr.expense'
    _name = 'hr.expense'
    _description = "Expenses register"

    x_project_id = fields.Many2one(
        'project.project',
        string="Project"
    )