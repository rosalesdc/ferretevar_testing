"""
* Created by gonzalezoscar on 6/07/18
* report_expenses_portal_user
"""

# -*- coding: utf-8 -*-
import json
import base64
from odoo import http
from odoo.http import request


class RegisterExpenseControllers(http.Controller):

    @http.route('/page/report_expenses_portal_user.s4g_register_expense/', type='http', auth='user', website=True)
    def get_expense_data(self, **kw):
        user = request.env.user

        tasks_users = http.request.env['project.task'].sudo().search(
            [
                ('user_id.id', '=', user.id)
            ]
        )

        employee_obj = http.request.env['hr.employee'].sudo().search(
            [
                ('user_id.id', '=', user.id)
            ]
        )

        projects_ids = []

        for task in tasks_users:
            projects_ids.append(task.project_id.id)

        projects = http.request.env['project.project'].sudo().search(
            [
                ('id', 'in', projects_ids)
            ]
        )
        print (projects)

        products = http.request.env['product.product'].sudo().search(
            [
                ('can_be_expensed', '=', True)
            ]
        )

        return http.request.render(
            'report_expenses_portal_user.s4g_register_expense',
            {
                'projects': projects,
                'products': products,
                'user': user,
                'employee_obj': employee_obj,
            }
        )

    @http.route('/page/report_expenses_portal_user.expense_success', type='http', auth='user', website=True)
    def render_sucess_expense(self):
        return http.request.render('report_expenses_portal_user.expense_success', {})

    @http.route('/website/create_myexpense', type='http', methods=['POST', 'GET'], auth='user', website=True)
    def create_myexpense(self, **kw):
        name = kw.get('name')
        product_id = kw.get('product_id')
        unit_amount = kw.get('unit_amount')
        quantity = kw.get('quantity')
        reference = kw.get('reference')
        date = kw.get('date')
        x_project_id = kw.get('x_project_id')
        employee_id = kw.get('employee_id')

        expense_data = {
            'name': name,
            'product_id': product_id,
            'unit_amount': unit_amount,
            'quantity': quantity,
            'reference': reference,
            'date': date,
            'x_project_id': x_project_id,
            'employee_id': int(employee_id),
        }

        expense_record = http.request.env['hr.expense'].sudo().create(expense_data)

        if kw.get('Voucher', False):
            attachments = request.env['ir.attachment']
            filetoload = kw.get('Voucher')
            expense_id = expense_record.id
            name = kw.get('Voucher').filename
            attachment = filetoload.read()
            attachments.sudo().create({
                'name': "Voucher file",
                'datas_fname': name,
                'res_name': name,
                'res_model': 'hr.expense',
                'res_id': expense_id,
                'datas': base64.b64encode(attachment),
            })
        return http.request.redirect('/page/report_expenses_portal_user.expense_success')
