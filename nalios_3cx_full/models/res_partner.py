# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re


class Partner(models.Model):
    _inherit = 'res.partner'

    phone_1 = fields.Char(unaccent=False, string="Phone 1")
    phone_format = fields.Char(compute='_get_formatted_numbers', store=True)
    phone_1_format = fields.Char(compute='_get_formatted_numbers', store=True)

    @api.depends('phone', 'phone_1')
    def _get_formatted_numbers(self):
        for partner in self:
            if partner.phone:
                partner.phone_format = re.sub('[^0-9]+', '', partner.phone)
            else:
                partner.phone_format = ''
            if partner.phone_1:
                partner.phone_1_format = re.sub('[^0-9]+', '', partner.phone_1)
            else:
                partner.phone_1_format = ''
