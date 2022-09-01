# -*- coding: utf-8 -*-
# from odoo import http


# class Customproject(http.Controller):
#     @http.route('/customproject/customproject', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customproject/customproject/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customproject.listing', {
#             'root': '/customproject/customproject',
#             'objects': http.request.env['customproject.customproject'].search([]),
#         })

#     @http.route('/customproject/customproject/objects/<model("customproject.customproject"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customproject.object', {
#             'object': obj
#         })
