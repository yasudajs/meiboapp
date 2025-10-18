from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# Flask拡張のインスタンス作成
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    """Flaskアプリケーションファクトリ"""
    app = Flask(__name__)
    
    # 設定
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///meiboapp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # JWT設定
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # 開発時は無期限
    
    # 拡張の初期化
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # モデルのインポート（マイグレーション用）
    from app.models import User, Contact, Group
    
    # ブループリントの登録
    from app.routes.auth import auth_bp
    from app.routes.contacts import contacts_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(contacts_bp, url_prefix='/api/contacts')
    
    # ヘルスチェックエンドポイント
    @app.route('/api/health')
    def health_check():
        return {'status': 'OK', 'message': '名簿管理システム API'}
    
    return app