
from bottle import route, run, template, static_file
from os import listdir
from random import choice

IMG_DIR = "./static/images/"

@route('/')
def main():    
    img = choice(listdir(IMG_DIR))
    return template('./index.html', image=img)

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    run(
        host='0.0.0.0', port=5000, debug=True
    )
