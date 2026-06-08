# -*- coding: utf-8 -*-
{
    'name': "Elka Custom Changes",

    'summary': "Customizations for Elka",

    'description': """
    Customizations for Elka
    """,

    'author': "Techthings Limited",
    'website': "https://www.techthings.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    # ASSETS 

    # 'assets':{
    #     # assets for backend 
    #     'web.assets_backend': [
    #          'name_of_your_module/static/src/**/*'
    #     ],

    #     # # assets for frontend
    #      'web.assets_frontend': [
    #        'name_of_your_module/static/src/**/*'
    #     ],

    #     # your custom asset bundles
    #     'name_of_your_module.assets':[
    #         'name_of_your_module/static/src/**/*'
    #     ]
    # },

    # END OF ASSETS
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

