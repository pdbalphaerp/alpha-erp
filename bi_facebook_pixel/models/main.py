# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError



class FacebookPixelSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    fb_pixel_id = fields.Char(string = 'Facebook Fixel ID')

    @api.model
    def get_values(self):
        res = super(FacebookPixelSettings, self).get_values()
        res['fb_pixel_id'] = self.env['ir.config_parameter'].sudo().get_param("bi_facebook_pixel.fb_pixel_id", default="")
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param("bi_facebook_pixel.fb_pixel_id", self.fb_pixel_id or '')
        super(FacebookPixelSettings, self).set_values()


class FacebookPixelIntegrationID(models.AbstractModel):
    _inherit = 'ir.http'


    def check_fb_pixel_id(self, **kw):
        ResConfig = self.env['res.config.settings']
        default_values = ResConfig.default_get(list(ResConfig.fields_get()))
        return default_values['fb_pixel_id']

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
