from flask import Blueprint, request, jsonify



result_bp = Blueprint('result', __name__)
default_result_bp = Blueprint('default_result', __name__)

#private Callable Functions Set
preference_result_id = [1,2,3,4,5];

## mongoAtlasCaller : if has kinda usrid?



@result_bp.route('/ai-api/preference/<int:userId>', methods=['GET']) 
def result_preferences(userId):

    return jsonify({
        "user_preference_id" : preference_result_id,
    }, 200)

@default_result_bp.route('/ai-api/preference/default', methods=['GET']) 
def default_result_preferences():
    
    return jsonify({
        "default_preference_id" : preference_result_id,
    }, 200)
