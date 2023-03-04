from odoo import models, fields
class facture(models.Model):
    _name='interventions.facture'
    _description='facture'
    idfacture=fields.Integer("Facture identifiant")
    facture_libele=fields.Char("libele")
    Duree_garantie=fields.Integer("duree garantie")
    date_achat=fields.Date("date d'achat")