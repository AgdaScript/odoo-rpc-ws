# tools/rpc.py
import xmlrpc.client as xmlrpc
from tools.odoo import OdooObject, OdooEnvironment


class OdooRPC:
    #inicializa o odoo e o bd
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.models = None
        self.env = OdooEnvironment(self)
        self.user = None
        self.service_app = None

    #Autentica e conecta com o odoo via rpc 
    def connect(self):
        #common = xmlrpc.ServerProxy('{}/xmlrpc/2/common'.format(self.server))
        common = xmlrpc.ServerProxy('{}/xmlrpc/2/common'.format(self.server), allow_none=True)

        self.uid = common.authenticate(self.database, self.username, self.password, {})
        self.models = xmlrpc.ServerProxy('{}/xmlrpc/2/object'.format(self.server), allow_none=True)
        #se autenticado com sucesso cria um objeto para o user autenticado
        if self.uid:
            self.user = OdooObject(self, 'res.users', self.uid)

    #metodo para executar qq metodo de qq modelo odoo via rpc
    def execute_kw(self, model_name, method, args, kwargs):
        print('RPC execute_kw: %s.%s', model_name, method)
        return self.models.execute_kw(self.database, self.uid, self.password, model_name, method, args, kwargs)

    #permite usar o res.partner como atalho para acessar o odoo envirememt
    def __getitem__(self, key):
        return self.env[key]
