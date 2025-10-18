from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    """ユーザーモデル"""
    __tablename__ = 'users'
    
    # 主キー
    id = db.Column(db.Integer, primary_key=True)
    
    # ユーザー基本情報
    username = db.Column(db.String(100), nullable=False, comment='ユーザー名（氏名）')
    email = db.Column(db.String(120), unique=True, nullable=False, comment='メールアドレス（ログインID）')
    password_hash = db.Column(db.String(255), nullable=False, comment='パスワードハッシュ')
    
    # 権限管理
    user_role = db.Column(db.String(20), nullable=False, default='user', comment='ユーザー権限（admin/user）')
    is_active = db.Column(db.Boolean, default=True, nullable=False, comment='アクティブフラグ')
    
    # ログイン管理
    last_login = db.Column(db.DateTime, comment='最終ログイン日時')
    password_changed_at = db.Column(db.DateTime, default=datetime.utcnow, comment='パスワード変更日時')
    
    # タイムスタンプ
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, comment='作成日時')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False, comment='更新日時')
    
    def __init__(self, username, email, password, user_role='user'):
        """コンストラクタ"""
        self.username = username
        self.email = email
        self.set_password(password)
        self.user_role = user_role
    
    def set_password(self, password):
        """パスワードをハッシュ化して保存"""
        self.password_hash = generate_password_hash(password)
        self.password_changed_at = datetime.utcnow()
    
    def check_password(self, password):
        """パスワードを検証"""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """管理者権限を持つかチェック"""
        return self.user_role == 'admin'
    
    def update_last_login(self):
        """最終ログイン日時を更新"""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def to_dict(self):
        """辞書形式に変換（パスワードハッシュは除外）"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'user_role': self.user_role,
            'is_active': self.is_active,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def __repr__(self):
        return f'<User {self.email}>'