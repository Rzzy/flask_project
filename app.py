from flask_shop import create_app, db
from flask_migrate import Migrate

app = create_app('develop')
migrate = Migrate(app, db)  # 无其他代码需要添加

if __name__ == '__main__':
  app.run()