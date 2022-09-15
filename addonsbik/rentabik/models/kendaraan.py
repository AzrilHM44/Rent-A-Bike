from odoo import api, fields, models


class Kendaraan(models.Model):
    _name = 'rentabik.kendaraan'
    _description = 'New Description'

    name = fields.Char(string='Nama Kendaraan')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Sewa',required=True)
    kelompoksepeda_id = fields.Many2one(comodel_name='rentabik.kelompoksepeda', string='Kelompok Sepeda', 
                                                                                ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='rentabik.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')
    
    
    
