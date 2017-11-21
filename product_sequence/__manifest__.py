# Non part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Products sequence',
    'category' : 'Sales',
    'depends' : ['sale', 'base'],
    'demo' : [],
    'author': 'Walter Ruiter',
    'website': 'http://www.Vintage-Electronics.nl',
    'license': 'AGPL-3',

    'description': """
this app adds a sequence to the products and puts it in the default code field


""",
    'data': [
        'data/ir_sequence_data.xml',
    ]
}
