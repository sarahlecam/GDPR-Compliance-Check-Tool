from flask import jsonify, request, current_app
from functools import wraps
from itsdangerous import URLSafeTimedSerializer

def has_cookie():
    '''return true/false for cookie in session'''

    if 'CheckMateCookie' in request.cookies:
        # unserialize cookie payload and verify it's "good" (not expired, etc)
        key = current_app.config['SECRET_KEY']
        serializer = URLSafeTimedSerializer(secret_key = key)
        payload = request.cookies.get('CheckMateCookie')
        try:
            serializer.loads(payload, max_age = (30*60)) # 30 minutes is max time you can be logged in
            return True
        except:
            print("didnt work")
            print(serializer.loads(payload, max_age = (30*60)))
            return False
    return False

def require_cookie(fn):
    '''builds a wrapped function that short circuits if you have no cookie'''
    @wraps(fn)
    def decorated(*args, **kwargs):
        # if you don't have a cookie, return bad response
        if not has_cookie():
            r = jsonify({'Login error': 'Bad or missing user cookie'})
            r.status_code = 401
            return r

        # TODO: put company_id into flask session

        # return original response
        return fn(*args, **kwargs)
    return decorated
