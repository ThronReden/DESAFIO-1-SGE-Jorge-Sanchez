from odoo import models, fields

class Departamento(models.Model):
    _name = 'modulo_desafio.departamento'
    
    _description = 'Departamento'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del departamento'
    )

    descripcion = fields.Text(
        string='Descripción',
        help='Descripción del departamento'
    )

    jefe_departamento_id = fields.One2one(
        comodel_name='modulo_desafio.empleado',
        string='Jefe del Departamento',
        required=True,
        help='Empleado que lidera el departamento',
        ondelete='restrict',
    )

    empleados_ids = fields.One2many(
        comodel_name='modulo_desafio.empleado',
        reverse_name='departamento_id',
        string='Empleados',
        help='Empleados que pertenecen a este departamento',
    )