from flask import Blueprint, request, jsonify
import pymongo
from dotenv import load_dotenv
import os

data_resolver_bp = Blueprint('data_resolver', __name__)

load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')
# MongoDB 클라이언트 생성
client = pymongo.MongoClient(MONGO_URL)

# 'product_embedding_prev' 데이터베이스 가져오기 (없으면 생성)
db = client.get_database('product_embedding_prev') 

# 'product_data' 컬렉션 가져오기 (없으면 생성)
collection = db.get_collection('product_data')


# called by APIGATEWAY: bedrock Invokers -- json
@data_resolver_bp.route('/ai-api/bedrock/result/<int:productId>', methods=['POST'])
def data_resolve(productId):
    try:
        # 요청 데이터에서 JSON 데이터 가져오기
        data = request.get_json()

        # productId와 JSON 데이터를 MongoDB에 저장
        collection.insert_one({
            'productId': productId,
            'data': data
        })

        return jsonify({
            'message': 'Product data saved successfully',
            'productId': productId
            }), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
# called by APIGATEWAY: bedrock Invokers -- json
@data_resolver_bp.route('/ai-api/bedrock/result/<int:productId>', methods=['GET'])
def data_retrieve(productId):

    try:
        # productId를 이용하여 MongoDB에서 데이터 찾기
        product_data = collection.find_one({'productId': productId})

        if product_data:
            # 'data' 필드의 값을 가져옴
            data = product_data.get('data')
            return jsonify({
                'message': 'Product data retrieved successfully',
                'productId': productId,
                'data': data
            }), 200
        else:
            return jsonify({
                'message': 'Product data not found',
                'productId': productId
            }), 404

    except Exception as e:
        return jsonify({'message': str(e)}), 500