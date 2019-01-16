# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ImagesLoadLog(models.Model):
    _name = 'images_log.log'

    name = fields.Char(
        string="File name"
    )

    product_id = fields.Many2one(
        'product.template',
        string="Product found",
    )

    description = fields.Text(
        string="Description",
    )

    success_load = fields.Boolean(
        string="Success Load"
    )

