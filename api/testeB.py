from flask import Blueprint

bp = Blueprint('testeb', __name__)

@bp.route('/hello', methods=['GET'])
def hello():
    return "HelloB!"