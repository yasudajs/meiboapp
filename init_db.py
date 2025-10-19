"""
データベース初期化とテストデータ投入スクリプト
"""
import os
from datetime import datetime, date
from werkzeug.security import generate_password_hash
from app import app
from models import db, User, Contact, ContactPhone, ContactEmail, ContactAddress, Group, ContactGroup


def init_database():
    """データベースの初期化"""
    # データベースファイルのパス
    db_path = os.path.join(os.path.dirname(__file__), 'meiboapp.db')
    
    # 既存のデータベースファイルがあれば削除
    if os.path.exists(db_path):
        print(f"既存のデータベースを削除: {db_path}")
        os.remove(db_path)
    
    # テーブル作成
    with app.app_context():
        db.create_all()
        print("データベーステーブルを作成しました")


def create_test_users():
    """テストユーザーの作成"""
    with app.app_context():
        # 管理者ユーザー1
        admin1 = User(
            username="山田太郎",
            email="yamada.taro@example.com",
            password_hash=generate_password_hash("admin1234"),
            user_role="admin",
            is_active=1,
            password_changed_at=datetime.utcnow()
        )
        
        # 管理者ユーザー2
        admin2 = User(
            username="佐藤花子",
            email="sato.hanako@example.com",
            password_hash=generate_password_hash("admin5678"),
            user_role="admin",
            is_active=1,
            password_changed_at=datetime.utcnow()
        )
        
        # 一般ユーザー1
        user1 = User(
            username="鈴木一郎",
            email="suzuki.ichiro@example.com",
            password_hash=generate_password_hash("user1234"),
            user_role="user",
            is_active=1,
            password_changed_at=datetime.utcnow()
        )
        
        # 一般ユーザー2
        user2 = User(
            username="田中美咲",
            email="tanaka.misaki@example.com",
            password_hash=generate_password_hash("user5678"),
            user_role="user",
            is_active=1,
            password_changed_at=datetime.utcnow()
        )
        
        db.session.add_all([admin1, admin2, user1, user2])
        db.session.commit()
        
        print("テストユーザーを作成しました:")
        print("  管理者1: yamada.taro@example.com / admin1234")
        print("  管理者2: sato.hanako@example.com / admin5678")
        print("  一般1: suzuki.ichiro@example.com / user1234")
        print("  一般2: tanaka.misaki@example.com / user5678")


