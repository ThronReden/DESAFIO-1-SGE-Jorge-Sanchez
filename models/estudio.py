from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Estudio(models.Model):
    _name = 'modulo_desafio.estudio'
    _rec_name = 'nombre'
    
    _description = 'Estudio desarrollador'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del estudio desarrollador'
    )
    @api.constrains('nombre')
    def _check_nombre(self):
        for estudio in self:
            if not estudio.nombre.strip():
                raise ValidationError("El nombre del estudio no puede estar vacío.")
            if len(estudio.nombre) < 3:
                raise ValidationError("El nombre del estudio debe tener al menos 3 caracteres.")

    descripcion = fields.Text(
        string='Descripción',
        required=False,
        help='Descripción del estudio desarrollador'
    )

    logo = fields.Image(
        string='Logo',
        required=False,
        help='Logo del estudio desarrollador'
    )

    videojuego_ids = fields.One2many(
        comodel_name='modulo_desafio.videojuego',
        inverse_name='estudio_id',
        string='Videojuegos',
        help='Videojuegos desarrollados por este estudio',
    )