# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    _name = 'report.sale.wizard'
    _description = 'Wizard: Quick Sale Orders for SalePersons'
    
    user_id = fields.Many2one(comodel_name='sale.report',
                             string='Saleperson',
                             required=True)
    date_creation = fields.Date(string='Creation Date')
    
    
    # def action_print_report(self):
        