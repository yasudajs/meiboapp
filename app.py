import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from models import db, User


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'), static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'meiboapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# データベース初期化
db.init_app(app)

# Flask-Login初期化
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'
login_manager.login_message = 'ログインが必要です'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/")
def index():
    if current_user.is_authenticated:
        if current_user.is_admin():
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('user_page'))
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email or not password:
        flash('メールアドレスとパスワードを入力してください', 'error')
        return redirect(url_for('index'))
    
    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password_hash, password):
        if user.is_active:
            # ログイン成功
            login_user(user)
            # 最終ログイン日時を更新
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            # 権限に応じてリダイレクト
            if user.is_admin():
                return redirect(url_for('admin_page'))
            else:
                return redirect(url_for('user_page'))
        else:
            flash('このアカウントは無効化されています', 'error')
    else:
        flash('メールアドレスまたはパスワードが正しくありません', 'error')
    
    return redirect(url_for('index'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('ログアウトしました', 'success')
    return redirect(url_for('index'))


@app.route("/admin")
@login_required
def admin_page():
    if not current_user.is_admin():
        flash('管理者権限が必要です', 'error')
        return redirect(url_for('user_page'))
    return render_template("admin.html", user=current_user)


@app.route("/user")
@login_required
def user_page():
    return render_template("user.html", user=current_user)


# マイ連絡先表示
@app.route("/my_contact")
@login_required
def my_contact():
    # 自分の連絡先（is_deleted=0のみ）
    contact = current_user.contacts[0] if current_user.contacts and current_user.contacts[0].is_deleted == 0 else None
    return render_template("my_contact.html", user=current_user, contact=contact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
