# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json


class CustomAPIController(http.Controller):

    @http.route('/test', type='http', auth='none', methods=['GET', 'POST'], csrf=False)
    def test_endpoint(self, **kwargs):
        """Test endpoint that returns a success message"""
        response_data = {
            'status': 'success',
            'message': 'Success endpoint connection',
            'timestamp': str(request.env['ir.http']._get_default_lang().get('date_format', '%Y-%m-%d'))
        }
        
        return request.make_json_response(response_data)
