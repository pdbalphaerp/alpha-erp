# -*- coding: utf-8 -*-

{
    'name': 'Appointment Google Calendar | Appointment Calender Sync | Appointment Calender',
    'version': '1.0',
    'category': 'Productivity',
    'summary': """This module integrates Odoo appointments with Google Calendar so you can easily attach a Google Meet videoconference link to any meeting you schedule for your clients. When creating or confirming an appointment, users can generate or select the corresponding Google Calendar event and automatically retrieve its Meet link, then share it with the customer via email, SMS, portal or any communication channel used in Odoo. The link is stored on the appointment record, making it simple for staff to find and resend, and ensuring both parties join the same virtual room at the right time. By centralizing video meeting details inside Odoo, this module streamlines remote appointments, reduces confusion about which link to use, and delivers a more professional online meeting experience.""",
    'depends': ['google_calendar', 'appointment'],
    'installable': True,

    'data': [
        'views/appointment_templates_validation.xml',
        'views/appointment_type_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ur_appointment_google_calendar/static/src/**/*',
        ],
    },
    'auto_install': True,
    'author': 'Technoverse Systems',
    'website': 'https://www.technoversesystems.com',
    'license': 'LGPL-3',
    'price': '149.40',
    'currency': 'USD',
    "images": ["static/description/appointment_calender.png", ],
}
