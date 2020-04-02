# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HMS',
    'version': '1.1',
    'category': 'Open Source 40',
    'summary': 'ITI - Open Source 40 HMS',
    'description': "ITI - Open Source 40 HMS",
    'website': 'https://www.odoo.com',
    'depends': ['hr'],
    'data': [
        'security/group_security.xml',
        'security/ir.model.access.csv',
        'views/hms_patients_views.xml',
        'views/hms_patient_logs_views.xml',
        'views/hms_departments_views.xml',
        'views/hms_doctors_views.xml',
        'views/hr_patient_employee.xml',
        "report/hms_patients_template.xml",
        "report/report.xml",
    ]
}
