from time import sleep
from flask_shop.user import user,user_api # 创建的user蓝图
from flask_shop import models, db
from flask import request
from flask_restful import Resource, reqparse
import re
from flask_shop.utils.message import to_dict_msg
from flask_shop.utils.token import generate_auth_token, login_required

# restful 定义接口
class User(Resource):
  def get(self):
    try:
      id = int(request.args.get('id').strip())
      usr = models.User.query.filter_by(id = id).first()
      return to_dict_msg(200, data = usr.to_dict())
    except Exception:
      return to_dict_msg(500)
  def post(Resource):
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    nick_name = request.form.get('nick_name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    confirm_pwd = request.form.get('confirm_pwd')
    pwd = request.form.get('pwd') 
    # 验证数据
    if not all([name, pwd]):
      return to_dict_msg(503)
    if pwd != confirm_pwd:
      return to_dict_msg(501)
    if not re.match(r'1[345678]\d{9}',phone):
      return to_dict_msg(500)
    usr = models.User(name = name, password = pwd, nickName = nick_name, phone = phone, email = email)
    
    try: 
      db.session.add(usr)
      db.session.commit()
    except Exception:
      print("发生了异常：", Exception)
      return to_dict_msg(500, '', Exception)
    return {
      'status': 200,
      'msg': 'success'
    }
  def put(self):
    try: 
      id = int(request.form.get('id').strip())
      usr = models.User.query.get(id)
      name = request.form.get('name') if request.form.get('name') else usr.name
      nick_name = request.form.get('nick_name') if request.form.get('nick_name') else usr.nickName
      phone = request.form.get('phone') if request.form.get('phone') else usr.phone
      email = request.form.get('email') if request.form.get('email') else usr.email
      
      if usr:
        usr.name = name
        usr.nickName = nick_name
        usr.phone = phone
        usr.email = email
        db.session.commit()
      else:
        to_dict_msg(200, 'not find this user')
      return to_dict_msg(200)
    except Exception:
      to_dict_msg(500)
  def delete(self):
    id = int(request.form.get('id').strip())
    usr = models.User.query.get(id)
    if usr:
      db.session.delete(usr)
      db.session.commit
user_api.add_resource(User, '/user')

class UserList(Resource):
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, location = 'args')
    parser.add_argument('curPage', type=int, location = 'args')
    parser.add_argument('pageSize', type=int, location = 'args')

    try:
      args = parser.parse_args()
      name = args.get('name')
      curPage = args.get('curPage') if args.get('curPage') else 1
      pageSize = args.get('pageSize') if args.get('pageSize') else 5 
      if name:
        user_list = models.User.query.filter(models.User.name.like(f'%{name}%')).paginate(page = curPage, per_page=pageSize)
      else:
        user_list = models.User.query.paginate(page = curPage, per_page=pageSize)
      return to_dict_msg(200, data = {
        'cur': curPage,
        'pageSize': pageSize,
        'total':user_list.total,
        'data': [u.to_dict() for u in user_list.items]
      })
    except Exception as e:
      print(e)
      return to_dict_msg(500)

user_api.add_resource(UserList, '/user_list')

@user.route('/login', methods = ['POST'])
def login():
  name = request.form.get('name')
  pwd = request.form.get('pwd')

  if not all([name, pwd]):
    return { 'status': 10000, 'msg': '数据不完整'}
  if len(name) > 1:
    usr = models.User.query.filter_by(name =name).first()
    if usr:
      if usr.check_password(pwd):
        token = generate_auth_token(usr.id)
        return to_dict_msg(200, data = {
          'token': token 
        })
  return { 'status': 500, 'msg': 'error'}

@user.route('/test')
@login_required
def test_token():
  return to_dict_msg(200)