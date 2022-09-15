from odoo import api, fields, models


class Person(models.Model):
    _name = 'rentabik.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'rentabik.kasir'
    _inherit = 'rentabik.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')
    


