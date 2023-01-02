# -*- coding: utf-8 -*-
# © <2016> <Cristian Salamea>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner for Ecuador',
    'version': '10.0.0.0.0',
    'category': 'Localization',
    'author': 'Cristian Salamea',
    'website': 'www.prisehub.com',
    'license': 'AGPL-3',
    'data': [
        'view/partner_view.xml',
        'data/partner.xml'
    ],
    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': ['stdnum']
    },
    'installable': True,
}
