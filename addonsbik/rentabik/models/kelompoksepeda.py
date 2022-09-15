from asyncio import BaseTransport
from odoo import api, fields, models


class KelompokSepeda(models.Model):
    _name = 'rentabik.kelompoksepeda'
    _description = 'New Description'

    name = fields.Selection([
        ('sepedagunung','Sepeda Gunung'), ('motorlistrik','Motor Listrik'),('becak','Becak')
    ], string='Nama Kelompok')
    kode_kelompok = fields.Char(string='Kode Kelompok')
    
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'motorlistrik'):
            self.kode_kelompok = 'bike01'
        elif (self.name == 'sepedagunung'):
            self.kode_kelompok = 'bike02'
        elif (self.name == 'becak'):
            self.kode_kelompok = 'bike03'

    kode_sewa = fields.Char(string='Kode Sewa')
    kendaraan_ids = fields.One2many(comodel_name='rentabik.kendaraan', inverse_name='kelompoksepeda_id', string='Daftar Kendaraan')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('kendaraan_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['rentabik.kendaraan'].search([('kelompoksepeda_id','=',rec.id)]).mapped('name')
            b= len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
            
    
    
