import json

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from database.connect_db import CONNECT_DATABASE

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_DATABASE
# 不跟踪修改，不设置会有警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库连接对象
db = SQLAlchemy(app)

# 绑定app和数据库，迁移使用
migrate = Migrate(app, db)

# 传输命令行参数
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/', methods=['GET'])
def start():
    return 'This EMS!'


def main():
    # manager.run()
    app.run()


if __name__ == '__main__':
    main()
