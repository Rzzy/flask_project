from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map

db = SQLAlchemy()
def create_app(config):
  app = Flask(__name__)
  config_obj = config_map[config]
  app.config.from_object(config_obj)
  db.__init__(app)
  # 引入蓝图，并注册
  from flask_shop.user import user
  app.register_blueprint(user)

  from flask_shop.menu import menu
  app.register_blueprint(menu)

  from flask_shop.role import role
  app.register_blueprint(role)
  return app