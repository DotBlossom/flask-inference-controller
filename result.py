from flask import Blueprint, request, jsonify
import pymongo
from dotenv import load_dotenv
import os

result_bp = Blueprint('result', __name__)
default_result_bp = Blueprint('default_result', __name__)

# .env 파일에서 MongoDB 연결 정보 로드
load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')

# MongoDB 클라이언트 생성
client = pymongo.MongoClient(MONGO_URL)
db = client['user_actions']  # 'user_actions' 데이터베이스 가져오기
collection = db['user_purchases']  # 'user_purchases' 컬렉션 가져오기

# 기본 preference 결과 ID (MongoDB에서 값을 가져오지 못할 경우 사용)
default_preference_result_id = [1, 2, 3, 4, 5]


@result_bp.route('/ai-api/preference/<int:userId>', methods=['GET'])
def result_preferences(userId):

    try:
        # MongoDB에서 사용자의 productIds 가져오기
        user_data = collection.find_one({'userId': userId})

        if user_data:
            # productIds를 preference 결과 ID로 사용
            preference_result_id = user_data.get('productIds', [])
        else:
            # 사용자 데이터가 없는 경우 기본 preference 결과 ID 사용
            preference_result_id = default_preference_result_id

        return jsonify({
            "user_preference_id": preference_result_id,
            "message" : "retrieve user-preference-ids"
        }, 200)

    except Exception as e:
        return jsonify({'message': str(e)}), 500


@default_result_bp.route('/ai-api/preference/default', methods=['GET'])
def default_result_preferences():

    return jsonify({
        "default_preference_id": default_preference_result_id,
    }, 200)