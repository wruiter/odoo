# -*- coding: utf-8 -*-
# Non part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import UserError

class Picking(models.TransientModel):
    _name = "stock.picking.bulk"
    _description = "move selected stock"
    name = fields.Char(required=False, translate=True)
    location_dest_id = fields.Many2one(
        'stock.location', 'Destination Location', index=True, ondelete='cascade', required=True,
         help="The new location where the goods need to go")
    	
    @api.multi
    def move_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        Quants = self.env['stock.quant']
        for record in Quants.browse(active_ids):
            vals = {'picking_type_id':5, 'location_id':record.location_id.id, 'name':'Bulk Move', 'product_uom':record.product_uom_id.id, 'location_dest_id':self.location_dest_id.id, 'product_id':record.product_id.id, 'product_uom_qty':record.qty}
            move = self.env['stock.move'].sudo().create(vals)
            move.assign_picking()
            move.action_confirm()        	       	
        return {'type': 'ir.actions.act_window_close'}   	
