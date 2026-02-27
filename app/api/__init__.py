from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'flask-api'}), 200

@api_bp.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Flask API is running'}), 200
