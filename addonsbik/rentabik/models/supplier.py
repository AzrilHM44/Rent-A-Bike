from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'rentabik.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    kendaraan_id = fields.Many2many(comodel_name='rentabik.kendaraan', string='Kendaraan')
    
    
    
