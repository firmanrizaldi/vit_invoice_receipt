from odoo import models, fields, api, _
from odoo.exceptions import UserError
from num2words import num2words


class Invoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    
    amount_to_text = fields.Char(compute='_amount_to_text',
                                    string="amount text", required=False, )
    
    @api.depends('amount_total', 'currency_id')
    def _amount_to_text(self):
        for record in self:
            record.amount_to_text = num2words(record.amount_total ,lang= 'id' ) + " rupiah"
                

    