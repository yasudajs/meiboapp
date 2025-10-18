from datetime import datetime
from app import db

class Group(db.Model):
    """グループモデル"""
    __tablename__ = 'groups'
    
    # 主キー
    id = db.Column(db.Integer, primary_key=True)
    
    # 外部キー
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment='ユーザーID')
    
    # グループ情報
    group_name = db.Column(db.String(100), nullable=False, comment='グループ名')
    description = db.Column(db.Text, comment='説明')
    
    # タイムスタンプ
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, comment='作成日時')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False, comment='更新日時')
    
    # リレーション
    user = db.relationship('User', backref=db.backref('groups', lazy=True))
    
    def __init__(self, user_id, group_name, description=None):
        """コンストラクタ"""
        self.user_id = user_id
        self.group_name = group_name
        self.description = description
    
    def to_dict(self):
        """辞書形式に変換"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'group_name': self.group_name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Group {self.group_name}>'


# 連絡先とグループの多対多の関連テーブル
contact_groups = db.Table('contact_groups',
    db.Column('contact_id', db.Integer, db.ForeignKey('contacts.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
    db.Column('assigned_at', db.DateTime, default=datetime.utcnow, nullable=False, comment='割り当て日時')
)

# Contactモデルにグループリレーションを追加（models/contact.pyに後で追加する必要がある）