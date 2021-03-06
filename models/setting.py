# -*- coding: utf-8 -*-

import werobot.utils
from odoo import models, fields, api


class Setting(models.TransientModel):
    _name = 'wechat.settings'
    _inherit = 'res.config.settings'

    app_id = fields.Char('AppId', )
    app_secret = fields.Char('AppSecret', )
    enable_session = fields.Boolean('Enable Session', readonly=True)

    token = fields.Char('Token')
    access_token = fields.Char('Access Token')
    url = fields.Char('URL', readonly=True)
    
    @api.multi
    def set_app_id(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('app_id', config.app_id)

    @api.multi
    def set_app_secret(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('app_secret', config.app_secret)

    @api.multi
    def set_token(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('token', config.token)

    @api.multi
    def set_enable_session(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('enable_session', config.enable_session)

    @api.multi
    def set_url(self):
        """put wechat develop information into database"""
        self.ensure_one()
        config = self
        param = self.env["ir.config_parameter"]
        param.set_param('url', config.url)

    @api.model
    def get_default_app_id(self, fields):
        """get config information from database"""
        param = self.env["ir.config_parameter"]
        return {'app_id': param.get_param('app_id')}

    @api.model
    def get_default_app_secretd(self, fields):
        """get config information from database"""
        param = self.env["ir.config_parameter"]
        return {'app_secret': param.get_param('app_secret')}

    @api.model
    def get_default_token(self, fields):
        """get config information from database"""
        param = self.env["ir.config_parameter"]
        return {'token': param.get_param('token', default=werobot.utils.generate_token())}

    @api.model
    def get_default_url(self, fields):
        """get config information from database"""
        param = self.env["ir.config_parameter"]
        return {'url': param.get_param('url', default='/wechat')}

    @api.model
    def get_default_enable_session(self, fields):
        """get config information from database"""
        param = self.env["ir.config_parameter"]
        return {'enable_session': param.get_param('enable_session', default=True)}
