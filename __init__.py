from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
def create_app(config_name):
   app = Flask(__name__)
   user_db = 'root'
   pass_db = 'sena'
   url_db = 'localhost'
   name_db = 'flask_alchemy'
   full_url_db = f'mysql://{user_db}:{pass_db}@{url_db}/{name_db}'
   app.config['SQLALCHEMY_DATABASE_URI'] = full_url_db
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   db = SQLAlchemy(app)

   migrate = Migrate()
   migrate.init_app(app, db)
   return app
