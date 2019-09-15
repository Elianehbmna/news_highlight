from flask import render_template
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    # print(sources)
    title = "News Highlighter"
    return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/news/<id>')
def articles(id):
    '''
    view articles page
    '''
    print('test')
    print(id)
    articles = get_articles(id)
    # print(articles)
    title = f'NH | {id}'

    return render_template('articles.html',title= title,articles = articles)