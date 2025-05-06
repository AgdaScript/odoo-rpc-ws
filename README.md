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



app/
├── services/
│   ├── birthday-service.py
│   ├── employee.py
│   └── partners.py
└── tools/
    ├── odoo-conection.py
    ├── odoo-rpc.py
    └── odoo-session.py


app/
├── scripts/
│   └── partners_script.py
├── services/
│   └── partners.py
├── tools/
│   └── odoo_session.py


 Frontend (com Infinite Scroll):
Manda um request inicial com "direction": "center" e a center_date

Ao rolar para baixo:

Atualiza a center_date para o último item visível

Chama a API com "direction": "next"

Ao rolar para cima:

Atualiza a center_date para o primeiro item visível

Chama a API com "direction": "previous"


app/
├── api/
│   └── birthday.py
├── services/
│   └── birthday_service.py
├── tools/
│   └── lazy_loader.py
└── main.py


pip install fastapi
