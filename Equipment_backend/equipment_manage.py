import json
import os
import base64

from MyQR import myqr
from flask import Blueprint, request, send_from_directory

from common.equipment_model import Equipment
from common.system_model import db_session, AreaMaintain
from tools.handle import MyEncoder

equipment_management = Blueprint('equipment_management', __name__)


def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


@equipment_management.route('/EquipmentTree', methods=['GET'])
def equipment_tree():
    """设备分类树操作"""
    if request.method == 'GET':
        factory = db_session.query(AreaMaintain).first()
        sql = "select Position from Equipment"
        parent_tags = db_session.execute(sql).fetchall()
        tags_list = set(item[0] for item in parent_tags)
        children = []
        i = 1
        for item in tags_list:
            # 通过一级节点获取所有对应节点下的值
            children2 = []
            children1 = {"id": i, "label": item, "children": children2}
            query_data = db_session.query(Equipment).filter_by(Position=item).all()
            # parent_tag2 = set(item.ParentTag for item in query_data)
            i += 1
            for data in query_data:
                rank2_data = {"id": data.EquipmentCode, "label": data.EquipmentName, "type": "设备"}
                children2.append(rank2_data)
            children.append(children1)
        tree = [{"label": factory.AreaName, "children": children}]
        return json.dumps({'code': '1000', 'msg': '成功', 'data': tree}, cls=MyEncoder, ensure_ascii=False)


@equipment_management.route('/qrcode', methods=['POST'])
def generate_qrcode():
    """生成二维码"""
    qr_name = request.values.get('EquipmentCode')
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(root_path, 'picture')
    # gif_path = os.path.join(root_path, 'picture\\niu.gif')
    myqr.run(words="http://www.baidu.com/", colorized=True, save_name=f'{qr_name}.png', save_dir=file_path)
    query_data = db_session.query(Equipment).filter_by(EquipmentCode=qr_name).first()
    file_path2 = os.path.join(root_path, f'picture\\{qr_name}.png')
    # file_path2 = os.path.join(root_path, f'picture\\TQ1001.png')
    data = return_img_stream(file_path2)
    query_data.QRCode = data
    db_session.commit()
    db_session.close()
    return json.dumps({'code': '1000', 'msg': '成功', 'data': data}, cls=MyEncoder, ensure_ascii=False)


@equipment_management.route('/upload_picture', methods=['POST', 'GET'])
def upload_picture():
    """上传设备图片"""
    EquipmentCode = request.values.get('EquipmentCode')
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(root_path, 'picture')
    if request.method == 'POST':
        file = request.files.get('file')
        ext = file.filename.split('.')[-1]
        file_name = EquipmentCode + '.' + ext
        file_full_path = os.path.join(root_path, f'picture\\{file_name}')
        file.save(file_full_path)
        data = db_session.query(Equipment).filter_by(EquipmentCode=EquipmentCode).first()
        data.Picture = file_name
        db_session.commit()
        db_session.close()
        return json.dumps({'code': '1000', 'msg': '成功', 'data': file_full_path}, cls=MyEncoder, ensure_ascii=False)
    if request.method == 'GET':
        data = db_session.query(Equipment).filter_by(EquipmentCode=EquipmentCode).first()
        return send_from_directory(file_path, data.Picture)


# @equipment_management.route('/avatar', methods=['GET'])
# def get_avatar():
#     # width = request.args.get('width', 200)
#     # height = request.args.get('height', 200)
#     #
#     # user = Users.query.get(user_id)
#     # filename = user.avatar
#     # pic_path = '%s_%s_%s.%s' % (filename.split('.')[0], width, height, filename.split('.')[-1])
#     #
#     # print(pic_path)
#     #
#     # root_path = get_root_path(current_app)
#     # filepath = os.path.join(root_path, current_app.config['UPLOAD_PATH'])
#     # print(filepath)
#     root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     file_path = os.path.join(root_path, 'picture')
#     pic_path = 'JX1001.png'
#     a = send_from_directory(file_path, pic_path)
#     # data = db_session.query(Equipment).filter_by(EquipmentCode="JX1001").first()
#     # data.Picture = a
#     # db_session.commit()
#     # db_session.close()
#
#     return json.dumps({'code': '1000', 'msg': '成功', 'data': a}, cls=MyEncoder, ensure_ascii=False)
