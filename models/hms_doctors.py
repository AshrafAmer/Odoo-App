from odoo import models, fields


class HmsDoctors(models.Model):
    _name = "hms.doctors"
    _description = 'Hms Doctors details'
    first_name = fields.Char(help="Doctor First Name")
    last_name = fields.Char(help="Doctor Last Name")
    image = fields.Binary(help="Doctor Profile 4 * 6")
    grade_year = fields.Date(help="Graduation Year")
    patients_ids = fields.Many2many(comodel_name="hms.patients")
    skills_ids = fields.Many2many("hms.skills")


class DoctorSkills(models.Model):
    _name = "hms.skills"
    name = fields.Char()
