from datetime import datetime
from app import db

class Contact(db.Model):
    """連絡先モデル"""
    __tablename__ = 'contacts'
    
    # 主キー
    id = db.Column(db.Integer, primary_key=True)
    
    # 外部キー（ユーザーID - このレコードの所有者）
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment='ユーザーID')
    
    # 氏名情報
    last_name = db.Column(db.String(50), nullable=False, comment='姓')
    first_name = db.Column(db.String(50), nullable=False, comment='名')
    last_name_kana = db.Column(db.String(100), nullable=False, comment='姓フリガナ')
    first_name_kana = db.Column(db.String(100), nullable=False, comment='名フリガナ')
    
    # 連絡先情報
    email = db.Column(db.String(120), nullable=False, comment='メールアドレス')
    personal_phone = db.Column(db.String(20), comment='個人携帯番号')
    business_phone = db.Column(db.String(20), comment='業務携帯番号')
    
    # 勤務先情報
    department = db.Column(db.String(100), nullable=False, comment='部署名')
    position = db.Column(db.String(100), nullable=False, comment='役職')
    
    # 個人情報
    birthday = db.Column(db.Date, nullable=False, comment='生年月日')
    
    # 住所情報
    postal_code = db.Column(db.String(10), nullable=False, comment='郵便番号')
    prefecture = db.Column(db.String(20), nullable=False, comment='都道府県')
    city = db.Column(db.String(100), nullable=False, comment='市区町村')
    address1 = db.Column(db.String(200), nullable=False, comment='住所1（番地）')
    address2 = db.Column(db.String(200), comment='住所2（建物名等）')
    
    # その他情報
    notes = db.Column(db.Text, comment='備考')
    profile_image = db.Column(db.String(255), comment='プロフィール画像パス')
    
    # フラグ情報
    is_favorite = db.Column(db.Boolean, default=False, nullable=False, comment='お気に入りフラグ')
    is_deleted = db.Column(db.Boolean, default=False, nullable=False, comment='削除フラグ')
    
    # タイムスタンプ
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, comment='作成日時')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False, comment='更新日時')
    
    # リレーション
    user = db.relationship('User', backref=db.backref('contacts', lazy=True, cascade='all, delete-orphan'))
    
    # グループリレーション（多対多）
    groups = db.relationship('Group', secondary='contact_groups', backref=db.backref('contacts', lazy='dynamic'))
    
    def __init__(self, user_id, last_name, first_name, last_name_kana, first_name_kana, 
                 email, department, position, birthday, postal_code, prefecture, 
                 city, address1, **kwargs):
        """コンストラクタ"""
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.last_name_kana = last_name_kana
        self.first_name_kana = first_name_kana
        self.email = email
        self.department = department
        self.position = position
        self.birthday = birthday
        self.postal_code = postal_code
        self.prefecture = prefecture
        self.city = city
        self.address1 = address1
        
        # オプション項目
        self.address2 = kwargs.get('address2')
        self.personal_phone = kwargs.get('personal_phone')
        self.business_phone = kwargs.get('business_phone')
        self.notes = kwargs.get('notes')
        self.profile_image = kwargs.get('profile_image')
    
    @property
    def full_name(self):
        """フルネーム"""
        return f"{self.last_name} {self.first_name}"
    
    @property
    def full_name_kana(self):
        """フルネーム（フリガナ）"""
        return f"{self.last_name_kana} {self.first_name_kana}"
    
    @property
    def full_address(self):
        """完全住所"""
        address = f"{self.prefecture}{self.city}{self.address1}"
        if self.address2:
            address += f" {self.address2}"
        return address
    
    def soft_delete(self):
        """論理削除"""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()
    
    def restore(self):
        """削除の取り消し"""
        self.is_deleted = False
        self.updated_at = datetime.utcnow()
    
    def toggle_favorite(self):
        """お気に入りの切り替え"""
        self.is_favorite = not self.is_favorite
        self.updated_at = datetime.utcnow()
    
    def to_dict(self, include_sensitive=False):
        """辞書形式に変換"""
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'full_name': self.full_name,
            'last_name_kana': self.last_name_kana,
            'first_name_kana': self.first_name_kana,
            'full_name_kana': self.full_name_kana,
            'email': self.email,
            'department': self.department,
            'position': self.position,
            'is_favorite': self.is_favorite,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        
        # 詳細情報を含める場合
        if include_sensitive:
            data.update({
                'personal_phone': self.personal_phone,
                'business_phone': self.business_phone,
                'birthday': self.birthday.isoformat() if self.birthday else None,
                'postal_code': self.postal_code,
                'prefecture': self.prefecture,
                'city': self.city,
                'address1': self.address1,
                'address2': self.address2,
                'full_address': self.full_address,
                'notes': self.notes,
                'profile_image': self.profile_image
            })
        
        return data
    
    def __repr__(self):
        return f'<Contact {self.full_name} ({self.email})>'