# -*- coding: utf-8 -*-
import base64
import io
import logging
from PIL import Image, ImageFont, ImageDraw
from odoo import http, tools
from odoo.http import request

logger = logging.getLogger(__name__)


class ImportProductImages(http.Controller):

    @http.route('/page/import_product_images.import_product_images', type='http', auth='user', website=True)
    def render_website_template(self):
        is_manager = False
        user = request.env.user
        inventory_manager_group = http.request.env.ref('stock.group_stock_manager')
        if user.id in inventory_manager_group.users.ids:
            is_manager = True
            print ("Usuario admin de inventario")
        return http.request.render('import_product_images.import_product_images',
                                   {'is_manager': is_manager}
                                   )

    @http.route('/page/import_product_images.images_success', type='http', auth='user', website=True)
    def render_images_success(self):
        return http.request.render('import_product_images.images_success', {})

    @http.route('/page/import_product_images.images_failed', type='http', auth='user', website=True)
    def render_images_failed(self):
        return http.request.render('import_product_images.images_failed', {})

    @http.route('/website/import_images', type='http', auth='user', website=True, methods=['POST'])
    def import_product_images(self, product_images=None, disable_optimization=None, **kwargs):
        if not product_images:
            print ("There're no images to load")
        else:
            try:
                user = http.request.env.user
                language = user.lang
                total_images = 0
                images_per_product = 0
                for c_file in request.httprequest.files.getlist('product_images'):
                    total_images += 1
                    image_data = c_file.read()

                    # Search product by defined code
                    default_code = c_file.filename.split(".")
                    file_name_product = default_code[0].strip()
                    imageslogs = http.request.env['images_log.log']
                    if 'es' in language:
                        msj_des = "Archivo cargado desde el sitio web"
                    else:
                        msj_des = "File loaded only to the frontend"

                    log_id = imageslogs.sudo().create(
                        {
                            'name': c_file.filename,
                            'description': msj_des
                        }
                    )

                    product_obj = http.request.env['product.template'].sudo().search(
                        [
                            ('images_code', '=', file_name_product)
                        ]
                    )

                    print ("\n ID del log")
                    print (log_id)

                    if product_obj:
                        images_per_product += 1
                        existinglogs = imageslogs.sudo().search(
                            [
                                ('name', '=', c_file.filename)
                            ]
                        )

                        if existinglogs[0]:
                            if 'es' in language:
                                mymsj = ", - Imagen mediana actualizada"
                            else:
                                mymsj = ", - Medium image updated"

                            log_id.sudo().write(
                                {
                                    'product_id': product_obj[0].id,
                                    'success_load': True,
                                    'description': existinglogs[0].description + 
                                    str(mymsj)
                                }
                            )

                        else:
                            if 'es' in language:
                                mymsj = "La imagen mediana fue asignada al producto"
                            else:
                                mymsj = "Medium image was set for the product"
                            log_id.sudo().write(
                                {
                                    'product_id': product_obj.id,
                                    'success_load': True,
                                    'description': mymsj
                                }
                            )
                        processed_image = base64.b64encode(image_data)
                        product_obj.sudo().write(
                            {
                                'image_medium': processed_image
                            }
                        )
                    else:
                        if 'es' in language:
                            mymsj2 = "Esta imagen no fue cargada debido a que no " \
                                     "concuerda con el nombre de algun producto "
                        else:
                            mymsj2 = "This image wasnt loaded, doesnt exist a product with that name"

                        log_id.sudo().write(
                            {
                                'success_load': False,
                                'description': mymsj2
                            }
                        )
                if images_per_product > 0:
                    print ("\n Total images to load")
                    print (total_images)
                    print ("\n Images Loaded")
                    print (images_per_product)
                    return http.request.redirect('/page/import_product_images.images_success')
                else:
                    return http.request.redirect('/page/import_product_images.images_failed')
            except Exception as e:
                logger.exception("Failed to upload images")
