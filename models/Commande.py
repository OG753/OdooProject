from odoo import models, fields
class commande(models.Model):
    _name='interventions.commande'
    _description='commande'
    idCommande=fields.Integer("Cidentifiant")
    commande_libele=fields.Char("libele")
    commande_action=fields.Many2one('interventions.action', string='action')
    commande_equip=fields.One2many('interventions.equipement','idEquip',string='Equipements')
    commande_fournisseur=fields.Many2one('interventions.fournisseur',string='fournissuer')