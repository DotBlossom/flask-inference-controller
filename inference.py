from flask import Blueprint, request, jsonify



inference_bp = Blueprint('inference', __name__)

#private Callable Functions Set


@inference_bp.route('/ai-api/user/action/<int:userId>', methods=['POST']) 
def inference_invoke(userId):

    return 'a'