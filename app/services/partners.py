# services/partners.py

import sys
import os

# Garante que o diretório 'app' esteja no path para que as pastas 'services' e 'tools' sejam reconhecidas
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

# Importando a função de sessão do Odoo
from tools.odoo_session import get_odoo_session

def list_all_partners(fields=None, limit=100):
    """
    Lista todos os parceiros (res.partner) com os campos especificados.

    :param fields: Lista de campos que deseja retornar. Ex: ['name', 'email']
    :param limit: Quantidade máxima de registros a retornar
    :return: Lista de dicionários com dados dos parceiros
    """
    session = get_odoo_session()
    res_partner = session['res.partner']

    domain = []  # sem filtro, pega todos
    partners = res_partner.search_read(domain, fields=fields, limit=limit)

    return partners
