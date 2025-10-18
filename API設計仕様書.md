# 名簿アプリ API設計仕様書

## 📡 API エンドポイント仕様

### 🔐 認証系 API

#### 1. ログイン
```
POST /api/auth/login
```
**リクエスト**:
```json
{
  "email": "user@example.com",
  "password": "Password123!"
}
```
**レスポンス（成功）**:
```json
{
  "status": "success",
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
      "id": 1,
      "username": "田中太郎",
      "email": "user@example.com",
      "role": "user"
    }
  }
}
```

#### 2. ログアウト
```
POST /api/auth/logout
Headers: Authorization: Bearer {access_token}
```

#### 3. トークン更新
```
POST /api/auth/refresh
```
**リクエスト**:
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### 4. パスワード変更
```
PUT /api/auth/change-password
Headers: Authorization: Bearer {access_token}
```
**リクエスト**:
```json
{
  "current_password": "OldPass123!",
  "new_password": "NewPass456!"
}
```

---

### 👥 連絡先管理 API

#### 1. 連絡先一覧取得
```
GET /api/contacts
Headers: Authorization: Bearer {access_token}
Query Parameters:
  - page: ページ番号（デフォルト: 1）
  - limit: 1ページあたりの件数（デフォルト: 20）
  - sort: ソート項目（name, name_kana, created_at, updated_at）
  - order: ソート順（asc, desc）
  - search: 検索キーワード
```

**レスポンス**:
```json
{
  "status": "success",
  "data": {
    "contacts": [
      {
        "id": 1,
        "last_name": "田中",
        "first_name": "太郎",
        "last_name_kana": "タナカ",
        "first_name_kana": "タロウ",
        "email": "tanaka@example.com",
        "department": "営業部",
        "position": "課長",
        "is_favorite": false,
        "created_at": "2025-01-15T09:30:00Z",
        "updated_at": "2025-01-15T09:30:00Z"
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "total_items": 100,
      "items_per_page": 20
    }
  }
}
```

#### 2. 連絡先詳細取得
```
GET /api/contacts/{id}
Headers: Authorization: Bearer {access_token}
```

**レスポンス**:
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "last_name": "田中",
    "first_name": "太郎",
    "last_name_kana": "タナカ",
    "first_name_kana": "タロウ",
    "email": "tanaka@example.com",
    "department": "営業部",
    "position": "課長",
    "birthday": "1985-04-15",
    "personal_phone": "090-1234-5678",
    "business_phone": "03-1234-5678",
    "address": {
      "postal_code": "123-4567",
      "prefecture": "東京都",
      "city": "新宿区",
      "address1": "西新宿1-1-1",
      "address2": "ABCビル5F"
    },
    "notes": "営業担当者",
    "profile_image": "/uploads/profiles/user1.jpg",
    "is_favorite": false,
    "groups": [
      {
        "id": 1,
        "name": "営業チーム"
      }
    ],
    "created_at": "2025-01-15T09:30:00Z",
    "updated_at": "2025-01-15T09:30:00Z"
  }
}
```

#### 3. 連絡先新規登録（管理者のみ）
```
POST /api/contacts
Headers: Authorization: Bearer {access_token}
```

**リクエスト**:
```json
{
  "last_name": "田中",
  "first_name": "太郎",
  "last_name_kana": "タナカ",
  "first_name_kana": "タロウ",
  "email": "tanaka@example.com",
  "department": "営業部",
  "position": "課長",
  "birthday": "1985-04-15",
  "personal_phone": "090-1234-5678",
  "business_phone": "03-1234-5678",
  "address": {
    "postal_code": "123-4567",
    "prefecture": "東京都",
    "city": "新宿区",
    "address1": "西新宿1-1-1",
    "address2": "ABCビル5F"
  },
  "notes": "営業担当者",
  "user_role": "user"
}
```

**レスポンス（成功）**:
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "generated_password": "Ab3$Fg89",
    "message": "ユーザーが正常に登録されました"
  }
}
```

#### 4. 連絡先更新
```
PUT /api/contacts/{id}
Headers: Authorization: Bearer {access_token}
```
- 管理者：全項目更新可能
- 一般ユーザー：自分のデータのみ、一部項目のみ更新可能

