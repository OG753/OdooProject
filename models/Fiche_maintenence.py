from odoo import models, fields
class fiche(models.Model):
    _name='interventions.fiche'
    _description='fiche maintenance'
    _rec_name='f_libele'
    idf=fields.Integer("Fidentifiant")
    f_libele=fields.Char("libele")
    f_tech=fields.Many2one('interventions.technicien', string="Techniciens")
    f_maintenance=fields.One2many('interventions.maintenance','idM',string="maintenance")
    