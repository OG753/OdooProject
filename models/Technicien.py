from odoo import models, fields
class technicien(models.Model):
    _name='interventions.technicien'
    _description='technicien'
    idTech=fields.Integer("identifiant")
    tech_fname=fields.Char("prenom")
    tech_lname=fields.Char("nom")
    tech_telephone=fields.Char("Telephone")
    tech_ville=fields.Char("ville")
    tech_maintenance=fields.Many2many('interventions.maintenance', string="Reglage")
    tech_categorie=fields.Many2one('interventions.ctechnicien', string="Categorie")

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s %s" % (record.tech_lname,record.tech_categorie)
            result.append((record.id, rec_name))
        return result

    