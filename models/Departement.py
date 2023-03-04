from odoo import models, fields
class departement(models.Model):
    _name='interventions.departement'
    _description='departement'
    _rec_name='dep_libele'
    idD=fields.Integer("identifiant")
    dep_libele=fields.Char("libele")
    dep_code=fields.Char("code")
    dep_responsable= fields.Many2one('interventions.responsable', string='responsbale')