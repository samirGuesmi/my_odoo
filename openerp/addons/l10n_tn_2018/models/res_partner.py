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

from openerp.osv import fields, osv, orm


class res_partner(osv.Model):
    """ Inherits partner and adds company registry information in the partner form """
    _inherit = 'res.partner'

    _columns = {
        'company_registry': fields.char('Company registry', help='The company registry information of the partner.'),
        'unique_fiscal_identification_number': fields.char('Unique Fiscal Identification Number', size=7),
        'unique_fiscal_key_control': fields.char('Unique Fiscal Key Control', size=1),
        'fiscal_code': fields.selection([('A', 'A'), ('P', 'P'), ('B', 'B'), ('D', 'D'), ('N', 'N')], 'Fiscal Code'),
        'fiscal_category_code': fields.selection([('M', 'M'), ('P', 'P'), ('C', 'C'), ('N', 'N'), ('E', 'E')], 'Fiscal Category Code'),
        'secondary_establishment_number': fields.char('Secondary Establishment Number', size=3),
    }
