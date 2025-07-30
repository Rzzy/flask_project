
import os

class Config:
  # 配置MYSQL参数
  MYSQL_DIALECT = 'mysql'
  MYSQL_DIRVER = 'pymysql'
  MYSQL_NAME = 'root'
  MYSQL_PWD = '1234'
  MYSQL_HOST = 'localhost'
  MYSQL_PORT = '3306'
  MYSQL_DB = 'flask_shop'
  MYSQL_CHARSET = 'utf8mb4'

  SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DIRVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
  SQLALCHEMY_TRACK_MODIFICATIONS = True

  SECRET_KEY = os.urandom(16)
  DEBUG = True

class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  DEBUG = False

config_map = {
  'develop': DevelopmentConfig,
  'product': ProductionConfig
}