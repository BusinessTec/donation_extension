#-*- coding:utf-8 -*-
from openerp import fields, models, api
from openerp.exceptions import except_orm, Warning, RedirectWarning

class sale_order(models.Model):
    _inherit = "sale.order"
    @api.one
    def button_fee(self):
        k=0
        l = self.partner_id.name
        for lin in self.order_line:
            p=lin.product_id
            for c in lin.product_id.client_code_ids:
                if c.product_id==p and self.partner_id==c.partner_id:
                    lines=self.pool.get('sale.order.line')
                    z1 = round(lin.price_subtotal*c.client_fee/100,2)*(-1)
                    vals = {
                        'order_id': self.id,
                        'name': c.client_text,
                        'product_uom_qty': 1,
                        'product_uos_qty': 1,
                        'product_uom': c.client_producto.product_tmpl_id.uom_id.id,
                        'product_uos': c.client_producto.product_tmpl_id.uom_id.id,
                        'product_id': c.client_producto.id,
                        'price_unit': z1,
                        'tax_id': lin.tax_id,
                        'state': 'draft'
                    }
                    res = self.env['sale.order.line'].create(vals)
                    self.order_line=self.order_line

