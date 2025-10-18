<template>
  <div class="contact-list">
    <div class="row">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-4">
          <h2>連絡先一覧</h2>
          <button class="btn btn-primary">
            <i class="bi bi-plus"></i> 新規登録
          </button>
        </div>
      </div>
    </div>

    <!-- 検索フォーム -->
    <div class="row mb-4">
      <div class="col-md-6">
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            placeholder="名前、メール、電話番号で検索..."
            v-model="searchQuery"
            @input="searchContacts"
          />
          <button class="btn btn-outline-secondary" type="button">
            <i class="bi bi-search"></i>
          </button>
        </div>
      </div>
      <div class="col-md-3">
        <select class="form-select" v-model="sortBy" @change="sortContacts">
          <option value="name">名前順</option>
          <option value="name_kana">フリガナ順</option>
          <option value="created_at">登録日順</option>
          <option value="updated_at">更新日順</option>
        </select>
      </div>
    </div>

    <!-- 連絡先一覧 -->
    <div class="row">
      <div class="col-12">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead class="table-light">
              <tr>
                <th>氏名</th>
                <th>フリガナ</th>
                <th>メールアドレス</th>
                <th>部署</th>
                <th>役職</th>
                <th>操作</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="contact in filteredContacts" :key="contact.id">
                <td>{{ contact.last_name }} {{ contact.first_name }}</td>
                <td>{{ contact.last_name_kana }} {{ contact.first_name_kana }}</td>
                <td>{{ contact.email }}</td>
                <td>{{ contact.department }}</td>
                <td>{{ contact.position }}</td>
                <td>
                  <button class="btn btn-sm btn-outline-primary me-1">
                    詳細
                  </button>
                  <button class="btn btn-sm btn-outline-secondary">
                    編集
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- データが無い場合 -->
    <div v-if="filteredContacts.length === 0" class="text-center py-5">
      <p class="text-muted">連絡先が見つかりませんでした。</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactList',
  data() {
    return {
      searchQuery: '',
      sortBy: 'name_kana',
      contacts: [],
      filteredContacts: []
    }
  },
  mounted() {
    this.loadContacts()
  },
  methods: {
    loadContacts() {
      // TODO: APIからデータを取得
      // 仮のデータ
      this.contacts = [
        {
          id: 1,
          last_name: '田中',
          first_name: '太郎',
          last_name_kana: 'タナカ',
          first_name_kana: 'タロウ',
          email: 'tanaka@example.com',
          department: '営業部',
          position: '課長'
        },
        {
          id: 2,
          last_name: '佐藤',
          first_name: '花子',
          last_name_kana: 'サトウ',
          first_name_kana: 'ハナコ',
          email: 'sato@example.com',
          department: '総務部',
          position: '主任'
        }
      ]
      this.filteredContacts = [...this.contacts]
    },
    searchContacts() {
      if (!this.searchQuery) {
        this.filteredContacts = [...this.contacts]
        return
      }
      
      const query = this.searchQuery.toLowerCase()
      this.filteredContacts = this.contacts.filter(contact => {
        return (
          contact.last_name.toLowerCase().includes(query) ||
          contact.first_name.toLowerCase().includes(query) ||
          contact.last_name_kana.toLowerCase().includes(query) ||
          contact.first_name_kana.toLowerCase().includes(query) ||
          contact.email.toLowerCase().includes(query) ||
          contact.department.toLowerCase().includes(query)
        )
      })
    },
    sortContacts() {
      // TODO: ソート機能の実装
      console.log('Sort by:', this.sortBy)
    }
  }
}
</script>