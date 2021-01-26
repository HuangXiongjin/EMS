import json

from flask import Flask
from flask_login import LoginManager

from common.system_model import db_session, User
from database.connect_db import CONNECT_DATABASE
from system_backend.account_auth import login_auth

app = Flask(__name__)

# 初始化 LoginManager
login_manager = LoginManager()
# 设为'strong'侦测IP地址和user-agent信息有无异常，有异常就退出
login_manager.session_protection = 'strong'
# 设置没有登录的信息
login_manager.login_message = False
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_DATABASE
# 不跟踪修改，不设置会有警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1qaz2wsx3edd45'

app.register_blueprint(login_auth)


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).filter_by(ID=int(user_id)).first()


@app.route('/', methods=['GET'])
def start():
    return 'This EMS!'


def main():
    app.run()


if __name__ == '__main__':
    main()
