{
'name': 'Intervention',
'summary': "Gestion des interventions",
'description': """
        Gestion des interventions
        ==============
        """,
  'author': "Equipe GL",
  'website': "https.intervention.com",
  'category': 'Uncategorized',
  'version': '1.0',
  'sequence':0,
  'depends': ['mail'],
  'data': ['views/intervention.xml','views/reclamation.xml','views/action.xml','views/type_intervention.xml',
   'views/commande.xml','views/fournisseur.xml','views/maintenance.xml','views/fiche.xml','views/technicien.xml',
   'views/categorie_technicien.xml','views/equipement.xml','views/type_equipement.xml','views/facture.xml',
   'views/departement.xml','views/responsable.xml','security/groups.xml','security/ir.model.access.csv','reports/fiche_maintenance_report.xml',
   'reports/reclamation_report.xml'
   ],
   'demo': ['mail','contacts'],
   'installable': True,
   'application': True,
   'license': 'LGPL-3',
}