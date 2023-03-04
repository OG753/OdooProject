from odoo import models, fields
class fournisseur(models.Model):
    _name='interventions.fournisseur'
    _description='fournisseur'
    # _inherit = 'res.partner'
    idFournisseur=fields.Integer("identifiant")
    fournisseur_name=fields.Char("intitule")
    fournisseur_code=fields.Char("code")
    numero_telephone=fields.Char("telephone")
    fournisseur_adresse=fields.Char("adresse")
    fournisseur_region=fields.Char("region")
    code_postal=fields.Char("code postale")
    fournisseur_commande=fields.One2many('interventions.commande','idCommande',string='commandes')