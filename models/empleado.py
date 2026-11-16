from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'modulo_desafio.empleado'
    
    _description = 'Empleado'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del empleado'
    )
    @api.constrains('nombre')
    def _check_nombre(self):
        for record in self:
            if not record.nombre.strip():
                raise ValidationError('El nombre no puede estar vacío.')

    apellidos = fields.Char(
        string='Apellidos',
        required=True,
        help='Apellidos del empleado'
    )
    @api.constrains('apellidos')
    def _check_apellidos(self):
        for record in self:
            if not record.apellidos.strip():
                raise ValidationError('Los apellidos no pueden estar vacíos.')

    fecha_nacimiento = fields.Date(
        string='Fecha de nacimiento',
        required=True,
        help='Fecha de nacimiento del empleado'
    )
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento > fields.Date.today():
                raise ValidationError('La fecha de nacimiento no puede ser futura.')

    email = fields.Char(
        string='Email',
        required=True,
        help='Email del empleado'
    )

    salario = fields.Float(
        string='Salario',
        required=True,
        help='Salario del empleado'
    )
    @api.constrains('salario')
    def _check_salario(self):
        for record in self:
            if record.salario < 0:
                raise ValidationError('El salario no puede ser negativo.')

    departamento_id = fields.Many2one(
        comodel_name='modulo_desafio.departamento',
        string='Departamento',
        help='Departamento al que pertenece el empleado',
        ondelete='restrict',
    )