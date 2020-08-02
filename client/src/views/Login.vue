<template>
  <div class="container">
    <div>
      <form class="form" @submit="submit">
        <h2>User Login</h2>
        <div class="input-container">
          <i class="fa fa-user icon"></i>
          <input
            type="text"
            v-model="username"
            class="input-field"
            placeholder="Username"
          />
        </div>

        <div class="input-container">
          <i class="fa fa-key icon"></i>
          <input
            type="text"
            v-model="password"
            class="input-field"
            placeholder="Password"
          />
        </div>

        <button class="btn">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    submit(e) {
      e.preventDefault();
    }
  }
};
</script>
