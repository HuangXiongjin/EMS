import json

from flask import Blueprint, request

from system_backend import autocode

system_set = Blueprint('system_set', __name__, template_folder='templates')


@system_set.route('/system_set/make_model', methods=['POST', 'GET'])
def make_model():
    if request.method == 'POST':
        data = request.values
        try:
            jsonstr = json.dumps(data.to_dict())
            return autocode.make_model_main(data)
        except Exception as e:
            print(e)
            # logger.error(e)
