import os
import sys

# Adiciona a pasta `app/` ao sys.path
CURRENT_DIR = os.path.dirname(__file__)
APP_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, APP_DIR)

from services.partners import list_all_partners

def main():
    print("Listando parceiros do Odoo...")
    try:
        partners = list_all_partners(fields=['name', 'email'], limit=10)
        for partner in partners:
            print(f"ID: {partner.get('id')} | Nome: {partner.get('name')} | Email: {partner.get('email')}")
    except Exception as e:
        print(f"Erro ao buscar parceiros: {e}")

if __name__ == '__main__':
    main()
