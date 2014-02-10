import sys

from flask import Flask, request, redirect, session, url_for, redirect, \
     render_template, abort, g, flash

from werkzeug import check_password_hash, generate_password_hash, secure_filename

## -----------------------------------------------------------------------------
## PROPS

CONFIG_FILE = 'config.json'

## -----------------------------------------------------------------------------
## INIT

app = Flask(__name__)
app.debug = True

## -----------------------------------------------------------------------------
## METHODS

def response_output(obj):
	return json.dumps(obj)

def load_data_from_string(json_string):
    return json.loads(json_string)

def load_data(relative_path):
    full_path = os.getcwd() + path_divider + relative_path
    return parse_models(full_path)
    
def parse_data(path):
    #print path
    data = None
    f = open(path,'r')
    data = json.loads(f.read())
    f.close()
    return data

def util_makepath(path):

    """ creates missing directories for the given path and
	returns a normalized absolute version of the path.

    - if the given path already exists in the filesystem
      the filesystem is not modified.

    - otherwise makepath creates directories along the given path
      using the dirname() of the path. You may append
      a '/' to the path if you want it to be a directory path.
    """

    from os import makedirs
    from os.path import normpath,dirname,exists,abspath

    dpath = normpath(dirname(path))
    if not exists(dpath): makedirs(dpath)
    return normpath(abspath(path))

## -----------------------------------------------------------------------------
## APP ##
	
@app.route('/<path:path>')
def route_path(path):
	context = {}
	context["settings"] = webAppSettings
	return render_template('main.htm', **context)

@app.route('/')
def route_root():
	context = {}
	context["settings"] = webAppSettings
	return render_template('main.htm', **context)

## -----------------------------------------------------------------------------
## ERRORS ##

@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist", 404

## -----------------------------------------------------------------------------
## DEV ##

if __name__ == '__main__':
	app.run(port=8080)