from flask import Blueprint
from flask_restful import Api

# 创建模块蓝图， 并添加url前缀 /user
user = Blueprint('user', __name__, url_prefix='/user')

# 使用restful，先用Api方法包裹
user_api = Api(user)
# 引入创建的模块
from flask_shop.user import view