from flask import Blueprint, request, jsonify
import pymongo
from dotenv import load_dotenv
import os

user_actions_bp = Blueprint('user_actions', __name__)
load_dotenv()
#private Callable Functions Set

# MongoDB Atlas 연결 정보
MONGO_URL = os.getenv('MONGO_URL')
# MongoDB 클라이언트 생성
client = pymongo.MongoClient(MONGO_URL)

@user_actions_bp.route('/ai-api/user/action/<int:userId>', methods=['POST']) 
def get_user_actions(userId):

    try:
        # 요청 데이터에서 productIds 가져오기
        data = request.get_json()
        productIds = data.get('productIds', [])

        # productIds가 리스트가 아니거나 비어있는 경우 에러 반환
        if not isinstance(productIds, list) or not productIds:
            return jsonify({'message': 'Invalid productIds'}), 400

        # 'user_actions' 데이터베이스 가져오기 (없으면 생성)
        db = client['user_actions']

        # 'user_purchases' 컬렉션 가져오기 (없으면 생성)
        collection = db['user_purchases']

        # userId를 이용하여 document 찾기
        user_data = collection.find_one({'userId': userId})

        if user_data:
            # userId가 이미 존재하는 경우, productIds 업데이트
            collection.update_one(
                {'userId': userId},
                {'$addToSet': {'productIds': {'$each': productIds}}}
            )
        else:
            # userId가 없는 경우, 새로운 document 생성
            collection.insert_one({'userId': userId, 'productIds': productIds})
        
        return jsonify({
            "productIds" : productIds,
            "message" : "success to save Ids"
        }), 200


    except Exception as e:
        return jsonify({'message': str(e)}), 500