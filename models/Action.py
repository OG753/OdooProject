from odoo import models, fields
class action(models.Model):
    _name='interventions.action'
    _description='action'
    _rec_name='act_libele'
    idAct=fields.Integer("Aidentifiant")
    act_libele=fields.Char("libele")
    act_intervention=fields.Many2one('interventions.intervention',string='interventions')
    act_commande=fields.One2many('interventions.commande','idCommande',string='Commandes')
    act_maintenance=fields.One2many('interventions.maintenance','idM',string='Reparation')