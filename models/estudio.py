from odoo import models, fields

class Estudio(models.Model):
    _name = 'modulo_desafio.estudio'
    
    _description = 'Estudio desarrollador'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del estudio desarrollador'
    )

    descripcion = fields.Text(
        string='Descripción',
        required=False,
        help='Descripción del estudio desarrollador'
    )

    logo = fields.Binary(
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