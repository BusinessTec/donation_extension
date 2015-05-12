# -*- encoding: utf-8 -*-

from openerp import models, fields, api

class donation_extra(models.Model):

        _inherit = 'donation.donation'
        
        notes = fields.Text(string='Notes','Additional Information')
        donation_number = fields.Char(string='Invoice Number', readonly=True, default=False, copy=False, compute="_new_number")
        
        @api.one
	@api.depends('id')
	def _new_number(self):
	        if self.state=='done':
	                self.donation_number=context_today(self)[:4]+'/'+{:04}".format(self.id)
	
