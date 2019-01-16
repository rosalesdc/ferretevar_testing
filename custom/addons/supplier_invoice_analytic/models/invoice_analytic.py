# -*- coding: utf-8 -*-

from odoo import fields, models, api


class invoiceAnalytic(models.Model):
	_inherit = 'account.invoice'

	x_cuenta_analitica_id = fields.Many2one('account.analytic.account',string='Cuenta Analitica',compute="get_cuenta_analitica")

	@api.multi
	def get_cuenta_analitica(self):
		#parent_model = self.env.context.get('active_model')
		#print('MODEL',parent_model)
		parent_id = self.env.context.get('default_purchase_id')
		print('CTIVE',parent_id)
		model_record = self.env['purchase.order'].browse(parent_id)
		print('REC	',model_record)
		print('purchase analytic ',model_record.x_cuenta_analitica_id.id)
		self.x_cuenta_analitica_id = model_record.x_cuenta_analitica_id.id
		for record in self.invoice_line_ids:
			record.sudo().write({'account_analytic_id':model_record.x_cuenta_analitica_id.id})
