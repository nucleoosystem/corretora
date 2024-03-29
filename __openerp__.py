# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-Today OpenERP S.A. (<http://www.openerp.com>).
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

{
    'name': 'Corretora',
    'version': '1.0',
    'category': 'Others',
    'sequence': 2,
    'summary': 'ATS Corretora',
    'description': """
   """,
    'author': 'ATS Soluções',
    'website': '',
    'depends': ['l10n_br_base','l10n_br_crm'],
    'data': [
        #'security/ir.model.access.csv',
        #'security/crm_productsite_security.xml',   
        'crm_lead_view.xml',
        'crm_opportunity_view.xml',
    ],
    'installable': True,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
