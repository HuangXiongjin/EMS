import json
import time

from flask import Blueprint, request
from flask_mail import Message, Mail

from run import app

a = Blueprint("wbrj", __name__)
# user_manager = Blueprint('user_manager', __name__)
mail = Mail(app)

def add_date(week, work_time):
    """
    递增预工作时间
    :param week: 工作周期
    :param work_time: 计划开始时间
    :return:
    """
    """递增周期"""
    time_array = time.strptime(work_time, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array))
    if week[1] == '周':
        new_time_stamp = time_stamp + 604800 * int(week[0])
        new_time_array = time.localtime(new_time_stamp)
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", new_time_array)
        return new_time
    elif week[1] == '月':
        new_time_stamp = time_stamp + 86400 * 30 * int(week[0])
        new_time_array = time.localtime(new_time_stamp)
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", new_time_array)
        return new_time
    elif week[1] == '年':
        new_time_stamp = time_stamp + 86400 * 365 * int(week[0])
        new_time_array = time.localtime(new_time_stamp)
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", new_time_array)
        return new_time


def get_time_stamp(work_time):
    """
    计算工作时间间隔
    :param work_time: 计划开始时间
    :return:
    """
    time_array = time.strptime(work_time, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array))
    # 倒数三天
    # return 0 < time_stamp - int(time.time()) < 259200
    # 倒数7天
    return 0 < time_stamp - int(time.time()) < 604800
    # 倒数47天
    # return 0 < time_stamp - int(time.time()) < 604800 * 7


def get_no(no):
    """自动生成工单号"""
    return str(str(str(no).replace('-', '')).replace(':', '')).replace(' ', '')


@a.route('/send_mail', methods=['GET'])
def email_send_charactor():
    # recipients = json.loads(request.values.get("mail"))
    recipients = ['2563814081@qq.com']
    message = Message("智能设备运维任务", sender="1975436224qq.com", recipients=recipients)
    message.body = '您有一份新的运维任务，详情登录系统查看'
    try:
        mail.send(message)
        return json.dumps({"code": "1000", "message": "发送成功，请注意查收~"})
    except Exception as e:
        print(e)
        return json.dumps({"code": "1001", "message": "发送失败，请检查邮箱格式是否正确！"})
