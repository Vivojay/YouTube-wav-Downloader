from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('disp_vid_thumbnails.html')
    #if you want to render a .html file, 
    # import render_template from flask and use 
    #render_template("index.html") here.

if __name__ == '__main__':
    app.debug = False
    app.run() #go to http://localhost:5000/ to view the page.
