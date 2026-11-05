from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Departamento(models.Model):
    _name = 'modulo_desafio.departamento'
    
    _description = 'Departamento'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del departamento'
    )
    @api.constrains('nombre')
    def _check_nombre(self):
        for record in self:
            if not record.nombre.strip():
                raise ValidationError("El nombre del departamento no puede estar vacío.")

    descripcion = fields.Text(
        string='Descripción',
        help='Descripción del departamento'
    )

    jefe_id = fields.Many2one(
        comodel_name='modulo_desafio.empleado',
        string='Jefe del Departamento',
        help='Empleado que lidera el departamento',
        ondelete='set null',
    )

    empleado_ids = fields.One2many(
        comodel_name='modulo_desafio.empleado',
        inverse_name='departamento_id',
        string='Empleados',
        help='Empleados que pertenecen a este departamento',
    )