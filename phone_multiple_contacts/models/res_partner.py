from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_ids = fields.One2many('partner.phone', 'partner_id', string='Phone Numbers')
