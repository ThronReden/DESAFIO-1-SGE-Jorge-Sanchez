from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Videojuego(models.Model):
    _name = 'modulo_desafio.videojuego'
    _rec_name = 'nombre'

    _description = 'Videojuego'

    nombre = fields.Char(
        string='Título',
        required=True,
        help='Nombre del videojuego'
    )
    @api.constrains('nombre')
    def _check_nombre(self):
        for record in self:
            if not record.nombre.strip():
                raise ValidationError('El nombre no puede estar vacío.')

    logo = fields.Image(
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

    estudio_id = fields.Many2one(
        comodel_name='modulo_desafio.estudio',
        string='Estudio',
        required=True,
        help='Estudio desarrollador del juego',
        ondelete='restrict',
    )

    precio = fields.Float(
        string='Precio',
        required=True,
        digits=(10, 2),
        help='Precio del juego'
    )
    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 0:
                raise ValidationError('El precio no puede ser negativo.')

    descuento = fields.Float(
        string='Descuento (%)',
        required=False,
        digits=(5, 2),
        help='Descuento del juego'
    )
    @api.constrains('descuento')
    def _check_descuento(self):
        for record in self:
            if record.descuento < 0 or record.descuento > 100:
                raise ValidationError('El descuento debe estar entre 0 y 100.')

    precio_final = fields.Float('Precio final', digits=(10, 2), compute='_compute_precio_final')
    @api.depends('precio', 'descuento')
    def _compute_precio_final(self):
        for record in self:
            if record.descuento:
                # Aplicar el descuento al precio, si hay
                record.precio_final = record.precio * (1 - record.descuento / 100)
            else:
                record.precio_final = record.precio