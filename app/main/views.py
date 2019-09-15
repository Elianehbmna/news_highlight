from flask import render_template
from . import main
from ..requests import get_sources,get_articles,search_news
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

@main.route('/search/<topic_news>')
def search(topic_news):
    '''
    View function to display the search results
    '''

    news_name_list = topic_news.split(' ')
    news_name_format = '+'.join(news_name_list)
    searched_topics = get_topic(news_name_format)
    title = f'search results for {topic_news}'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',topic_news = search_news))
    else:
        return render_template('search.html',news_topics = searched_topics, t =topic_news,title=title)
