# North Macedonia - Accounting Localization (l10n_mk)

**Macedonian Accounting Localization for Odoo 18.0**

**Македонска сметководствена локализација за Odoo 18.0**

---

## Features / Карактеристики

### English

This module provides comprehensive accounting localization for North Macedonia:

- **Complete Chart of Accounts** - **428 accounts** based on official Macedonian accounting standards (МСС/МСФИ - IAS/IFRS)
- **VAT Configuration** - Full VAT setup with 18%, 5%, and 0% rates
- **Fiscal Positions** - Pre-configured for domestic, EU, and international transactions
- **Account Groups** - Organized by classes 0-9 (assets, liabilities, equity, income, expenses)
- **Tax Groups** - Automated tax calculation and reporting
- **Automatic Account Mapping** - Receivables, payables, income, and expense accounts
- **3-digit Account Codes** - Based on official Macedonian chart of accounts structure
- **Reconciliation Models** - Pre-configured for common Macedonian business transactions
- **Macedonian Language Support** - All account names in Cyrillic (Македонски јазик)

### Македонски

Овој модул обезбедува целосна сметководствена локализација за Северна Македонија:

- **Комплетен контен план** - **428 сметки** базирани на официјални македонски сметководствени стандарди (МСС/МСФИ)
- **ДДВ конфигурација** - Целосно поставување на ДДВ со стапки од 18%, 5% и 0%
- **Фискални позиции** - Претконфигурирани за домашни, ЕУ и меѓународни трансакции
- **Групирање на конта** - Организирани по класи 0-9 (средства, обврски, капитал, приходи, расходи)
- **Даночни групи** - Автоматизирано пресметување и известување на даноци
- **Автоматско мапирање на сметки** - Побарувања, обврски, приходи и расходни сметки
- **3-цифрени кодови на сметки** - Базирани на официјален македонски контен план
- **Модели за затворање** - Претконфигурирани за вообичаени македонски деловни трансакции
- **Поддршка за македонски јазик** - Сите имиња на сметки на кирилица

## Technical Information / Технички информации

### Odoo 18 Architecture / Архитектура на Odoo 18

This module uses Odoo 18's modern chart template system:

- Chart data loaded from CSV files in `data/template/` directory
- Template methods use `@template` decorator
- Automatic loading via `_parse_csv()` method
- No XML-based account templates (deprecated in Odoo 18)

Овој модул користи модерен систем за шаблони на контен план во Odoo 18:

- Податоците за контниот план се вчитуваат од CSV фајлови во `data/template/` директориум
- Методите за шаблони користат `@template` декоратор
- Автоматско вчитување преку `_parse_csv()` метод
- Без XML-базирани шаблони за сметки (deprecated во Odoo 18)

## Installation / Инсталација

### English

#### For New Companies (Recommended):

1. Install the module from Apps menu
2. Create a new company with country set to "North Macedonia"
3. The chart of accounts will be installed automatically
4. Configure your company details

#### For Existing Companies:

1. Install the module from Apps menu
2. Go to **Settings** → **Companies** → Update Info
3. Set **Fiscal Country** to "North Macedonia"
4. Go to **Accounting** → **Configuration** → **Accounting**
5. Click **Install Chart of Accounts**
6. Select "Macedonian Chart of Accounts"
7. Click **Install**

See `INSTALLATION.md` for detailed step-by-step instructions.

### Македонски

#### За нови компании (Препорачано):

1. Инсталирајте го модулот од менито Апликации
2. Креирајте нова компанија со земја поставена на "Северна Македонија"
3. Контниот план автоматски ќе се инсталира
4. Конфигурирајте ги деталите на вашата компанија

#### За постоечки компании:

1. Инсталирајте го модулот од менито Апликации
2. Одете на **Settings** → **Companies** → Update Info
3. Поставете **Fiscal Country** на "Северна Македонија"
4. Одете на **Accounting** → **Configuration** → **Accounting**
5. Кликнете **Install Chart of Accounts**
6. Изберете "Macedonian Chart of Accounts"
7. Кликнете **Install**

Видете `INSTALLATION.md` за детални инструкции чекор-по-чекор.

## Chart of Accounts Structure / Структура на контен план

