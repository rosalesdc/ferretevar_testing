# -*- coding: utf-8 -*-
import os
import csv
import tempfile
import base64

from odoo.exceptions import UserError
from odoo import api, fields, models, _, SUPERUSER_ID


class updatePricelist(models.TransientModel):
	_name = 'import.product.pricelist'

	file_data = fields.Binary('Archivo', required=True)
	file_name = fields.Char('File Name')
	pricelist_id = fields.Many2one('product.pricelist',string='Lista de precios')

	def import_button(self):
		if not self.csv_validator(self.file_name):
			raise UserError(_("El archivo debe ser de extension .csv"))
		file_path = tempfile.gettempdir()+'/file.csv'
		
		data = self.file_data
		
		f = open(file_path,'wb')
		f.write(base64.b64decode(data))
		f.close() 
		
		archive = csv.DictReader(open(file_path))
		product_tmpl_obj = self.env['product.template']
		archive_lines = []
		for line in archive:
			archive_lines.append(line)
		
		not_code = []
		for record in self.pricelist_id:
			print('pricelist_id ',str(record))
			for line in archive_lines:
				string = ""
				
				code = str(line.get('code',""))
				price_unit = line.get('price',0.0)
				#print('code ',str(code))
				#print('price ',str(price_unit))
				for item in record.item_ids:
					print('oitem ',str(item))
					if item.product_tmpl_id.default_code == code:
						item.write({'fixed_price':price_unit})

	@api.model
	def csv_validator(self, xml_name):
		name, extension = os.path.splitext(xml_name)
		return True if extension == '.csv' else False