# Installation Instructions / Инструкции за инсталација

## l10n_mk - North Macedonia Accounting Localization

**ВАЖНО / IMPORTANT**: Контниот план **НЕ** се инсталира автоматски! / The chart of accounts does **NOT** install automatically!

Следете ги точните чекори подолу зависно од вашата ситуација:

Follow the exact steps below depending on your situation:

---

## Сценарио 1: Нова компанија (Препорачано) / Scenario 1: New Company (Recommended)

### Македонски

#### Чекор 1: Инсталирајте го модулот

1. Најавете се во Odoo (http://localhost:8069)
2. Одете на **Apps** (Апликации) → Активирајте Developer Mode
3. Кликнете на **Update Apps List** (Ажурирај листа на апликации)
4. Пребарајте "North Macedonia" или "l10n_mk"
5. Кликнете **Install** на "North Macedonia - Accounting"

#### Чекор 2: Креирајте нова компанија

1. Одете на **Settings** → **Users & Companies** → **Companies**
2. Кликнете **Create** (Креирај)
3. Внесете име на компанијата
4. **КРИТИЧНО**: Поставете **Country** на **North Macedonia** / **Северна Македонија**
5. Кликнете **Save**

#### Чекор 3: Контниот план се инсталира автоматски

Кога ќе ја снимите компанијата со земја = North Macedonia, Odoo автоматски ќе го инсталира Македонскиот контен план.

#### Чекор 4: Верификувајте ја инсталацијата

1. Одете на **Accounting** → **Configuration** → **Chart of Accounts**
2. Треба да видите **439 конта вкупно**:
   - 428 македонски конта (на кирилица)
   - 11 стандардни Odoo конта
3. Проверете дали имињата се на **македонски кирилица** (пр. "Побарувања од купувачи")
4. Одете на **Accounting** → **Configuration** → **Taxes**
5. Треба да видите ДДВ даноци: 18%, 5%, 0% (Извоз/Увоз)

### English

#### Step 1: Install the Module

1. Log in to Odoo (http://localhost:8069)
2. Go to **Apps** → Activate Developer Mode
3. Click **Update Apps List**
4. Search for "North Macedonia" or "l10n_mk"
5. Click **Install** on "North Macedonia - Accounting"

#### Step 2: Create New Company

1. Go to **Settings** → **Users & Companies** → **Companies**
2. Click **Create**
3. Enter company name
4. **CRITICAL**: Set **Country** to **North Macedonia**
5. Click **Save**

#### Step 3: Chart of Accounts Installs Automatically

When you save the company with country = North Macedonia, Odoo will automatically install the Macedonian chart of accounts.

#### Step 4: Verify Installation

1. Go to **Accounting** → **Configuration** → **Chart of Accounts**
2. You should see **439 accounts total**:
   - 428 Macedonian accounts (in Cyrillic)
   - 11 standard Odoo accounts
3. Verify that names are in **Macedonian Cyrillic** (e.g., "Побарувања од купувачи")
4. Go to **Accounting** → **Configuration** → **Taxes**
5. You should see VAT taxes: 18%, 5%, 0% (Export/Import)

---

## Сценарио 2: Постоечка компанија / Scenario 2: Existing Company

### Macedonian

#### Чекор 1: Инсталирајте го модулот

1. Најавете се во Odoo
2. Одете на **Apps** → Активирајте Developer Mode
3. **Update Apps List** → Пребарајте "l10n_mk" → **Install**

#### Чекор 2: Поставете ја фискалната земја

1. Одете на **Settings** → **Companies** → **Update Info**
2. Поставете **Fiscal Country** на **North Macedonia**
3. **Снимете** ги промените

#### Чекор 3: Рачно инсталирајте го контниот план

**КРИТИЧНО**: Контниот план НЕ се инсталира автоматски за постоечки компании!

1. Одете на **Accounting** → **Configuration** → **Accounting**
2. Ќе видите копче **Install a Chart of Accounts**
3. Кликнете на копчето
4. Изберете **"Macedonian Chart of Accounts"** / **"Македонски контен план"**
5. Кликнете **Install**

#### Чекор 4: Верификувајте ја инсталацијата

Истите чекори како Сценарио 1, Чекор 4 - треба да видите 439 конта со македонски имиња.

### English

#### Step 1: Install the Module

1. Log in to Odoo
2. Go to **Apps** → Activate Developer Mode
3. **Update Apps List** → Search "l10n_mk" → **Install**

#### Step 2: Set Fiscal Country

1. Go to **Settings** → **Companies** → **Update Info**
2. Set **Fiscal Country** to **North Macedonia**
3. **Save** changes

#### Step 3: Manually Install Chart of Accounts

**CRITICAL**: Chart of accounts does NOT install automatically for existing companies!

1. Go to **Accounting** → **Configuration** → **Accounting**
2. You will see a button **Install a Chart of Accounts**
3. Click the button
4. Select **"Macedonian Chart of Accounts"**
5. Click **Install**

#### Step 4: Verify Installation

Same steps as Scenario 1, Step 4 - you should see 439 accounts with Macedonian names.

---

## Debugging / Дебагирање

### Проверка на логови (Check Logs)

```bash
# View Odoo logs
docker logs odoo_server

# Follow logs in real-time
docker logs -f odoo_server
```

### Рестарт на Odoo (Restart Odoo)

```bash
docker-compose restart odoo
```

### Целосен рестарт (Full restart)

```bash
docker-compose down
docker-compose up -d
```

---

## Development Mode / Развоен режим

За да овозможите развоен режим за детални пораки за грешки:

To enable development mode for detailed error messages:

```bash
# Access Odoo container
docker exec -it odoo_server bash

# Enable developer mode from URL
# Add ?debug=1 to the URL, e.g.:
# http://localhost:8069/web?debug=1
```

---

## Troubleshooting / Решавање на проблеми

### 1. Контниот план не се инсталира / Chart of Accounts Not Installing

**Проблем**: Инсталиравте го модулот, но немате македонски конта.

**Решение**:
- За **нова компанија**: Проверете дали земјата е точно поставена на "North Macedonia" при креирање
- За **постоечка компанија**: Следете го Сценарио 2 погоре - мора рачно да го инсталирате контниот план

**Верификација**: Одете на Chart of Accounts - треба да видите **439 конта**, не само 51 default конта

### 2. Модулот не се појавува во Apps листа / Module Not Appearing in Apps

**Причини**:
1. Модулот не е во правилниот директориум
2. Apps листата не е ажурирана
3. Developer mode не е активиран

**Решение**:
```bash
# Проверете дали модулот постои
ls -la /home/eskon/odoo/addons/l10n_mk/

# Рестартирајте Odoo
cd /home/eskon/odoo
docker-compose restart odoo

# Потоа: Apps → Update Apps List → Пребарајте "l10n_mk"
```

### 3. Грешка при инсталација / Installation Error

**Најчести причини**:
- Account модулот не е инсталиран (dependency)
- CSV фајловите се корумпирани
- Permission грешки

**Проверка на логови**:
```bash
# Погледнете ги логовите за детали
docker logs odoo_server | grep -i "l10n_mk"

# Follow logs во реално време
docker logs -f odoo_server
```

### 4. ДДВ даноците не се појавуваат / VAT Taxes Not Showing

**Проблем**: Инсталиравте го контниот план, но нема ДДВ даноци.

**Причина**: Контниот план не е правилно инсталиран.

**Решение**:
1. Проверете Chart of Accounts - треба да има **439 конта**
2. Ако има само 51 конта, контниот план не е инсталиран
3. Следете го Сценарио 2 за рачна инсталација

### 5. Имињата на контата не се на кирилица / Account Names Not in Cyrillic

**Проблем**: Контата постојат, но имињата не се на македонски.

**Причина**: CSV преводите не се вчитани правилно.

**Верификација**: Отворете било кое конто - треба да видите имиња како:
- "Побарувања од купувачи" (a120)
- "Обврски кон добавувачи" (a220)
- "Приходи од продажба на стоки" (a740)

**Решење**: Upgrade модулот:
```bash
docker-compose run --rm odoo odoo -d your_database -u l10n_mk --stop-after-init
```

---

## Напредна инсталација / Advanced Installation

### За развивачи / For Developers

```bash
# Development mode со детални логови
docker-compose run --rm odoo odoo \
  -d odoo_dev \
  -i l10n_mk \
  --dev=all \
  --log-level=debug \
  --stop-after-init

# Тестирање
docker-compose run --rm odoo odoo \
  -d odoo_dev \
  -u l10n_mk \
  --test-enable \
  --stop-after-init
```

### Рачно тригерирање на контен план / Manually Trigger Chart Installation

Ако автоматската инсталација не работи:

```python
# Во Odoo shell (само за напредни корисници)
# docker-compose run --rm odoo odoo shell -d your_database

company = env.company
ChartTemplate = env['account.chart.template']
ChartTemplate.try_loading('mk', company)
```

---

## Следни чекори / Next Steps

После успешната инсталација на контниот план:

1. **Конфигурирајте ја компанијата**:
   - Додадете ЕДБ (даночен број)
   - Додадете ЕМБС
   - Поставете банкарски сметки

2. **Конфигурирајте даноци**:
   - Проверете ги ДДВ стапките (18%, 5%, 0%)
   - Конфигурирајте фискални позиции за EU/извоз

3. **Додадете партнери**:
   - **Contacts** → **Create**
   - Додадете купувачи и добавувачи со македонски податоци

4. **Започнете со трансакции**:
   - **Accounting** → **Customers** → **Invoices**
   - Креирајте влезни и излезни фактури

---

## Поддршка / Support

За прашања, баг репорти и поддршка:

**For questions, bug reports and support:**

- **Email**: info@eskon.mk
- **GitHub Repository**: https://github.com/eskon/odoo
- **GitHub Issues**: https://github.com/eskon/odoo/issues
- **Website**: https://eskon.mk

**Technical Information:**

- **Module**: l10n_mk (North Macedonia - Accounting)
- **Version**: 18.0.1.0.0
- **Odoo Version**: 18.0
- **Author**: ЕСКОН-ИНЖЕНЕРИНГ ДООЕЛ Струмица
- **License**: LGPL-3
