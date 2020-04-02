from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError


class HmsPatients(models.Model):
    _name = "hms.patients"
    _description = 'Patients details management'
    first_name = fields.Char(help="Patient first name")
    last_name = fields.Char(help="Patient last name")
    birth_date = fields.Date(help="Patient Birth date")
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(selection=[('A+', 'A+'), ('B+', 'B+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-')],
                                  string='Blood Type')
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text(help="patient full address")
    age = fields.Integer(compute="_compute_age")
    email = fields.Char(help="Your Unique Email")
    state = fields.Selection(selection=[
        ('undetermined', 'Undetermined Yet'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')
    ], string="Patient State", default='undetermined')

    department_id = fields.Many2one(comodel_name="hms.departments")
    doctors_ids = fields.Many2many(comodel_name="hms.doctors")
    department_capacity = fields.Integer(related="department_id.capacity")
    logs = fields.One2many(comodel_name="hms.log_history", inverse_name="patient_id")

    _sql_constraints = [
        ('email', 'UNIQUE(email)', 'This Email already exists!. It must be unique')
    ]

    # Functions Area

    patient_states = {
        'undetermined': 'good',
        'good': 'fair',
        'fair': 'serious'
    }

    @api.multi
    def button_change_states(self):
        for rec in self:
            new_state = self.patient_states.get(rec.state)
            self.env['hms.log_history'].create({
                "patient_id": self.id,
                "description": f"chang patient state from {self.state} to {new_state}"
            })
            rec.state = new_state
            self.write({"state": rec.state})

    @api.onchange('age')
    def change_age_pcr(self):
        if self.age < 30:
            pcr_val = [('checked', '=', True)]
        else:
            pcr_val = []
        return {
            'domain': {'history': pcr_val},
            'warning': {
                'title': 'age change',
                'message': 'PCR has been checked!'
            }
        }

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = date.today().year - rec.birth_date.year
            else:
                raise UserError("Patient don't has a birth date")
