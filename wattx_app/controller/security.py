from flask import jsonify, request
from functools import wraps

def has_cookie():
    '''return true/false for cookie in session'''
    if 'company_id' in request.cookies:
        return True
    return False

def require_cookie(fn):
    '''builds a wrapped function that short circuits if you have no cookie'''
    @wraps(fn)
    def decorated(*args, **kwargs):
        # if you don't have a cookie, return bad response
        if not has_cookie():
            r = jsonify({'Login error': 'no user cookie'})
            r.status_code = 400
            return r

        # return original response
        return fn(*args, **kwargs)
    return decorated
