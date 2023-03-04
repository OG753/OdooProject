from odoo import models,api, fields
class maintenance(models.Model):
    _name='interventions.maintenance'
    _description='maintenance'
    _rec_name='m_libele'
    idM=fields.Integer("Midentifiant")
    m_libele=fields.Char("libele",required='true')
    m_action=fields.Many2one('interventions.action', string='action')
    m_tech=fields.Many2many('interventions.technicien', string="Techniciens")
    m_equip_reparation=fields.Many2many('interventions.equipement',string='materiel a reparer', required='true')
    maintenance_f=fields.Many2one('interventions.fiche',string="fiche de maintenances")    