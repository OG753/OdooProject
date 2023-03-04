import base64
from odoo import models,api,fields
from odoo.exceptions import UserError, ValidationError
import io
from PIL import Image
import sys

class responsable(models.Model):
    _name='interventions.responsable'
    _description='responsable' 
    _inherits = {'res.partner': 'partner_id'}
    partner_id = fields.Many2one(
        'res.partner',
        ondelete='cascade',
        delegate=True,
    )
    _sql_constraints = [
        ('idResponsable', 'UNIQUE (idRes)',
           'ID doit être unique.')
        ]
    idRes=fields.Char("identifiant")
    res_fname=fields.Char("prenom")
    res_lname=fields.Char("nom")
    res_email=fields.Char("E-mail")
    res_telephone=fields.Char("Telephone")
    res_ville=fields.Char("ville")
    res_departement= fields.One2many('interventions.departement','idD',string='departement')
    res_reclamation= fields.One2many('interventions.reclamation','idR',string='reclamation')
    image = fields.Image(related='partner_id.image_1920')
    

    @api.constrains('image')
    def check_insert_image(self):
        if self.image:
            file_image = base64.b64decode(self.image)
            stream = io.BytesIO(file_image)
            img = Image.open(stream)
            width, height = img.size
            
            if width > 600 or height > 600:
                raise ValidationError(("You can't insert image with height or width more than 500 (500 x 500).\nHeight: %s \nWidth: %s" % (height, width)))
            
            image_size = sys.getsizeof(file_image) * 0.0009765625
            if image_size > 250:
                raise ValidationError(("You can't insert image with size more than 250 KB.\nSize: %s" % (image_size)))
        else:
            raise UserError(('You must include an Employee Image to be able to save this data.'))
    

