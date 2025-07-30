status_map = {
  200: 'success',
  500: 'error',
  501: 'password error',
  502: 'name is empty',
  503: 'field list is note all',
  403: 'no login info'
}

def to_dict_msg(status = 200, data= None, msg = None):
  return {
    'status': status,
    'data': data,
    'msg': msg if msg else status_map.get(status)
  }