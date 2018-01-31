# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api, fields

class AccountTaxInvoice(models.Model):
    _inherit = 'account.invoice.tax'

    is_timbre_line = fields.Boolean('Is Timbre', default=False)

AccountTaxInvoice()

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    @api.depends('invoice_line.price_subtotal', 'tax_line.amount', 'partner_id')
    def _compute_amount(self):
        timbre_line = self.env['account.invoice.tax'].search([
            ('invoice_id', '=', self.id),('is_timbre_line', '=', True)
        ])
        if self.partner_id and self.partner_id.fiscal_category_code != 'M' and not timbre_line:
            if self.type in ('in_invoice', 'in_refund', 'out_invoice', 'out_refund'):
                if (self.type in ('out_invoice', 'out_refund')):
                    tax_obj = self.env['account.tax'].search(
                        [('description', '=', 'Timbre-sale'), ('type_tax_use', 'in', ('all', 'sale'))])
                if (self.type in ('in_refund', 'in_invoice')):
                    tax_obj = self.env['account.tax'].search(
                        [('description', '=', 'Timbre-purchase'), ('type_tax_use', 'in', ('all', 'purchase'))])
                if (self.type in ('in_invoice', 'out_invoice')):
                    account_id = tax_obj.account_collected_id
                else:
                    account_id = tax_obj.account_paid_id
                if len(tax_obj):
                    timbre_line = self.env['account.invoice.tax'].create(
                        {
                            'is_timbre_line' : True,
                            'invoice_id': self.id,
                            'name': tax_obj.name,
                            'amount': tax_obj.amount,
                            'tax_amount': tax_obj.amount,
                            'tax_code_id': tax_obj.tax_code_id.id,
                            'base_code_id': tax_obj.base_code_id.id,
                            'account_id': account_id.id, 'manual': True,
                        })
                    self.tax_line = [(6,0, timbre_line.ids)]
        else:
            self.tax_line = [(6, 0, [])]
        res = super(account_invoice, self)._compute_amount()
        return res


account_invoice()
