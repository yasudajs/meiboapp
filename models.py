"""
データベースモデル定義
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ユーザーテーブル"""
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    user_role = db.Column(db.String(16), nullable=False)  # 'admin' or 'user'
    is_active = db.Column(db.Integer, nullable=False, default=1)
    last_login = db.Column(db.DateTime)
    password_changed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # リレーション
    contacts = db.relationship('Contact', backref='user', lazy=True)
    groups = db.relationship('Group', backref='user', lazy=True)
    
    # Flask-Loginで必要なメソッド
    def get_id(self):
        return str(self.user_id)
    
    def is_admin(self):
        return self.user_role == 'admin'


class Contact(db.Model):
    """連絡先テーブル"""
    __tablename__ = 'contacts'
    
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    employee_number = db.Column(db.String(16), nullable=False, unique=True)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name_kana = db.Column(db.String(64))
    first_name_kana = db.Column(db.String(64))
    department = db.Column(db.String(64))
    position = db.Column(db.String(64))
    birthday = db.Column(db.Date)
    notes = db.Column(db.String(1000))
    profile_image = db.Column(db.String(2000))
    is_favorite = db.Column(db.Integer, nullable=False, default=0)
    is_deleted = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # リレーション
    phones = db.relationship('ContactPhone', backref='contact', lazy=True, cascade='all, delete-orphan')
    emails = db.relationship('ContactEmail', backref='contact', lazy=True, cascade='all, delete-orphan')
    addresses = db.relationship('ContactAddress', backref='contact', lazy=True, cascade='all, delete-orphan')
    groups = db.relationship('ContactGroup', backref='contact', lazy=True, cascade='all, delete-orphan')


class ContactPhone(db.Model):
    """電話番号テーブル"""
    __tablename__ = 'contact_phones'
    
    phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.contact_id'), nullable=False)
    phone_type = db.Column(db.String(16))  # '社用携帯', '個人携帯', '自宅'
    phone_number = db.Column(db.String(20), nullable=False)


class ContactEmail(db.Model):
    """メールアドレステーブル"""
    __tablename__ = 'contact_emails'
    
    email_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.contact_id'), nullable=False)
    email_type = db.Column(db.String(16))  # '個人', '会社'
    email_address = db.Column(db.String(128), nullable=False)


class ContactAddress(db.Model):
    """住所テーブル"""
    __tablename__ = 'contact_addresses'
    
    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.contact_id'), nullable=False)
    address_type = db.Column(db.String(16))  # '自宅', '会社'
    postal_code = db.Column(db.String(10))
    prefecture = db.Column(db.String(8))
    city = db.Column(db.String(64))
    address1 = db.Column(db.String(128))
    address2 = db.Column(db.String(128))


class Group(db.Model):
    """グループテーブル"""
    __tablename__ = 'groups'
    
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    group_name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # リレーション
    contacts = db.relationship('ContactGroup', backref='group', lazy=True, cascade='all, delete-orphan')


class ContactGroup(db.Model):
    """連絡先グループ関係テーブル"""
    __tablename__ = 'contact_groups'
    
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.contact_id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'), primary_key=True)
    assigned_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
