<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="handleSubmit">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" />

      <label for="loginPassword">Password:</label>
      <input type="password" id="loginPassword" v-model="password" />

      <button type="submit">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
    <p>New user? <a @click.prevent="goToSignup">Sign up</a></p>
  </div>
</template>

<script>
import * as api from "../../api"; // Update this path to match your api/index.js file

export default {
  data() {
    return {
      username: "",
      password: "",
      error: null,
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await api.login({
          username: this.username,
          password: this.password,
        });

        // Save the JWT token in the local storage
        localStorage.setItem("jwt_token", response.data.access_token);

        // Update the authentication status in the Vuex store
        this.$store.commit("setAuthStatus", true);

        // Redirect to the protected route or a default route
        this.$router.push("/lancentric");
      } catch (error) {
        // Handle login errors
      }
    },

    async handleSubmit() {
      try {
        const response = await api.login(this.username, this.password);
        // console.log(response);
        if (response.status === 200) {
          // Redirect or perform any other action upon successful login
          this.$router.push("/");
        } else {
          this.error = "Invalid username or password";
        }
      } catch (error) {
        this.error = error.response.data.message || "An error occurred";
        // console.log(this.error);
      }
    },
  },
  goToSignup() {
    // Redirect to the signup page
    this.$router.push("/signup");
  },
};
</script>

<style scoped>
/* Add your styles here */
.login {
  padding: 4rem;
}
</style>