### Класа 0: Долгорочни нематеријални и материјални средства (Fixed Assets)
- 000-009: Нематеријални средства (Intangible Assets)
- 010-019: Материјални средства (Tangible Assets)
- 020-099: Финансиски средства (Financial Assets)

### Класа 1: Краткорочни средства и побарувања (Current Assets)
- 100-109: Парични средства (Cash & Bank)
- 110-119: Краткорочни финансиски средства (Short-term Financial Assets)
- 120-129: Побарувања од купувачи (Accounts Receivable)
- 130-139: Останати побарувања (Other Receivables)

### Класа 2: Капитал и обврски (Equity and Liabilities)
- 200-219: Капитал (Equity)
- 220-239: Обврски кон добавувачи (Accounts Payable)
- 240-299: Останати обврски (Other Liabilities)

### Класа 3: Приходи од продажба и финансиски приходи (Sales & Financial Income)
- 300-399: Приходи од продажба (Sales Revenue)

### Класа 4: Расходи од редовната дејност (Operating Expenses)
- 400-499: Деловни расходи (Operating Expenses)

### Класа 5: Финансиски расходи (Financial Expenses)
- 500-599: Финансиски расходи (Financial Expenses)

### Класа 6: Вонредни и редовни расходи (Extraordinary & Regular Expenses)
- 600-699: Вонредни расходи (Extraordinary Expenses)

### Класа 7: Приходи (Income)
- 700-799: Приходи (Income)

## VAT Rates / ДДВ Стапки

| Rate | Type | Description MK | Description EN |
|------|------|----------------|----------------|
| **18%** | Standard | Стандардна ДДВ стапка | Standard VAT rate |
| **5%** | Reduced | Намалена ДДВ стапка | Reduced VAT rate |
| **0%** | Export/Import | Извоз/Увоз | Export/Import |

## Fiscal Positions / Фискални позиции

- **EU Intra-Community (B2B)** - EU Интракомунитарно (Б2Б)
- **EU Private Individuals (B2C)** - ЕУ Приватни лица (Б2Ц)
- **Export (Non-EU)** - Извоз (Надвор од ЕУ)
- **Import** - Увоз

## Database Structure / Структура на базата

```
l10n_mk/
├── data/
│   ├── template/
│   │   ├── account.account-mk.csv      (428 accounts)
│   │   ├── account.group-mk.csv        (Account groups)
│   │   ├── account.tax-mk.csv          (VAT taxes)
│   │   └── account.tax.group-mk.csv    (Tax groups)
│   ├── account_chart_template_data.xml
│   └── account_chart_template_configure_data.xml
└── models/
    └── template_mk.py                   (Template methods)
```

## Module Dependencies / Зависности на модулот

- `account` - Odoo Accounting module (required)
- `base` - Odoo Base module (automatically installed)

## Version History / Историја на верзии

- **18.0.1.0.0** - Initial release for Odoo 18.0
  - 428 Macedonian accounts
  - VAT configuration (18%, 5%, 0%)
  - Fiscal positions for EU and international trade
  - Account groups and reconciliation models

## Contributing / Придонес

Contributions are welcome! Please submit pull requests to:
https://github.com/eskon/odoo

Придонесите се добредојдени! Ве молиме испратете pull requests на:
https://github.com/eskon/odoo

## License / Лиценца

LGPL-3

## Credits / Автори

**Author / Автор:**
- ЕСКОН-ИНЖЕНЕРИНГ ДООЕЛ Струмица

**Maintainer / Одржување:**
- ЕСКОН-ИНЖЕНЕРИНГ Development Team

**Based on / Базирано на:**
- Official Macedonian Chart of Accounts (Службен контен план на РСМ)
- Macedonian Accounting Standards (Македонски сметководствени стандарди - МСС)
- International Financial Reporting Standards (IFRS/МСФИ)

## Support / Поддршка

For support, please contact:

За поддршка, контактирајте:

- **Email**: info@eskon.com.mk
- **GitHub**: https://github.com/eskon/odoo/issues
- **Website**: https://www.eskon.com.mk

## Disclaimer / Напомена

This module is provided as-is for accounting purposes. Please consult with a certified accountant for specific accounting and tax advice in North Macedonia.

Овој модул е обезбеден како што е за сметководствени цели. Ве молиме консултирајте се со овластен сметководител за специфични сметководствени и даночни совети во Северна Македонија.
