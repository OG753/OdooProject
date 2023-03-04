from sqlite3 import apilevel
from sys import api_version
from odoo import models, fields
class reclamation(models.Model):
    _name="interventions.reclamation"
    _description="recalamtion"
    _rec_name='objet'
    idR=fields.Integer("idReclamation")
    objet=fields.Char("objet")
    date_reclamation=fields.Date("date")
    description=fields.Char("description")
    rec_responsable= fields.Many2one('interventions.responsable', string='responsbale')
    rec_intervention= fields.One2many('interventions.intervention','idI',string='interventions')
    state=fields.Selection([('envoye', 'Envoye'),
                            ('en cours de traitement', 'En cours de traitement'),
                            ('refuse', 'Refuse'),
                            ('accepte','Accepte'), ],string='state',default='envoye')
    
    def submitted_state(self):
        self.ensure_one()
        self.state='envoye'
    def accepted_state(self):
        self.ensure_one()
        self.state='accepte'
    def refused_state(self):
        self.ensure_one()
        self.state='refuse'
    def underReview_state(self):
        self.ensure_one()
        self.state='en cours de traitement'