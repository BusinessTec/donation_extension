# -*- encoding: utf-8 -*-

from openerp import models, fields


class product(models.Model):

        _inherit = 'product.product'

        client_code_ids=fields.One2many('product.client.info','product_id',store=True)
