import json

from flask import Flask
from flask_mail import Message, Mail

mail = Mail()
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='1975436224@qq.com',
    MAIL_PASSWORD='uqtwjtaxscijcibb',
    MAIL_DEBUG=True
)
mail.init_app(app)


def email_send_charactor():
    # recipients = json.loads(request.values.get("mail"))
    with app.app_context():
        recipients = ['2563814081@qq.com']
        message = Message("智能设备运维任务", sender="1975436224@qq.com", recipients=recipients)
        message.body = '您有一份新的运维任务，详情登录系统查看'
        try:
            mail.send(message)
            return json.dumps({"code": "1000", "message": "发送成功，请注意查收~"})
        except Exception as e:
            print(e)
            return json.dumps({"code": "1001", "message": "发送失败，请检查邮箱格式是否正确！"})


if __name__ == '__main__':
    email_send_charactor()
    print('发送完毕')
