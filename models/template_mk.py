# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import Command, _, models

from odoo.addons.account.models.chart_template import template
import logging

_logger = logging.getLogger(__name__)


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('mk')
    def _get_mk_template_data(self):
        """
        Macedonian Chart of Accounts Template
        Контен план според македонските сметководствени стандарди (МСС/МСФИ)
        """
        return {
            'name': _('Macedonian Chart of Accounts'),
            'parent': False,
            'code_digits': '3',
            'property_account_receivable_id': 'a120',
            'property_account_payable_id': 'a220',
            'property_account_expense_categ_id': 'a400',
            'property_account_income_categ_id': 'a740',
        }

    @template('mk', 'res.company')
    def _get_mk_res_company(self):
        """
        Company-specific configuration for Macedonian companies
        Конфигурација за македонски компании
        """
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.mk',
                'bank_account_code_prefix': '100',
                'cash_account_code_prefix': '102',
                'transfer_account_code_prefix': '108',
                'account_default_pos_receivable_account_id': 'a120',
                'account_sale_tax_id': 'att_vat_sale_18',
                'account_purchase_tax_id': 'att_vat_purchase_18',
            },
        }

    @template('mk', 'account.journal')
    def _get_mk_account_journal(self):
        """
        Journal configuration for Macedonian accounting
        Конфигурација на дневници
        """
        return {
            'sale': {'refund_sequence': True},
            'purchase': {'refund_sequence': True},
        }

    @template('mk', 'account.tax.group')
    def _get_mk_account_tax_group(self):
        """
        Tax groups for Macedonian VAT rates
        Даночни групи за македонски ДДВ стапки
        """
        return {
            'atg_vat_18': {
                'name': 'ДДВ 18% / VAT 18%',
                'sequence': 1,
            },
            'atg_vat_5': {
                'name': 'ДДВ 5% / VAT 5%',
                'sequence': 2,
            },
            'atg_vat_exempt': {
                'name': 'ДДВ 0% / VAT 0%',
                'sequence': 3,
            },
        }

    @template('mk', 'account.tax')
    def _get_mk_account_tax(self):
        """
        Macedonian VAT taxes with repartition lines
        Македонски ДДВ даноци со линии за распределба
        """
        return {
            'att_vat_sale_18': {
                'name': 'ДДВ 18%',
                'amount': 18.0,
                'amount_type': 'percent',
                'type_tax_use': 'sale',
                'sequence': 10,
                'country_id': 'base.mk',
                'tax_group_id': 'atg_vat_18',
                'invoice_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a230'}),
                ],
                'refund_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a230'}),
                ],
            },
            'att_vat_purchase_18': {
                'name': 'ДДВ 18%',
                'amount': 18.0,
                'amount_type': 'percent',
                'type_tax_use': 'purchase',
                'sequence': 10,
                'country_id': 'base.mk',
                'tax_group_id': 'atg_vat_18',
                'invoice_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a130'}),
                ],
                'refund_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a130'}),
                ],
            },
            'att_vat_sale_5': {
                'name': 'ДДВ 5%',
                'amount': 5.0,
                'amount_type': 'percent',
                'type_tax_use': 'sale',
                'sequence': 20,
                'country_id': 'base.mk',
                'tax_group_id': 'atg_vat_5',
                'invoice_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a230'}),
                ],
                'refund_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a230'}),
                ],
            },
            'att_vat_purchase_5': {
                'name': 'ДДВ 5%',
                'amount': 5.0,
                'amount_type': 'percent',
                'type_tax_use': 'purchase',
                'sequence': 20,
                'country_id': 'base.mk',
                'tax_group_id': 'atg_vat_5',
                'invoice_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a130'}),
                ],
                'refund_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a130'}),
                ],
            },
            'att_vat_sale_0': {
                'name': 'Извоз 0%',
                'amount': 0.0,
                'amount_type': 'percent',
                'type_tax_use': 'sale',
                'sequence': 30,
                'country_id': 'base.mk',
                'tax_group_id': 'atg_vat_exempt',
                'invoice_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a230'}),
                ],
                'refund_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a230'}),
                ],
            },
            'att_vat_purchase_0': {
                'name': 'Увоз 0%',
                'amount': 0.0,
                'amount_type': 'percent',
                'type_tax_use': 'purchase',
                'sequence': 30,
                'country_id': 'base.mk',
                'tax_group_id': 'atg_vat_exempt',
                'invoice_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a130'}),
                ],
                'refund_repartition_line_ids': [
                    Command.create({'repartition_type': 'base'}),
                    Command.create({'repartition_type': 'tax', 'account_id': 'a130'}),
                ],
            },
        }

    @template('mk', 'account.reconcile.model')
    def _get_mk_reconcile_model(self):
        """
        Reconciliation models for common Macedonian transactions
        Модели за затворање на типични македонски трансакции
        """
        return {
            'bank_fees_template': {
                'name': 'Bank Fees',
                'line_ids': [
                    Command.create({
                        'account_id': 'a400',
                        'amount_type': 'percentage',
                        'amount_string': '100',
                        'label': 'Bank Fees',
                    }),
                ],
                'name@mk': 'Банкарски провизии',
                'name@en': 'Bank Fees',
            },
        }

    @template('mk', 'account.fiscal.position')
    def _get_mk_account_fiscal_position(self):
        """
        Fiscal positions for Macedonian VAT scenarios
        Фискални позиции за македонски ДДВ сценарија
        """
        return {
            'fiscal_position_eu_b2b': {
                'name': 'EU Intra-Community (B2B)',
                'name@mk': 'ЕУ Интракомунитарно (Б2Б)',
                'name@en': 'EU Intra-Community (B2B)',
                'auto_apply': True,
                'vat_required': True,
                'country_group_id': 'account.europe',
                'tax_ids': [
                    # Map 18% sale tax to 0% export tax for EU B2B
                    Command.create({
                        'tax_src_id': 'att_vat_sale_18',
                        'tax_dest_id': 'att_vat_sale_0',
                    }),
                    Command.create({
                        'tax_src_id': 'att_vat_sale_5',
                        'tax_dest_id': 'att_vat_sale_0',
                    }),
                ],
            },
            'fiscal_position_eu_b2c': {
                'name': 'EU Private Individuals (B2C)',
                'name@mk': 'ЕУ Приватни лица (Б2Ц)',
                'name@en': 'EU Private Individuals (B2C)',
                'auto_apply': True,
                'vat_required': False,
                'country_group_id': 'account.europe',
                # No tax mapping - regular VAT applies for B2C sales
            },
            'fiscal_position_export': {
                'name': 'Export (Non-EU)',
                'name@mk': 'Извоз (Надвор од ЕУ)',
                'name@en': 'Export (Non-EU)',
                'auto_apply': False,  # Manual selection
                'tax_ids': [
                    # Map all sale taxes to 0% for exports
                    Command.create({
                        'tax_src_id': 'att_vat_sale_18',
                        'tax_dest_id': 'att_vat_sale_0',
                    }),
                    Command.create({
                        'tax_src_id': 'att_vat_sale_5',
                        'tax_dest_id': 'att_vat_sale_0',
                    }),
                ],
            },
            'fiscal_position_import': {
                'name': 'Import',
                'name@mk': 'Увоз',
                'name@en': 'Import',
                'auto_apply': False,  # Manual selection
                'tax_ids': [
                    # Map purchase taxes to 0% for imports (customs handles VAT)
                    Command.create({
                        'tax_src_id': 'att_vat_purchase_18',
                        'tax_dest_id': 'att_vat_purchase_0',
                    }),
                    Command.create({
                        'tax_src_id': 'att_vat_purchase_5',
                        'tax_dest_id': 'att_vat_purchase_0',
                    }),
                ],
            },
        }

    # CSV files should load automatically, but we explicitly call _parse_csv
    # as a workaround for path resolution issues
    @template('mk', 'account.group')
    def _get_mk_account_group(self):
        return self._parse_csv('mk', 'account.group')

    @template('mk', 'account.account')
    def _get_mk_account_account(self):
        return self._parse_csv('mk', 'account.account')
