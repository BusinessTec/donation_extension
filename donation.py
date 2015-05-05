# -*- encoding: utf-8 -*-

from openerp import models, fields, api


class AModel(models.Model):

        _name = 'product.client.info'

        client_code=fields.Char(string='Código de cliente',size=14,store=True)
        client_ean13=fields.Char(string='EAN13 de cliente',size=14,store=True)
        client_fee=fields.Float(string='Tarifa logística',digits=(6,2),store=True)
        client_text=fields.Char(string='Texto de tarifa',size=64,store=True)
        client_producto=fields.Many2one('product.product',store=True)
        product_id=fields.Many2one('product.product',store=True,required=True)
        partner_id=fields.Many2one('res.partner',store=True,required=True)
        display_name=fields.Char(string='Name', compute='cdn')
        name=fields.Char(string='Name', compute='cn')
        @api.one
        @api.depends('product_id.name')
        def cdn(self):
            self.display_name=self.product_id.name
        @api.one
        @api.depends('product_id.name')
        def cn(self):
            self.name=self.product_id.name
