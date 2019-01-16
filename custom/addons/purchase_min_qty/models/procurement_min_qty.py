# -*- coding: utf-8 -*-

from odoo import fields, models, api

class procurementMinQty(models.Model):
	_inherit = 'procurement.group'

	@api.model
	def run(self, product_id, product_qty, product_uom, location_id, name, origin, values):
		values.setdefault('company_id', self.env['res.company']._company_default_get('procurement.group'))
		values.setdefault('priority', '1')
		values.setdefault('date_planned', fields.Datetime.now())
		rule = self._get_rule(product_id, location_id, values)

		if not rule:
			raise UserError(_('No procurement rule found. Please verify the configuration of your routes'))

		if location_id.name == 'Clientes':
			getattr(rule, '_run_%s' % rule.action)(product_id, product_qty, product_uom, location_id, name, origin, values)
		else:
			seller = product_id.seller_ids[0]
			qty_min = seller.min_qty
			if product_qty > qty_min:
				quantity = product_qty % qty_min
				if quantity > 0:
					print('MOD QUANTITY',quantity)
					quantity = (product_qty-quantity)+qty_min
					print('FULL QUANTITY',quantity)
				else:
					quantity = product_qty / qty_min
					quantity = (quantity*qty_min)
			else:
				quantity = qty_min			
			getattr(rule, '_run_%s' % rule.action)(product_id, quantity, product_uom, location_id, name, origin, values)
		return True