#### 5. 連絡先削除（管理者のみ）
```
DELETE /api/contacts/{id}
Headers: Authorization: Bearer {access_token}
```

#### 6. 連絡先検索
```
GET /api/contacts/search
Headers: Authorization: Bearer {access_token}
Query Parameters:
  - q: 検索キーワード
  - field: 検索対象フィールド（name, email, phone, department）
  - limit: 件数制限
```

---

### 🏷️ グループ管理 API

#### 1. グループ一覧
```
GET /api/groups
Headers: Authorization: Bearer {access_token}
```

#### 2. グループ作成
```
POST /api/groups
Headers: Authorization: Bearer {access_token}
```

#### 3. グループにメンバー追加/削除
```
POST /api/groups/{group_id}/members
DELETE /api/groups/{group_id}/members/{contact_id}
```

---

### 👤 ユーザー管理 API（管理者専用）

#### 1. ユーザー一覧
```
GET /api/users
Headers: Authorization: Bearer {access_token}
Required Role: admin
```

#### 2. ユーザー権限変更
```
PUT /api/users/{id}/role
Headers: Authorization: Bearer {access_token}
Required Role: admin
```

---

## 🚨 エラーハンドリング仕様

### 1. HTTPステータスコード
- **200**: 成功
- **201**: 作成成功
- **400**: バリデーションエラー
- **401**: 認証エラー
- **403**: 権限エラー
- **404**: リソースが見つからない
- **409**: 重複エラー
- **429**: レート制限
- **500**: サーバーエラー

### 2. エラーレスポンス形式

#### バリデーションエラー（400）
```json
{
  "status": "error",
  "error_type": "validation_error",
  "message": "入力値に問題があります",
  "errors": {
    "last_name": ["姓は必須です"],
    "email": ["既に登録されているメールアドレスです"],
    "password": ["パスワードは8文字以上である必要があります"]
  }
}
```

#### 認証エラー（401）
```json
{
  "status": "error",
  "error_type": "authentication_error",
  "message": "認証に失敗しました",
  "error_code": "AUTH001"
}
```

#### 権限エラー（403）
```json
{
  "status": "error",
  "error_type": "permission_error",
  "message": "この操作を実行する権限がありません",
  "error_code": "PERM001"
}
```

#### リソース未発見（404）
```json
{
  "status": "error",
  "error_type": "not_found",
  "message": "指定されたリソースが見つかりません",
  "error_code": "NOT_FOUND"
}
```

#### サーバーエラー（500）
```json
{
  "status": "error",
  "error_type": "server_error",
  "message": "サーバー内部エラーが発生しました",
  "error_code": "SYS001"
}
```

---

## 🔒 認証・権限制御

### 1. JWT設定
```
アクセストークン有効期限: 15分
リフレッシュトークン有効期限: 30日
```

### 2. 権限制御マトリックス

| エンドポイント | 管理者 | 一般ユーザー | 備考 |
|----------------|--------|--------------|------|
| GET /api/contacts | ✅ 全件 | ✅ 自分のみ | |
| POST /api/contacts | ✅ | ❌ | 新規登録は管理者のみ |
| PUT /api/contacts/{id} | ✅ 全件 | ✅ 自分のみ | |
| DELETE /api/contacts/{id} | ✅ | ❌ | 削除は管理者のみ |
| GET /api/users | ✅ | ❌ | ユーザー管理は管理者のみ |

### 3. レート制限
```
ログインAPI: 5回/分/IP
その他API: 100回/分/ユーザー
```

---

## 📋 決定が必要な具体的項目

### 🎯 即決が必要
1. **ページネーション**: 1ページ何件表示？（推奨：20件）
2. **検索**: 部分一致か完全一致か？（推奨：部分一致）
3. **ソート**: デフォルトのソート順は？（推奨：フリガナ順）
4. **画像アップロード**: サイズ制限は？（推奨：1MB以下）

### 🤔 検討が必要
1. **プロフィール画像**: 必要か？実装優先度は？
2. **グループ機能**: Phase1で実装するか？
3. **エクスポート機能**: CSV/Excel両方必要か？
4. **検索機能**: 高度な検索（複数条件）は必要か？

---

どの項目から詳細を決めていきますか？