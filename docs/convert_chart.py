#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert mk_chart_of_accounts_odoo18.csv to Odoo 18 template format
"""

import csv

# Input and output files
input_file = '/home/eskon/odoo/addons/l10n_mk/docs/mk_chart_of_accounts_odoo18.csv'
output_file = '/home/eskon/odoo/addons/l10n_mk/data/template/account.account-mk.csv'

# Read input CSV
accounts = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        code = row['Code'].strip()
        name = row['Name'].strip()
        account_type = row['Type'].strip()
        reconcile = row['Allow Reconciliation'].strip()

        # Convert reconcile to boolean string
        reconcile_bool = 'True' if reconcile.lower() == 'true' else 'False'

        accounts.append({
            'id': f'a{code}',
            'name': name,
            'code': code,
            'account_type': account_type,
            'reconcile': reconcile_bool,
            'tag_ids': ''
        })

# Write output CSV in Odoo 18 format
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['id', 'name', 'code', 'account_type', 'reconcile', 'tag_ids']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(accounts)

print(f"✓ Converted {len(accounts)} accounts")
print(f"  Input:  {input_file}")
print(f"  Output: {output_file}")
