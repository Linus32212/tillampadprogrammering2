import csv
import os
import locale

# small helper to format currency using locale
def format_currency(value):
    try:
        return locale.currency(value, grouping=True)
    except Exception:
        return f"{value:.2f}"


def _get_field(row, *aliases, default=''):
    """Return the first matching key from row (case-insensitive) or default."""
    # normalize lookup to lower-case keys
    lower_map = {k.lower(): k for k in row.keys()}
    for a in aliases:
        key = a.lower()
        if key in lower_map:
            return row[lower_map[key]]
    return default


def load_data(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # use aliases for description (csv has 'description' not 'desc')
            try:
                id_val = int(_get_field(row, 'id'))
            except Exception:
                # skip rows with invalid id
                continue

            name = _get_field(row, 'name', 'product', default='')
            desc = _get_field(row, 'desc', 'description', 'beskrivning', default='')
            try:
                price = float(_get_field(row, 'price', 'pris', default='0') or 0)
            except Exception:
                price = 0.0
            try:
                quantity = int(_get_field(row, 'quantity', 'qty', default='0') or 0)
            except Exception:
                quantity = 0

            products.append({
                'id': id_val,
                'name': name,
                'desc': desc,
                'price': price,
                'quantity': quantity,
            })
    return products


def view_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product['name']} — {format_currency(product['price'])}")


def list_all_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx} {product['name']} {format_currency(product['price'])} {product['desc']}")


def add_product(products):
    # minimal add flow — only name and price for now
    try:
        new_id = int(input("Ange ID (heltal): "))
    except ValueError:
        print("Ogiltigt ID")
        return
    name = input("Namn: ")
    desc = input("Beskrivning: ")
    try:
        price = float(input("Pris: "))
    except ValueError:
        price = 0.0
    try:
        quantity = int(input("Kvantitet: "))
    except ValueError:
        quantity = 0

    products.append({
        'id': new_id,
        'name': name,
        'desc': desc,
        'price': price,
        'quantity': quantity,
    })


# set locale if available; fall back quietly if not
try:
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')
except Exception:
    try:
        locale.setlocale(locale.LC_ALL, '')
    except Exception:
        pass


if __name__ == '__main__':
    products = load_data('db_products.csv')

    os.system('cls')
    list_all_products(products)

    while True:
        try:
            idx = int(input("Välj produkt (nummer, 0 = avsluta): "))
        except ValueError:
            print("Ange ett giltigt nummer")
            continue
        if idx == 0:
            break
        if idx < 1 or idx > len(products):
            print("Ogiltigt val")
            continue
        product = products[idx-1]
        print(
            f"ID: {product['id']}\nNamn: {product['name']}\nBeskrivning: {product['desc']}\nPris: {format_currency(product['price'])}\nKvantitet: {product['quantity']}\n"
        )
    
    
    
    
    
    
