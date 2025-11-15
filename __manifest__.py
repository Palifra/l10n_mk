# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'North Macedonia - Accounting',
    'version': '18.0.1.0.0',
    'icon': '/account/static/description/l10n.png',
    'countries': ['mk'],
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
North Macedonia - Accounting Localization
==========================================

This module provides the Odoo Accounting localization for North Macedonia:

    * Chart of Accounts (1,677 accounts) based on official Macedonian accounting standards (МСС/МСФИ - IAS/IFRS)
    * VAT configuration (ДДВ 18%, 5%, 0% for export/import)
    * Tax groups and fiscal positions for domestic and international transactions
    * Bank account configuration
    * Account types and reconciliation models

Локализација на Одоо сметководство за Северна Македонија:

    * Контен план (1,677 сметки) базиран на официјални македонски сметководствени стандарди (МСС/МСФИ)
    * Конфигурација на ДДВ (18%, 5%, 0% за извоз/увоз)
    * Даночни групи и фискални позиции за домашни и меѓународни трансакции
    * Конфигурација на банкарски сметки
    * Типови на сметки и модели за затворање
    """,
    'author': 'ЕСКОН-ИНЖЕНЕРИНГ ДООЕЛ Струмица',
    'website': 'https://github.com/eskon/odoo',
    'maintainer': 'ЕСКОН-ИНЖЕНЕРИНГ Development Team',
    'depends': [
        'account',
    ],
    'data': [
        # Currency configuration
        'data/account_chart_template_data.xml',

        # Note: Chart of accounts, account groups, taxes, tax groups, and fiscal
        # positions are loaded automatically via the template_mk.py Python model
        # using the @template decorator (Odoo 18 approach).
        # CSV data files are in data/template/ directory.

        # Post-installation configuration
        'data/account_chart_template_configure_data.xml',
    ],
    'demo': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
