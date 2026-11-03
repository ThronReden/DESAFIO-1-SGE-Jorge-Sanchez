from odoo import models, fields

class Empleado(models.Model):
    _name = 'modulo_desafio.empleado'
    
    _description = 'Empleado'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del empleado'
    )

    apellidos = fields.Char(
        string='Apellidos',
        required=True,
        help='Apellidos del empleado'
    )

    email = fields.Char(
        string='Email',
        required=True,
        help='Email del empleado'
    )

    departamento_id = fields.Many2one(
        comodel_name='modulo_desafio.departamento',
        string='Departamento',
        required=True,
        help='Departamento al que pertenece el empleado',
        ondelete='restrict',
    )