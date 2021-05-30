# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BasicModel2(models.Model):
    _name = 'rewan2.basic.model2'
    _description = 'Description'

    name = fields.Char()
    unit_price = fields.Integer()
    qty = fields.Integer()
    sub_total= fields.Integer(compute="compute_value", store=True)
    model1=fields.Many2one('rewan2.basic.model1','Model1')
    order =fields.Many2one('rewan2.order','Order')


    @api.depends('unit_price')
    def compute_value(self):
        for record in self:
            record.sub_total = record.unit_price * 10
