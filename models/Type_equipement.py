from odoo import models, fields
class tequipement(models.Model):
    _name='interventions.tequipement'
    _description='types equipement'
    _rec_name='te_libele'
    idTE=fields.Integer("TE identifiant")
    te_libele=fields.Char("libele")
    te_equip=fields.One2many('interventions.equipement','idEquip',string='Equipements')