# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Activity Based Costing',
    'summary': '''Activity Based Costing''',
    'author': 'ONESTEiN BV',
    'website': 'http://www.onestein.eu',
    'category': 'Accounting & Finance',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'account_budget',
        'analytic',
        'web_widget_float_highlight',
        'project',
    ],
    'data': [
        'views/account_analytic_account.xml',
        'menu_items.xml',
    ],
    'installable': True,
}
