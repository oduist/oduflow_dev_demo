from odoo import fields, models


class PartnerPhone(models.Model):
    _name = 'partner.phone'
    _description = 'Partner Phone Number'
    _order = 'sequence, id'

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    sequence = fields.Integer(default=10)
    label = fields.Selection(
        [
            ('mobile', 'Mobile'),
            ('work', 'Work'),
            ('home', 'Home'),
            ('fax', 'Fax'),
            ('other', 'Other'),
        ],
        default='mobile',
        required=True,
    )
    phone = fields.Char(required=True)
    note = fields.Char()
