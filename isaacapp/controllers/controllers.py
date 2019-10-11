# -*- coding: utf-8 -*-
from odoo import http

# class Isaacapp(http.Controller):
#     @http.route('/isaacapp/isaacapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isaacapp/isaacapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('isaacapp.listing', {
#             'root': '/isaacapp/isaacapp',
#             'objects': http.request.env['isaacapp.isaacapp'].search([]),
#         })

#     @http.route('/isaacapp/isaacapp/objects/<model("isaacapp.isaacapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isaacapp.object', {
#             'object': obj
#         })