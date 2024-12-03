from flask import Blueprint, request, jsonify



result_bp = Blueprint('result', __name__)


@result_bp.route('/ai-api/preference/<int:userId>', methods=['GET']) 
def result_preferences(userId):
    
    return 'a'