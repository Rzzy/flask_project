from time import sleep
from flask_shop.menu import menu,menu_api # 创建的user蓝图
from flask_shop import models, db
from flask import request
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg
from flask_shop.utils.token import generate_auth_token, login_required

class Menu(Resource):
  def get(self):
    menu_list = []
    mu = models.Menu.query.filter(models.Menu.level == 1).all()
    for m in mu:
      menu_list.append(m.to_dict())
    return to_dict_msg(200, data = menu_list)
  
menu_api.add_resource(Menu, '/menu')  
