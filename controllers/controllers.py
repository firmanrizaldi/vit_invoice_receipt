# -*- coding: utf-8 -*-
from odoo import http

# class VitInvoiceReceipt(http.Controller):
#     @http.route('/vit_invoice_receipt/vit_invoice_receipt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_invoice_receipt/vit_invoice_receipt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_invoice_receipt.listing', {
#             'root': '/vit_invoice_receipt/vit_invoice_receipt',
#             'objects': http.request.env['vit_invoice_receipt.vit_invoice_receipt'].search([]),
#         })

#     @http.route('/vit_invoice_receipt/vit_invoice_receipt/objects/<model("vit_invoice_receipt.vit_invoice_receipt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_invoice_receipt.object', {
#             'object': obj
#         })