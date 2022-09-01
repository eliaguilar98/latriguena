# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta, date


class customproject(models.Model):
#     _name = 'customproject.customproject'
#     _description = 'customproject.customproject'
      _inherit = 'project.task.recurrence'
      next_recurrence_date = fields.Datetime()

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