def create_test_contacts():
    """テスト連絡先データの作成"""
    with app.app_context():
        # ユーザー取得
        admin1 = User.query.filter_by(email="yamada.taro@example.com").first()
        user1 = User.query.filter_by(email="suzuki.ichiro@example.com").first()
        user2 = User.query.filter_by(email="tanaka.misaki@example.com").first()
        
        # 連絡先1: 営業部の社員
        contact1 = Contact(
            user_id=admin1.user_id,
            employee_number="EMP001",
            last_name="高橋",
            first_name="健太",
            last_name_kana="タカハシ",
            first_name_kana="ケンタ",
            department="営業部",
            position="課長",
            birthday=date(1985, 4, 15),
            notes="大阪支社担当"
        )
        
        # 連絡先2: 人事部の社員
        contact2 = Contact(
            user_id=admin1.user_id,
            employee_number="EMP002",
            last_name="伊藤",
            first_name="美穂",
            last_name_kana="イトウ",
            first_name_kana="ミホ",
            department="人事部",
            position="主任",
            birthday=date(1990, 8, 22),
            notes="採用担当"
        )
        
        # 連絡先3: 開発部の社員
        contact3 = Contact(
            user_id=user1.user_id,
            employee_number="EMP003",
            last_name="渡辺",
            first_name="大樹",
            last_name_kana="ワタナベ",
            first_name_kana="ダイキ",
            department="開発部",
            position="エンジニア",
            birthday=date(1992, 11, 5),
            notes="Webアプリケーション開発"
        )
        
        # 連絡先4: 総務部の社員
        contact4 = Contact(
            user_id=user2.user_id,
            employee_number="EMP004",
            last_name="中村",
            first_name="さくら",
            last_name_kana="ナカムラ",
            first_name_kana="サクラ",
            department="総務部",
            position="一般社員",
            birthday=date(1995, 3, 10),
            notes="施設管理担当"
        )
        
        db.session.add_all([contact1, contact2, contact3, contact4])
        db.session.commit()
        
        # 電話番号の追加
        phones = [
            ContactPhone(contact_id=contact1.contact_id, phone_type="社用携帯", phone_number="090-1234-5678"),
            ContactPhone(contact_id=contact1.contact_id, phone_type="自宅", phone_number="03-1111-2222"),
            ContactPhone(contact_id=contact2.contact_id, phone_type="社用携帯", phone_number="080-2345-6789"),
            ContactPhone(contact_id=contact3.contact_id, phone_type="個人携帯", phone_number="080-3333-4444"),
            ContactPhone(contact_id=contact4.contact_id, phone_type="社用携帯", phone_number="090-4567-8901"),
        ]
        
        # メールアドレスの追加
        emails = [
            ContactEmail(contact_id=contact1.contact_id, email_type="会社", email_address="takahashi.k@example.com"),
            ContactEmail(contact_id=contact2.contact_id, email_type="会社", email_address="ito.m@example.com"),
            ContactEmail(contact_id=contact3.contact_id, email_type="会社", email_address="watanabe.d@example.com"),
            ContactEmail(contact_id=contact3.contact_id, email_type="個人", email_address="daiki.w@gmail.com"),
            ContactEmail(contact_id=contact4.contact_id, email_type="会社", email_address="nakamura.s@example.com"),
        ]
        
        # 住所の追加
        addresses = [
            ContactAddress(
                contact_id=contact1.contact_id,
                address_type="自宅",
                postal_code="123-4567",
                prefecture="東京都",
                city="千代田区",
                address1="丸の内1-2-3",
                address2="マンションA 101号"
            ),
            ContactAddress(
                contact_id=contact2.contact_id,
                address_type="自宅",
                postal_code="234-5678",
                prefecture="神奈川県",
                city="横浜市西区",
                address1="みなとみらい4-5-6"
            ),
        ]
        
        db.session.add_all(phones + emails + addresses)
        db.session.commit()
        
        print("テスト連絡先データを作成しました:")
        print(f"  - {contact1.last_name} {contact1.first_name} ({contact1.department})")
        print(f"  - {contact2.last_name} {contact2.first_name} ({contact2.department})")
        print(f"  - {contact3.last_name} {contact3.first_name} ({contact3.department})")
        print(f"  - {contact4.last_name} {contact4.first_name} ({contact4.department})")


def create_test_groups():
    """テストグループの作成"""
    with app.app_context():
        admin1 = User.query.filter_by(email="yamada.taro@example.com").first()
        
        # グループ1: 営業チーム
        group1 = Group(
            user_id=admin1.user_id,
            group_name="営業チーム",
            description="営業部門のメンバー"
        )
        
        # グループ2: 開発チーム
        group2 = Group(
            user_id=admin1.user_id,
            group_name="開発チーム",
            description="開発部門のメンバー"
        )
        
        db.session.add_all([group1, group2])
        db.session.commit()
        
        # グループと連絡先の関連付け
        contact1 = Contact.query.filter_by(employee_number="EMP001").first()
        contact3 = Contact.query.filter_by(employee_number="EMP003").first()
        
        if contact1:
            cg1 = ContactGroup(contact_id=contact1.contact_id, group_id=group1.group_id)
            db.session.add(cg1)
        
        if contact3:
            cg2 = ContactGroup(contact_id=contact3.contact_id, group_id=group2.group_id)
            db.session.add(cg2)
        
        db.session.commit()
        
        print("テストグループを作成しました:")
        print(f"  - {group1.group_name}")
        print(f"  - {group2.group_name}")


if __name__ == "__main__":
    print("=" * 50)
    print("データベース初期化とテストデータ投入")
    print("=" * 50)
    
    # データベース初期化
    init_database()
    
    # テストデータ投入
    create_test_users()
    create_test_contacts()
    create_test_groups()
    
    print("=" * 50)
    print("完了しました!")
    print("=" * 50)
