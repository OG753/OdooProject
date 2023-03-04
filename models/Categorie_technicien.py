from odoo import models, fields
class ctechnicien(models.Model):
    _name='interventions.ctechnicien'
    _description='categories technicien'
    _rec_name='ct_libele'
    idCT=fields.Integer("identifiant")
    ct_libele=fields.Char("libele")
    ct_technicien=fields.One2many('interventions.technicien','idTech',string="technicien")
   
