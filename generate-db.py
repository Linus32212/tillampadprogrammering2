import csv
import os
import locale

       #lista
def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []    
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products 

def view_products(products):
     for index, products in enumerate(products):
         print()

def list_all_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx} {product['name']} {product['price']} {product['desc']} {product['price']}")

def add_product(products):
    New_product = input("Skapa ett ID:")
    product.append(New_product)  
        
#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')

os.system('cls')
list_all_products(products)

while True:
    idx = int(input("Välj produkt: "))
    product = products[idx-1]
    print(f"ID: {product['id']}\n Namn: {product['name']} \nBeskrivning: {product['desc']} \n Pris: {product['price']} \n Kvantitet: {product['quantity']}")
