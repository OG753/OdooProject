from odoo import models, api,fields
from odoo.exceptions import ValidationError
from datetime import datetime,timedelta,date
class intervention(models.Model):
    _name='interventions.intervention'
    _description='intervention'
    _rec_name='idI'
    idI=fields.Char("identifiant")
    date_debut=fields.Date("date debut", required=True)
    date_fin=fields.Date("date fin")
    duree=fields.Integer("duree", compute='_compute_duree')
    priority=fields.Selection([('haute', 'Haute'),
                            ('moyenne', 'Moyenne'),
                            ('faible', 'Faible'),],string='etat',help="select reclamation priority")
    etat=fields.Selection([('en cours', 'En cours'),
                            ('terminée', 'Terminée'),
                            ('annulée', 'annulée'),],string='etat',default='en cours')
    intervention_reclamation=fields.Many2one('interventions.reclamation', string='reclamation')
    intervention_type=fields.Many2one('interventions.tintervention', string='type')
    intervention_action=fields.One2many('interventions.action','idAct',string='Actions')
    _sql_constraints = [
        ('idintervention', 'UNIQUE (idI)',
           'ID doit être unique.')
        ]
    def encours_state(self):
        self.ensure_one()
        self.etat='en cours'
    def ter_state(self):
        self.ensure_one()
        self.etat='terminée'
    def ann_state(self):
        self.ensure_one()
        self.etat='annulée'

    @api.constrains('date_fin')
    def _check_date_fin(self):
       for record in self:
          if record.date_debut >= record.date_fin:
             raise models.ValidationError('Les dattes saisies ne sont pas correctes ! ')
    @api.constrains('date_debut','date_fin')
    def _compute_duree(self):
        for record in self:
            if record.date_fin:
                delta=record.date_fin-record.date_debut
                record.duree=delta.days
