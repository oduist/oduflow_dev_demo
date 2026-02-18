from odoo import api, fields, models


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

    def _sync_partner_phone(self):
        for partner in self.mapped('partner_id'):
            first = partner.phone_ids[:1]
            partner.phone = first.phone if first else False

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._sync_partner_phone()
        return records

    def write(self, vals):
        res = super().write(vals)
        if 'phone' in vals or 'sequence' in vals:
            self._sync_partner_phone()
        return res

    def unlink(self):
        partners = self.mapped('partner_id')
        res = super().unlink()
        remaining = self.env['partner.phone'].search([('partner_id', 'in', partners.ids)], order='sequence, id', limit=1)
        for partner in partners:
            first = remaining.filtered(lambda p: p.partner_id == partner)[:1]
            partner.phone = first.phone if first else False
        return res
