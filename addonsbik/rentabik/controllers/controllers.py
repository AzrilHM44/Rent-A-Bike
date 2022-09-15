from odoo import http, models, fields
from odoo.http import request
import json

class rentabik(http.Controller):
    @http.route('/rentabik/getkendaraan', auth='public', method=['GET'])
    def getkendaraan(self, **kw):
        kendaraan = request.env['rentabik.kendaraan'].search([])
        isi = []
        for bb in kendaraan:
            isi.append({
                'nama_kendaraan' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)

    @http.route('/rentabik/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['rentabik.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'kendaraan' : s.kendaraan_id[0].name
            })
        return json.dumps(sup)