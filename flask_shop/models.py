from flask_shop import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class baseModel:
  create_time = db.Column(db.DateTime, default = datetime.now)
  update_time = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

class User(db.Model, baseModel):
  __tablename__ = 't_user'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(32), unique = True, nullable = False)
  pwd = db.Column(db.String(200))
  nickName = db.Column(db.String(32))
  phone = db.Column(db.String(11))
  email = db.Column(db.String(32))

  @property
  def password(self):
    return self.pwd
  
  @password.setter
  def password(self, t_pwd):
    self.pwd = generate_password_hash(t_pwd)

  def check_password(self, t_pwd):
    return check_password_hash(self.pwd, t_pwd)
  
  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'nick_name': self.nickName,
      'phone': self.phone
    }
  
class Menu(db.Model):
  __tablename__ = 't_menu'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(32), unique = True, nullable = False)
  level = db.Column(db.Integer)
  path = db.Column(db.String(32))
  pid = db.Column(db.Integer, db.ForeignKey('t_menu.id'))
  children = db.relationship('Menu')

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'level': self.level,
      'path': self.path,
      'pid': self.pid,
      'children': self.get_child_list()
    }
  def get_child_list(self):
    object_child = self.children
    data = []
    for o in object_child:
      data.append(o.to_dict())

    return data

class Role(db.Model):
  __tablename__ = 't_role'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(32), unique = True, nullable = True)
  desc = db.Column(db.String(256))

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'desc': self.desc
    }