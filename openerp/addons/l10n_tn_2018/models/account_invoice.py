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

from openerp.osv import fields, osv
from num2words import num2words
import math


class account_invoice(osv.Model):
    _inherit = 'account.invoice'


    def _get_amount_to_text(self, cr, uid, ids, field_names=None, arg=False, context=None):
        if context is None:
            context = {}
        res = {}
        for invoice in self.browse(cr, uid, ids, context=context):
            num2words(42, lang='fr')
            txt = num2words(int(invoice.amount_total), lang='fr')
            if int(invoice.amount_total) > 1 :
                txt += ' Dinars '
            else :
                txt += ' Dinar '
            str_decimal = str(math.modf(invoice.amount_total)[0]*1000)
            txt += num2words(float(str_decimal), lang='fr') + ' millimes'
            res[invoice.id] = txt
        return res


    _columns = {
        'amount_to_text': fields.function(_get_amount_to_text, method=True,
                                          type='char', size=256, string='Amount to Text',
                                          help='Amount of the invoice in letter'),
    }

account_invoice()