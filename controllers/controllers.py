# -*- coding: utf-8 -*-
from odoo import http


class Rewan2(http.Controller):
    @http.route('/rewan2/rewan2/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/rewan2/rewan2/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('rewan2.listing', {
            'root': '/rewan2/rewan2',
            'objects': http.request.env['rewan2.rewan2'].search([]),
        })

    @http.route('/rewan2/rewan2/objects/<model("rewan2.rewan2"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('rewan2.object', {
            'object': obj
        })
