class OdooEnvironment:
    def __init__(self, rpc):
        self.rpc = rpc

    def __getitem__(self, model_name):
        return OdooObject(self.rpc, model_name)


class OdooObject:
    def __init__(self, rpc, model_name, record_id=None):
        self.rpc = rpc
        self.model_name = model_name
        self.record_id = record_id

    def search(self, domain, offset=0, limit=None, order=None):
        kwargs = {
            'offset': offset,
            'limit': limit,
            'order': order,
        }
        return self.rpc.execute_kw(self.model_name, 'search', [domain], kwargs)

    def read(self, ids, fields=None):
        kwargs = {
            'fields': fields,
        }
        return self.rpc.execute_kw(self.model_name, 'read', [ids], kwargs)

    def search_read(self, domain, fields=None, offset=0, limit=None, order=None):
        kwargs = {
            'fields': fields,
            'offset': offset,
            'limit': limit,
            'order': order,
        }
        return self.rpc.execute_kw(self.model_name, 'search_read', [domain], kwargs)

    def write(self, ids, values):
        return self.rpc.execute_kw(self.model_name, 'write', [ids, values], {})

    def create(self, values):
        return self.rpc.execute_kw(self.model_name, 'create', [values], {})

    def unlink(self, ids):
        return self.rpc.execute_kw(self.model_name, 'unlink', [ids], {})
