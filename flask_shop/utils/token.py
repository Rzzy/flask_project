from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app, request
from flask_shop.models import User
from flask_shop.utils.message import to_dict_msg
import functools

def generate_auth_token(uid):
  # 创建加密对象
  s = Serializer(current_app.config['SECRET_KEY'])
  # 生成token
  return s.dumps({'id': uid})

def verify_auth_token(token_str):
  # 创建解谜对象
  s = Serializer(current_app.config['SECRET_KEY'])

  try:
    data = s.loads(token_str, max_age=10)
  except Exception:
    return None
  usr = User.query.filter_by(id = data['id']).first()
  return usr


def login_required(view_func):
  functools.wraps(view_func) # 高级函数 防止参数丢失
  def verify_token(*arg, **kwargs):
    try:
      token = request.headers['token']
    except Exception: 
      return to_dict_msg(403)
    s = Serializer(current_app.config['SECRET_KEY'])
    try: 
      s.loads(token, max_age=10)
    except Exception:
      return to_dict_msg(403)
    return view_func(*arg, **kwargs)
  return verify_token