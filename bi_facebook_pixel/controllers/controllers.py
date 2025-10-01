# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import json
from odoo.http import request
import odoo.http as http
from odoo.http import request


class EmiproThemeBase(http.Controller):
	@http.route(['/get_pixel_id'], type='http', auth="public", website=True)
	def get_pixel_id(self):
		ResConfig = request.env['res.config.settings']
		default_values = ResConfig.sudo().default_get(list(ResConfig.fields_get()))
		if default_values['fb_pixel_id']:
			return json.dumps(default_values['fb_pixel_id'])
		else:
			return json.dumps(False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
