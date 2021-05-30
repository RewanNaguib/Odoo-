# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rewan2(models.Model):
    _name = 'rewan2.basic.model1'
    _description = 'rewan2.rewan2'

    name = fields.Char()
    price = fields.Integer()
    # value2 = fields.Float(compute="compute_value", store=True)
    description = fields.Text()
    manufactrer = fields.Char()
    timestamp = fields.Datetime()
    model_2=fields.One2many('rewan2.basic.model2','model1')


    # @api.onchange('value')
    # def compute_value(self):
       
    #     for record in self:
    #         record.value2 = record.value / 10.0
