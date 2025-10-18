<template>
  <div class="login-container">
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-4">
        <div class="card">
          <div class="card-header">
            <h4 class="text-center">ログイン</h4>
          </div>
          <div class="card-body">
            <form @submit.prevent="login">
              <div class="mb-3">
                <label for="email" class="form-label">メールアドレス</label>
                <input
                  type="email"
                  class="form-control"
                  id="email"
                  v-model="form.email"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">パスワード</label>
                <input
                  type="password"
                  class="form-control"
                  id="password"
                  v-model="form.password"
                  required
                />
              </div>
              <button type="submit" class="btn btn-primary w-100">
                ログイン
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      form: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    login() {
      // TODO: ログイン処理の実装
      console.log('Login attempt:', this.form)
      // 仮でダッシュボードに遷移
      this.$router.push('/dashboard')
    }
  }
}
</script>

<style scoped>
.login-container {
  padding-top: 100px;
}
</style>