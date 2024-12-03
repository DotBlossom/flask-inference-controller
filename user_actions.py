from flask import Blueprint, request, jsonify



user_actions_bp = Blueprint('user_actions', __name__)


@user_actions_bp.route('/ai-api/user/action/<int:userId>', methods=['POST']) 
def get_user_actions(userId):

    return 'a'