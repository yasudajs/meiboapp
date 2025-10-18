from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """ログインエンドポイント"""
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({
            'status': 'error',
            'message': 'メールアドレスとパスワードが必要です'
        }), 400
    
    # TODO: ユーザー認証の実装
    # 仮の認証（開発時のみ）
    if data['email'] == 'admin@example.com' and data['password'] == 'password123':
        access_token = create_access_token(identity=data['email'])
        return jsonify({
            'status': 'success',
            'data': {
                'access_token': access_token,
                'user': {
                    'email': data['email'],
                    'role': 'admin'
                }
            }
        })
    
    return jsonify({
        'status': 'error',
        'message': '認証に失敗しました'
    }), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """ログアウトエンドポイント"""
    return jsonify({
        'status': 'success',
        'message': 'ログアウトしました'
    })

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    """現在のユーザー情報取得"""
    # TODO: JWT認証の実装
    return jsonify({
        'status': 'success',
        'data': {
            'user': {
                'email': 'admin@example.com',
                'role': 'admin'
            }
        }
    })