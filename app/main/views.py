from flask import render_template
from . import main

# Views
@main.route('/source/<int:source_id>')
def index(source_id):

    '''
    View root page function that returns the index page and its data
    '''

    
    return render_template('source.html',id = source_id)