{
    'name': "modulo_desafio",
    'summary': "Modulo para el desafio 1 de SGE de Jorge Sanchez",
    'description': "Tarea de clase - Jorge Sanchez",
    'website': "https://thronreden.github.io/",
    'category': "Tools", # Preliminar
    'version': "0.1",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/videojuego_views.xml',
        'views/estudio_views.xml',
    ],
    'instalable': True,
    'application': True,
    'demo': [ 'demo.xml' ],
}