<template>
  <div class="home">
    <div class="jumbotron bg-light p-5 rounded">
      <h1 class="display-4">名簿管理システム</h1>
      <p class="lead">
        小規模事業所向けの効率的な連絡先管理システムです。
      </p>
      <hr class="my-4">
      <p>
        従業員の連絡先情報を安全に管理し、検索・編集・削除機能を提供します。
      </p>
      <router-link class="btn btn-primary btn-lg" to="/contacts" role="button">
        連絡先一覧を見る
      </router-link>
    </div>

    <div class="row mt-5">
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">🔐 安全な認証</h5>
            <p class="card-text">
              JWT認証により、安全なログイン機能を提供します。
            </p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">🔍 高速検索</h5>
            <p class="card-text">
              氏名、部署、メールアドレスなど様々な条件で検索可能です。
            </p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">👥 権限管理</h5>
            <p class="card-text">
              管理者と一般ユーザーで適切な権限制御を行います。
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.jumbotron {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.card {
  height: 100%;
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-5px);
}
</style>