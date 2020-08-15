# -*- coding: utf-8 -*-
"""
Set up bench Blueprint
"""
from flask import Blueprint

bench = Blueprint('bench', __name__)

from . import views

#from models import *

#@bench.app_context_processor
#def inject_permissions():
#    return dict(Permission=Permission)
