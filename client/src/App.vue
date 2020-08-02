<template>
  <div id="app">
    <div id="nav" v-if="isLoggedIn">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
import CheckLogin from "@/mixins/CheckLogin";
import axios from 'axios'
import {config} from '@/config/config'

export default {
  mixins: [CheckLogin],
  data() {
    return {
      isLoggedIn: false
    };
  },
  mounted() {
    if (CheckLogin.methods.checkLogin()) this.isLoggedIn = true;
    if (!this.isLoggedIn && this.$router.path != '/login') this.$router.push({name: 'Login'})

    this.checkAPI()
  },
  methods: {
    checkAPI() {
      axios
        // .get('http://localhost:5000/api/user')
        .get(config.API_BASE_URI + 'api/user')
        .then(data => console.log(data))
        .catch(err => {console.log(err)})
    }
  }
};
</script>
