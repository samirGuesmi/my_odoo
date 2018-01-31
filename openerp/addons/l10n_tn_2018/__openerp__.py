# -*- encoding: utf-8 -*-

{
    "name": "Tunisian - Accounting 2018",
    "version": "1.0",
    "author": "DevCostKiller : Mehdi CHAHED",
    "website": "http://www.devcostkiller.com",
    "category": "Localization/Account Charts",
    "depends": ['base',
                'account',
                # 'account_voucher',
                # 'l10n_tn_rib'
                ],
    "data": [
        'report/report_invoice_document.xml',
        'views/res_partner.xml',
        'views/account_bank_statement_view.xml',
        'views/account_voucher_view.xml',
        'data/plan_comptable_general.xml',
        'data/tn_pcg_taxes.xml',
        'data/tn_tax.xml',
        'wizard/l10n_tn_wizard.xml',
        'security/ir.model.access.csv',
    ],
    "test": [],
    "demo_xml": [],
    "active": True,
    "installable": True,
    'images': ['images/config_chart_l10n_tn.jpg', 'images/l10n_tn_chart.jpg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
