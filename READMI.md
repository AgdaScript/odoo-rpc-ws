|- tools
    |- rpc.py
        ->Centraliza a autenticação com o Odoo.
        ->Fornece um método genérico (execute_kw) para chamar qualquer função no Odoo.
        ->Funciona com OdooObject para facilitar o acesso orientado a objetos a modelos do Odoo.


app/
│
├── tools/
│   ├── rpc.py             # Lida com a comunicação RPC
│   ├── odoo.py            # Define OdooObject e OdooEnvironment
│
├── services/
│   ├── employees.py       # Lógica de listagem e filtro de funcionários
│   ├── partners.py        # Lógica de listagem de parceiros
│
├── birthday/
│   └── birthday.py        # Script que chama os serviços e roda o relatório
│
└── main.py                # Ponto de entrada, se quiser orquestrar tudo
