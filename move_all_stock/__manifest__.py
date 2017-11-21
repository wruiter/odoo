# Non part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Move All Stock',
    'category' : 'Warehouse',
    'depends' : ['base','stock'],
    'demo' : [],
    'author': 'Walter Ruiter',
    'website': 'http://www.Vintage-Electronics.nl',
    'license': 'AGPL-3',

    'description': """
Makes it possible to move the current stock from multiple location to one new location.
======================================================

It is possible to select multiple products and multiple source locations:
-------------------------------
  

""",
    'data': [
        'views/stock_quant.xml',
    ]
}
