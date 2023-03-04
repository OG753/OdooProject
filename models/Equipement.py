from odoo import models,api, fields
from odoo.exceptions import ValidationError
import json
class equipement(models.Model):
    _name='interventions.equipement'
    _description='equipement'
    _rec_name='equip_Libele'
    idEquip=fields.Integer("identifiant")
    equip_Libele=fields.Char("libele", required='true')
    equip_type=fields.Many2one('interventions.tequipement',string='type', required='true')
    equip_prix=fields.Float("prix unitaire",digits=(14,3))
    equip_Description=fields.Char("description")
    equip_active=fields.Selection([('bon', 'Bon'),
                            ('a maintenanir', 'A maintenanir'),
                            ('a remplacer', 'A remplacer'),],string='equip_etat',help="select state of equipement",required="true")
    equip_commande=fields.Many2one('interventions.commande',string='commande')
    equip_reparation=fields.Many2many('interventions.maintenance',string='Reparation')
    my_equip = fields.Integer(string='Number_maintainance',store=True,compute='_compute_number')
    my_groupby_equip=fields.Char(string='Equipement', compute='_compute_groupby_field')
   
    @api.constrains('equip_reparation')
    def _compute_groupby_field(self):
        for record in self:
            record.my_groupby_equip= ','.join(record.equip_reparation.mapped('m_libele'))


    @api.depends ('equip_reparation')
    def _compute_number(self): 
        x='a remplacer'
        for rec in self:	
          rec.my_equip = len(rec.equip_reparation)
          if int(rec.my_equip) > 10:
            rec.equip_active=x
                  
    # def get_type_equipment(self):
    #     res_types=[]
    #     self.env.cr.execute("SELECT DISTINCT equip_type FROM interventions_equipement WHERE equip_reparation IS NOT NULL")
    #     res_types= self.env.cr.fetchall()
    #     return res_types

    # def get_count(self):
    #     res_=equipement.get_type_equipment(self)
    #     st=[]
    #     for i in range(len(res_)):
    #        self.env.cr.execute("SELECT COUNT(*) FROM interventions_equipement WHERE equip_type='"+str(res_[i][0])+"'")
    #        st.append(self.env.cr.fetchone()[0])
    #     return st

    
           

       
