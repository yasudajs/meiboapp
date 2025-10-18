from flask import Blueprint, jsonify

contacts_bp = Blueprint('contacts', __name__)

@contacts_bp.route('/', methods=['GET'])
def get_contacts():
    """連絡先一覧取得"""
    # 仮のデータ
    contacts = [
        {
            'id': 1,
            'last_name': '田中',
            'first_name': '太郎',
            'last_name_kana': 'タナカ',
            'first_name_kana': 'タロウ',
            'email': 'tanaka@example.com',
            'department': '営業部',
            'position': '課長'
        },
        {
            'id': 2,
            'last_name': '佐藤',
            'first_name': '花子',
            'last_name_kana': 'サトウ',
            'first_name_kana': 'ハナコ',
            'email': 'sato@example.com',
            'department': '総務部',
            'position': '主任'
        }
    ]
    
    return jsonify({
        'status': 'success',
        'data': {
            'contacts': contacts,
            'pagination': {
                'current_page': 1,
                'total_pages': 1,
                'total_items': len(contacts),
                'items_per_page': 20
            }
        }
    })

@contacts_bp.route('/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    """連絡先詳細取得"""
    # TODO: データベースから取得
    return jsonify({
        'status': 'success',
        'data': {
            'id': contact_id,
            'last_name': '田中',
            'first_name': '太郎',
            'email': 'tanaka@example.com'
        }
    })

@contacts_bp.route('/', methods=['POST'])
def create_contact():
    """連絡先新規作成"""
    # TODO: 実装
    return jsonify({
        'status': 'success',
        'message': '連絡先が作成されました'
    }), 201