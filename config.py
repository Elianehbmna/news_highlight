import os

class Config:
 SOURCE_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
#  ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
 SOURCE_API_KEY  = os.environ.get('SOURCE_API_KEY ')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}