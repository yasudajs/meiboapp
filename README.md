# 名簿管理システム（MeiboApp）

小規模事業所向けの名簿管理Webアプリケーション

## 📋 プロジェクト概要

### 目的
個人や組織の連絡先情報を効率的に管理・検索・更新できるWebアプリケーション

### 対象ユーザー
- 小規模組織（50-1000人程度の連絡先管理）
- 企業の人事・総務部門

## 🔧 技術構成

### フロントエンド
- **フレームワーク**: Vue.js 3
- **CSSフレームワーク**: Bootstrap 5
- **バンドラー**: Vite
- **HTTP クライアント**: Axios

### バックエンド
- **言語**: Python 3.7.17
- **フレームワーク**: Flask 2.2.5
- **データベース**: SQLite
- **ORM**: SQLAlchemy 1.4.53
- **認証**: JWT (Flask-JWT-Extended)
- **API**: Flask-RESTX 0.5.1

## 📁 プロジェクト構成

```
meiboapp/
├── backend/           # Flaskバックエンド
│   ├── app/
│   │   ├── models/    # データベースモデル
│   │   ├── routes/    # APIルート
│   │   └── utils/     # ユーティリティ
│   ├── migrations/    # データベースマイグレーション
│   ├── tests/         # テストファイル
│   └── requirements.txt
├── frontend/          # Vue.jsフロントエンド
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   └── router/
│   └── package.json
├── docs/              # ドキュメント
├── 仕様書.md
├── API設計仕様書.md
└── README.md
```

## 🚀 セットアップ手順

### 前提条件
- Python 3.7.17
- Node.js 18+
- Git

### 1. リポジトリのクローン
```bash
git clone <repository-url>
cd meiboapp
```

### 2. バックエンドセットアップ
```bash
cd backend

# 仮想環境作成
python -m venv venv

# 仮想環境アクティベート (Windows)
venv\Scripts\activate

# 依存関係インストール
pip install -r requirements.txt

# 環境変数設定
copy .env.example .env
# .envファイルを編集

# データベース初期化
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 開発サーバー起動
python run.py
```

### 3. フロントエンドセットアップ
```bash
cd frontend

# 依存関係インストール
npm install

# 開発サーバー起動
npm run dev
```

## 🔐 主要機能

### 権限管理
- **管理者権限**: 全データの管理、ユーザー登録・削除
- **一般ユーザー権限**: 自分のデータのみ編集可能

### 連絡先管理
- 連絡先の登録・編集・削除・表示
- 高度な検索機能
- グループ管理
- お気に入り機能

### セキュリティ
- JWT認証
- パスワード強度チェック
- 権限ベースアクセス制御
- 入力値検証

## 📚 ドキュメント

- [仕様書](./仕様書.md) - 詳細な機能仕様
- [API設計仕様書](./API設計仕様書.md) - API仕様
- [環境構築手順](./環境構築手順.md) - 開発環境セットアップ
- [Python3.7対応の制約と対策](./Python3.7対応の制約と対策.md) - 技術制約への対応

## 🧪 テスト

### バックエンドテスト
```bash
cd backend
pytest
```

### フロントエンドテスト
```bash
cd frontend
npm run test
```

## 📦 デプロイ

### 本番環境要件
- Python 3.7.17
- 必要モジュール（requirements.txt参照）
- Webサーバー（Nginx等）

### デプロイ手順
1. サーバーに必要モジュールをインストール
2. アプリケーションファイルをアップロード
3. 環境変数を設定
4. データベースを初期化
5. Webサーバーを設定

## 🤝 開発ガイドライン

### コミットメッセージ
- feat: 新機能の追加
- fix: バグ修正
- docs: ドキュメント更新
- style: コードフォーマット
- refactor: リファクタリング
- test: テスト追加・修正

### ブランチ戦略
- `main`: 本番環境
- `develop`: 開発環境
- `feature/*`: 機能開発
- `hotfix/*`: 緊急修正

## 📝 ライセンス

MIT License

## 👥 作成者

システム開発チーム

---

**作成日**: 2025年10月19日  
**最終更新**: 2025年10月19日