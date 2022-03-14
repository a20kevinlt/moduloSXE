# -*- coding: utf-8 -*-
# from odoo import http


# class MisNotas(http.Controller):
#      @http.route('/mis_notas/mis_notas/', auth='public')
#      def index(self, **kw):
#          return "Hello, world"

#      @http.route('/mis_notas/mis_notas/objects/', auth='public')
#      def list(self, **kw):
#          return http.request.render('mis_notas.listing', {
#              'root': '/mis_notas/mis_notas',
#              'objects': http.request.env['mis_notas.mis_notas'].search([]),
#          })

#      @http.route('/mis_notas/mis_notas/objects/<model("mis_notas.mis_notas"):obj>/', auth='public')
#      def object(self, obj, **kw):
#          return http.request.render('mis_notas.object', {
#              'object': obj
#          })
