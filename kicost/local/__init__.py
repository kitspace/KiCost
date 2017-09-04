# -*- coding: utf-8 -*-

__author__ = 'XESS Corporation'
__email__ = 'info@xess.com'

from . import local

from ..kicost import distributors
distributors.update(
    {
        'local': {
            'module': local,
            'scrape': 'web',
            'function': 'farnell',
            'label': 'Farnell',
            'order_cols': ['part_num', 'purch', 'refs'],
            'order_delimiter': ' '
        }
    }
)

