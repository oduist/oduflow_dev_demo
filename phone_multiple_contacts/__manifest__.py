{
    'name': 'Multiple Phone Contacts',
    'version': '18.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Allow multiple phone numbers per partner',
    'description': """
        Adds the ability to store multiple phone numbers for a contact.
        Each phone number can have a label (e.g. Work, Home, Fax).
    """,
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_phone_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
