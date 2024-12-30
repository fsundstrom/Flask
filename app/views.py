import requests
import json
import re
import os
from requests.auth import HTTPBasicAuth
from flask import request, abort, render_template , Response, send_from_directory
from app import app
from app.forms import Form
  
####################################################################################
# Views                                                                            #
####################################################################################

# for fav icon
##########################
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# render form for imput
#########################
# defult page /
@app.route('/' , methods=['GET', 'POST'])
def index():
  # import form info
  form = Form()
  # if this is a responce get form data
  if request.method == 'POST' and form.validate():
     number = form.start.data
     return render_template('done.html', title='got_data', number=number, form=form)
  # if this is a get render basic page with form input
  return render_template('index.html', title='enter data', form=form)

####################################################################################
# Private methods, helpers and error handlers                                      #
####################################################################################

# demo so just have error handler here

@app.errorhandler(400)
def bad_request(error):
  return "Bad request: %s" % error, 400

