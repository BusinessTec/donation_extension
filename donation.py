# -*- encoding: utf-8 -*-

from openerp import models, fields, api


class donation_extra(models.Model):

        _inherit = 'donation.donation'
        
        notes = fields.Text(string='Notes','Additional Information')
        internal_number = fields.Char(string='Invoice Number', readonly=True, default=False, copy=False, )
