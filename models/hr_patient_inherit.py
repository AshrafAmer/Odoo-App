from odoo import models, fields, api
from odoo.exceptions import UserError


class HmsPatientLogHistory(models.Model):
    _inherit = "hr.employee"

    related_patient_id = fields.Integer()
    website = fields.Char()

    @api.constrains()
    def _check_email(self):
        for val in self:
            if self.env['hms.log_history'].search([('email', '=', val.work_email)]):
                raise UserError("This email is already exists. please ")

    @api.multi
    def unlink(self):
        for rec in self:
            if self.env['hms.log_history'].search([('email', '=', rec.work_email)]):
                raise UserError("You can't delete This Patient")
        super().unlink()
