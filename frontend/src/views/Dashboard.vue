<template>
  <div class="dashboard">
    <div class="row">
      <div class="col-12">
        <h2>ダッシュボード</h2>
        <p class="text-muted">名簿管理システムへようこそ</p>
      </div>
    </div>

    <div class="row">
      <div class="col-md-3 mb-3">
        <div class="card text-center">
          <div class="card-body">
            <h5 class="card-title">連絡先総数</h5>
            <h2 class="text-primary">{{ totalContacts }}</h2>
          </div>
        </div>
      </div>
      <div class="col-md-3 mb-3">
        <div class="card text-center">
          <div class="card-body">
            <h5 class="card-title">お気に入り</h5>
            <h2 class="text-warning">{{ favoriteContacts }}</h2>
          </div>
        </div>
      </div>
      <div class="col-md-3 mb-3">
        <div class="card text-center">
          <div class="card-body">
            <h5 class="card-title">グループ数</h5>
            <h2 class="text-success">{{ totalGroups }}</h2>
          </div>
        </div>
      </div>
      <div class="col-md-3 mb-3">
        <div class="card text-center">
          <div class="card-body">
            <h5 class="card-title">今月の更新</h5>
            <h2 class="text-info">{{ monthlyUpdates }}</h2>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-4">
      <div class="col-12">
        <div class="d-grid gap-2 d-md-flex justify-content-md-start">
          <router-link to="/contacts" class="btn btn-primary btn-lg">
            連絡先一覧を見る
          </router-link>
          <button class="btn btn-outline-secondary btn-lg">
            新規登録
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      totalContacts: 0,
      favoriteContacts: 0,
      totalGroups: 0,
      monthlyUpdates: 0
    }
  },
  mounted() {
    // TODO: APIからデータを取得
    this.loadDashboardData()
  },
  methods: {
    loadDashboardData() {
      // 仮のデータ
      this.totalContacts = 42
      this.favoriteContacts = 8
      this.totalGroups = 5
      this.monthlyUpdates = 12
    }
  }
}
</script>