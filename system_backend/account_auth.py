import json
from flask import Blueprint, request
from flask_login import login_user, current_user, LoginManager

import time
import datetime

# flask_login的初始化
# login_manager = LoginManager()
# login_manager.db_session_protection = 'strong'
# login_manager.login_view = 'login_auth.login'
from common.system_model import db_session, User
from tools.handle import MyEncoder

login_auth = Blueprint('login_auth', __name__, template_folder='templates')


@login_auth.route('/login', methods=['POST'])
def login():
    '''
    用户登陆认证
    :return:
    '''
    try:
        if request.method == 'POST':
            data = request.values
            WorkNumber = data.get('WorkNumber')
            password = data.get('Password')
            # 验证账户与密码
            user = db_session.query(User).filter_by(WorkNumber=WorkNumber).first()
            if user and (user.confirm_password(password) or user.Password == password):
                login_user(user)
                user.session_id = str(time.time())
                user.LastLoginTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                db_session.commit()
                return json.dumps({"code": "1000", "message": "登录成功"}, ensure_ascii=False)
            else:
                return json.dumps({"code": "2000", "message": "用户名密码错误"}, ensure_ascii=False)
    except Exception as e:
        print(e)
        db_session.rollback()
        # logger.error(e)
        return json.dumps([{"status": "Error:" + str(e)}], cls=MyEncoder, ensure_ascii=False)

