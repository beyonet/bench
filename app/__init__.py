#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prototype By: author
"""
import os
from flask import Flask
from flask import render_template
from flask import request
import csv



def create_app(config_name=None):

    server = Flask(__name__)
    #server.config.from_object(app_config[config_name])
    #app_config[config_name].init_app(server) #What is happending here again?

    # Extensions
    #register_extensions(server)

    # Models
    #from models import ...

    # Blueprints
    register_blueprints(server)

    return server


def register_blueprints(server):

    from .bench import bench as bench_blueprint
    server.register_blueprint(bench_blueprint, url_prefix='/bench')
