from odoo import api, fields, models


class kendaraanDatang(models.TransientModel):
    _name = 'rentabik.kendaraandatang'

    kendaraan_id = fields.Many2one(
        comodel_name='rentabik.kendaraan',
        string='Nama kendaraan',
        required=True)


    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def button_kendaraan_datang(self):
        for rec in self:
            self.env['rentabik.kendaraan'].search([('id', '=', rec.kendaraan_id.id)]).write({'stok': rec.kendaraan_id.stok + rec.jumlah})
