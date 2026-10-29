from odoo import models, fields

class Videojuego(models.Model):
    _name = 'modulo_desafio.videojuego'

    _description = 'Videojuego'

    nombre = fields.Char(
        string='Título',
        required=True,
        help='Nombre del videojuego'
    )

    fecha_lanzamiento = fields.Date(
        string='Lanzamiento',
        required=True,
        help='Fecha de lanzamiento del juego'
    )