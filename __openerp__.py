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


{
    'name': 'eBay',
    'version': '1.0',
    'author': 'xlongfeng',
    'category': 'Uncategorized',
    'depends': ['base', 'base_import', 'sale_stock'],
    'demo': [],
    'description': """
This is a module for managing ebay listings, orders and messages in OpenERP.
    """,
    'data': [
        'security/ebay_security.xml',
        'ebay_view.xml',
        'ebay_seller_list_view.xml',
        'ebay_user_view.xml',
        'ebay_item_view.xml',
        'ebay_message_view.xml',
        'wizard/sale_order_state_view.xml',
        'ebay_sale_view.xml',
        'photobucket_view.xml',
        'res_partner_view.xml',
        'wizard/export_order_view.xml',
        'wizard/get_order_view.xml',
        'wizard/item_state_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
