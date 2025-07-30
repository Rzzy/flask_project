export FLASK_APP=app.py
# 执行一次，初始化迁移
#flask db init
# 生成表结构
flask db migrate -m "fist migrate bash"
# 映射数据库
flask db upgrade