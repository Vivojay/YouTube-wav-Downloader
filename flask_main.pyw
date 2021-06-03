from flask import Flask, request, render_template
import logging
import click

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

@app.route('/')
def index():
    return render_template('disp_vid_thumbnails.html')
    # if you want to render a .html file, 
    # import render_template from flask and use 
    # render_template("index.html") here.

if __name__ == '__main__':
    app.debug = False
    app.run() #go to http://localhost:5000/ to view the page.
