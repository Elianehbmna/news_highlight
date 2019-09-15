import os

class Config:
    SOURCE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    # SOURCE_API_KEY  = os.environ.get('SOURCE_API_KEY')
    print (os.environ.get('SOURCE_API_KEY'))
    SOURCE_API_KEY= '118648cf442841859bf02eef5e9af5e5'
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}