# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Nutrition(models.Model):
    _name = 'nutrition'
    _rec_name = 'customer_id'
    _description = ""

    no = fields.Char(
        string='No',
        default='New',
        index=True,
        readonly=1,
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
    )
    nutrition_ids = fields.Many2many(
        'ingredient',
    )
    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Datetime.now,
    )

    @api.model
    def create(self, vals):
        no = self.env['ir.sequence'].next_by_code('nutrition')
        vals.update({
            'no': no
        })
        result = super(Nutrition, self).create(vals)
        return result

