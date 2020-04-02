from odoo import models, fields


class HmsPatientLogHistory(models.Model):
    _name = "hms.log_history"
    _description = 'Hms Patient Log history'

    patient_id = fields.Many2one(comodel_name="hms.patients")
    description = fields.Char(help="Log Description")

    _columns = {
        'create_date': fields.Datetime('Date Created', readonly=True),
        'create_uid': fields.Many2one('res.users', 'by User', readonly=True),
    }

