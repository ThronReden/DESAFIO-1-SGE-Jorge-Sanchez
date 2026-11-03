from odoo import models, fields

class Videojuego(models.Model):
    _name = 'modulo_desafio.videojuego'

    _description = 'Videojuego'

    nombre = fields.Char(
        string='Título',
        required=True,
        help='Nombre del videojuego'
    )

    logo = fields.Binary(
        string='Logo',
        required=False,
        help='Logo del videojuego'
    )

    descripcion = fields.Text(
        string='Descripción',
        required=False,
        help='Descripción del videojuego'
    )

    fecha_lanzamiento = fields.Date(
        string='Lanzamiento',
        required=True,
        help='Fecha de lanzamiento del juego'
    )

    estudio_id = fields.Many2One(
        comodel_name='modulo_desafio.estudio',
        string='Estudio',
        required=True,
        help='Estudio desarrollador del juego',
        ondelete='restrict',
    )