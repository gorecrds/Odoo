# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course information'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)
    
    currency_id = fields.Many2one('res.currency', string='Currency',
                                 default=lambda self: 
                                  self.env.user.company_id.currency_id)
    
    base_price = fields.Float(string='Base price', default=0.00)
    
    additional_fee = fields.Float(string='Additional fee', default=10.00)
    
    total_price = fields.Float(string='Total price', readonly=True)
    
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        
        if self.base_price < 0:
            raise UserError('Base price cannot be negative.')
        
        self.total_price = self.base_price + self.additional_fee
    
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('Additional fees cannot be less than 10: %s' % record.additional_fee)