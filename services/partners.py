from tools.odoo import OdooObject

def list_partners(session, limit=10):
    partner_obj = OdooObject(session, 'res.partner')
    return partner_obj.search_read([], fields=['name', 'email'], limit=limit)
