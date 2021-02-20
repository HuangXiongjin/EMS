import datetime
import json
import os
import socket

from flask import Flask, request
from flask_cors import CORS
from flask_login import LoginManager
from flask_restful import Api, Resource

from Equipment_backend.equipment_manage import equipment_management
from common.common_cuid import select, update, delete, insert
from common.system_model import db_session, User, RunLog
from database.connect_db import CONNECT_DATABASE
from system_backend.PermissionAssignment import permission_distribution
from system_backend.Role_management import role_management
from system_backend.account_auth import login_auth
from system_backend.user_manage import user_manager
from tools.handle import MyEncoder

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
api = Api(app)

CORS(app, supports_credentials=True)
app.register_blueprint(login_auth)
app.register_blueprint(permission_distribution)
app.register_blueprint(user_manager)
app.register_blueprint(role_management)
app.register_blueprint(equipment_management)


class CUIDList(Resource):
    def get(self):
        return select(request.values)

    def post(self):
        return insert(request.values)

    def put(self):
        return update(request.values)

    def delete(self):
        return delete(request.values)


api.add_resource(CUIDList, '/CUID')


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).filter_by(ID=int(user_id)).first()


@app.errorhandler(Exception)
def error_handler(e):
    """
    全局捕获异常
    :param e:捕获异常参数
    """
    db_session.rollback()
    re_path = request.path
    # re_func = request.url_rule.endpoint
    re_func = request.url_rule.endpoint.split('.')[1]
    re_method = request.method
    root_path = os.path.abspath(os.path.dirname(__file__))
    now_date = datetime.datetime.now().strftime('%Y%m%d')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # file_path = os.path.join(root_path, f'logs\\{now_date}.txt')
    ip = socket.gethostbyname(socket.gethostname())
    result = f"{now_time} -- {ip} -- {re_path} -- {re_func} -- {re_method} -- {str(e)} \n"
    print(result)
    # with open(file_path, 'a', encoding='utf-8') as f:
    #     f.write(result)
    # db_session.add(RunLog(OperateTime=now_time, IP=ip, User='user', Path=re_path, Func=re_func, Method=re_method, Error=str(e)))
    # db_session.commit()
    # db_session.close()
    return json.dumps({'code': '2000', '捕获异常详情': result}, cls=MyEncoder, ensure_ascii=False)


def main():
    # app.run(host='0.0.0.0')
    app.run()


if __name__ == '__main__':
    main()
