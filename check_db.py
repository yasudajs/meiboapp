"""
データベース内容確認スクリプト
"""
from app import app
from models import db, User, Contact, ContactPhone, ContactEmail, Group


def check_database():
    """データベース内容の確認"""
    with app.app_context():
        print("\n" + "=" * 60)
        print("【ユーザー一覧】")
        print("=" * 60)
        users = User.query.all()
        for user in users:
            print(f"ID: {user.user_id}, 名前: {user.username}, Email: {user.email}, 権限: {user.user_role}")
        
        print("\n" + "=" * 60)
        print("【連絡先一覧】")
        print("=" * 60)
        contacts = Contact.query.filter_by(is_deleted=0).all()
        for contact in contacts:
            print(f"\n社員番号: {contact.employee_number}")
            print(f"  氏名: {contact.last_name} {contact.first_name} ({contact.last_name_kana} {contact.first_name_kana})")
            print(f"  部署: {contact.department}, 役職: {contact.position}")
            print(f"  登録者: {contact.user.username}")
            
            # 電話番号
            if contact.phones:
                print(f"  電話:")
                for phone in contact.phones:
                    print(f"    - {phone.phone_type}: {phone.phone_number}")
            
            # メールアドレス
            if contact.emails:
                print(f"  メール:")
                for email in contact.emails:
                    print(f"    - {email.email_type}: {email.email_address}")
            
            # グループ
            if contact.groups:
                print(f"  所属グループ:")
                for cg in contact.groups:
                    print(f"    - {cg.group.group_name}")
        
        print("\n" + "=" * 60)
        print("【グループ一覧】")
        print("=" * 60)
        groups = Group.query.all()
        for group in groups:
            member_count = len(group.contacts)
            print(f"グループ名: {group.group_name} (メンバー数: {member_count})")
            print(f"  説明: {group.description}")
            print(f"  作成者: {group.user.username}")
        
        print("\n" + "=" * 60)
        print("統計情報")
        print("=" * 60)
        print(f"総ユーザー数: {User.query.count()}")
        print(f"  - 管理者: {User.query.filter_by(user_role='admin').count()}")
        print(f"  - 一般: {User.query.filter_by(user_role='user').count()}")
        print(f"総連絡先数: {Contact.query.filter_by(is_deleted=0).count()}")
        print(f"総グループ数: {Group.query.count()}")
        print("=" * 60 + "\n")


if __name__ == "__main__":
    check_database()
