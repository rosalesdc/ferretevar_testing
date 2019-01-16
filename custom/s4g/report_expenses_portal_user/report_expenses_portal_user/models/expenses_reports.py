"""
* Created by gonzalezoscar on 23/07/18
* report_expenses_portal_user
"""

# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ExpensesReports(models.Model):
    _name = 'ops4g_expenses.reports'

    name = fields.Char(
        string="Name",
        index=True,
        required=True,
    )
