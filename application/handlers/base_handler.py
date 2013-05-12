
from google.appengine.api import users
from flask import render_template, g, request, redirect
from application import app, config
import logging



@app.before_request
def before_request():
    g.view_model = {
        'title': '',
        'title_prefix': config.app_name
    }
