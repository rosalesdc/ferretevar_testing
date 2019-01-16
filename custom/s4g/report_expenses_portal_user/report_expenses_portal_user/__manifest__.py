# -*- coding: utf-8 -*-
{
    'name': "Report expenses from website",

    'summary':
        """
            * Create expenses form website with a portal user. \n
            * A expense can be related to a project.
        """,

    'description':
        """
            * A employee has a portal user, this user can report expenses it is related to a project.
            *When a expense register doesn't exist a user can create it from a field.
        """,

    'author': "Soluciones4G - OGM",
    'website': "www.soluciones4g.com",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'web',
        'website_form',
        'hr_expense',
        'project',
        'product'
    ],

    'demo': [],

    'data': [
        'views/expenses_reports_view.xml',
        'data/website_data.xml',
        'views/expense_inherit_view.xml',
        'views/project_inherit_view.xml',
        'static/src/xml/frontend_custom_assets.xml',
        'views/portal_templates.xml',
        'data/website_menuitems.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
