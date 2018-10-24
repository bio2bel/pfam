# -*- coding: utf-8 -*-

"""Constants for Bio2BEL PFAM."""

from bio2bel import get_data_dir

__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
]

VERSION = '0.0.1-dev'
MODULE_NAME = 'bio2bel_pfam'
DATA_DIR = get_data_dir(MODULE_NAME)