# tools/odoo-session.py

import os
from dotenv import load_dotenv
from tools.odoo_rpc import OdooRPC

# Carrega variáveis do .env
load_dotenv()

def get_odoo_session():
    """
    Cria e retorna uma sessão de conexão com o Odoo.
    """
    url = os.getenv("URL")
    db_name = os.getenv("DB_NAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    if not all([url, db_name, username, password]):
        raise EnvironmentError("Algumas variáveis de ambiente estão faltando.")

    session = OdooRPC(url, db_name, username, password)
    session.connect()
    return session
