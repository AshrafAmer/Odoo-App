from odoo import models, fields


class HmsDepartment(models.Model):
    _name = "hms.departments"
    _description = 'Hms departments details'
    name = fields.Char(help="Department Name")
    location = fields.Char(help="Department location inside hospital")
    is_opened = fields.Boolean()
    capacity = fields.Integer()
    patients_ids = fields.One2many(comodel_name="hms.patients", inverse_name="department_id")
