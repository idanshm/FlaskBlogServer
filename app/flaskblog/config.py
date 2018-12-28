import json

with open('config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('APP_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get('SMTP_SERVER')
    MAIL_PORT = config.get('SMTP_PORT')
    MAIL_USE_TLS = config.get('USE_TLS')
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')

