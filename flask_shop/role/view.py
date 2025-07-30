from flask_shop.role import role,role_api # 创建的user蓝图
from flask_shop import models, db
from flask import request
from flask_restful import Resource, reqparse
import re
from flask_shop.utils.message import to_dict_msg

class Role(Resource):
  def get(slef):
    try:
      roles = models.Role.query.all()
      role_list = [role.to_dict() for role in roles]
      return to_dict_msg(200, role_list)
    except Exception:
      return to_dict_msg(500)
role_api.add_resource(Role, '/role')  
