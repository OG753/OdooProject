from odoo import models, fields
class tintervention(models.Model):
    _name='interventions.tintervention'
    _description='types interventions'
    _rec_name='ti_libele'
    idTI=fields.Integer("TI identifiant")
    ti_libele=fields.Char("libele")
    type_intervention=fields.One2many('interventions.intervention','idI',string='interventions')