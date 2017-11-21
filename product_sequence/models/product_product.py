# -*- coding: utf-8 -*-
# Non part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = ['product.template']
    default_code = fields.Char('Sequence')

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].get('product.number') or '/'
        if not vals['default_code']:
        	vals['default_code'] = seq
        return super(ProductProduct, self).create(vals)