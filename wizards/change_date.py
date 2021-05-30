# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ChangeDateWizard(models.TransientModel):
    _name = 'rewan2.change.date.wizard'
    _description = 'Description'

    # date = fields.Datetime(string="Date to change")
   
    def action_change_date(self):
        self.ensure_one()
        active_id=self.env['rewan2.order'].browse(self._context.get('active_id')).copy()
        # active_id.write({'date' : self.date})
       
