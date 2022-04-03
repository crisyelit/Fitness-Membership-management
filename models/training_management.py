# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, Command

class TrainingManagement(models.Model):
    _name = "training.management"
    _description = "This module allow you to Training Management System."
    _inherit = []

        name = fields.Char(required=True, tracking=True, default="New")
        code = fields.Char(string="Reference", required=True, tracking=True, index=True, copy=False)
        stage_id = fields.Many2one(
        'sale.subscription.stage', string='Stage', index=True, default=lambda s: s._get_default_stage_id(),
        copy=False, group_expand='_read_group_stage_ids', tracking=True)
        partner_id = fields.Many2one('res.partner', string='Customer', required=True, auto_join=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
        partner_invoice_id = fields.Many2one(
            'res.partner', string='Invoice Address',
            domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
        date_start = fields.Date(string='Start Date', default=fields.Date.today)
        date = fields.Date(string='End Date', tracking=True, help="If set in advance, the subscription will be set to renew 1 month before the date and will be closed on the date set in this field.")
