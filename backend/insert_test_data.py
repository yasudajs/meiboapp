"""
テストデータ挿入スクリプト
"""
from datetime import date
from app import create_app, db
from app.models import User, Contact, Group
from werkzeug.security import generate_password_hash

def insert_test_data():
    """テストデータを挿入"""
    app = create_app()
    app.app_context().push()
    
    try:
        # 管理者ユーザーの作成
        admin_user = User(
            username='admin',
            email='admin@meiboapp.com',
            password='admin123',
            user_role='admin'
        )
        db.session.add(admin_user)
        
        # 一般ユーザーの作成
        normal_user = User(
            username='user1',
            email='user1@meiboapp.com',
            password='user123',
            user_role='user'
        )
        db.session.add(normal_user)
        
        # 一旦コミットしてIDを取得
        db.session.commit()
        
        # グループの作成
        work_group = Group(
            user_id=normal_user.id,
            group_name='会社関係',
            description='職場の同僚や取引先'
        )
        db.session.add(work_group)
        
        family_group = Group(
            user_id=normal_user.id,
            group_name='家族・親戚',
            description='家族や親戚の連絡先'
        )
        db.session.add(family_group)
        
        db.session.commit()
        
        # 連絡先の作成
        contact1 = Contact(
            user_id=normal_user.id,
            last_name='田中',
            first_name='太郎',
            last_name_kana='タナカ',
            first_name_kana='タロウ',
            email='tanaka@example.com',
            phone='090-1234-5678',
            department='営業部',
            position='課長',
            birthday=date(1980, 5, 15),
            postal_code='100-0001',
            prefecture='東京都',
            city='千代田区',
            address1='大手町1-1-1'
        )
        db.session.add(contact1)
        
        contact2 = Contact(
            user_id=normal_user.id,
            last_name='佐藤',
            first_name='花子',
            last_name_kana='サトウ',
            first_name_kana='ハナコ',
            email='sato@example.com',
            phone='080-9876-5432',
            department='人事部',
            position='主任',
            birthday=date(1985, 12, 3),
            postal_code='150-0002',
            prefecture='東京都',
            city='渋谷区',
            address1='渋谷2-2-2'
        )
        db.session.add(contact2)
        
        contact3 = Contact(
            user_id=normal_user.id,
            last_name='山田',
            first_name='次郎',
            last_name_kana='ヤマダ',
            first_name_kana='ジロウ',
            email='yamada@example.com',
            phone='070-1111-2222',
            department='開発部',
            position='エンジニア',
            birthday=date(1990, 8, 20),
            postal_code='160-0023',
            prefecture='東京都',
            city='新宿区',
            address1='西新宿3-3-3'
        )
        db.session.add(contact3)
        
        db.session.commit()
        
        # 連絡先とグループの関連付け
        work_group.contacts.append(contact1)
        work_group.contacts.append(contact2)
        work_group.contacts.append(contact3)
        
        family_group.contacts.append(contact3)  # 山田さんは家族のグループにも所属
        
        db.session.commit()
        
        print("テストデータが正常に挿入されました！")
        print(f"管理者: {admin_user.username} (ID: {admin_user.id})")
        print(f"一般ユーザー: {normal_user.username} (ID: {normal_user.id})")
        print(f"グループ数: {Group.query.count()}")
        print(f"連絡先数: {Contact.query.count()}")
        
    except Exception as e:
        db.session.rollback()
        print(f"エラーが発生しました: {e}")
    finally:
        db.session.close()

if __name__ == '__main__':
    insert_test_data()