<template>
  <div class="signup">
    <h2>Sign Up</h2>
    <form @submit.prevent="handleSubmit">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" />

      <label for="registerPassword">Password:</label>
      <input type="password" id="registerPassword" v-model="password" />

      <label for="confirmRegisterPassword">Confirm Password:</label>
      <input
        type="password"
        id="confirmRegisterPassword"
        v-model="confirmPassword"
      />

      <button type="submit">Sign Up</button>
    </form>
    <p v-if="error">{{ error }}</p>
    <p>Already have an account? <a @click.prevent="goToLogin">Login</a></p>
  </div>
</template>

<script>
import * as api from "../../api"; // Update this path to match your api/index.js file

export default {
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
      error: null,
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await api.register({
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
        // Handle registration errors
      }
    },
    async handleSubmit() {
      if (this.password !== this.confirmPassword) {
        this.error = "Passwords must match";
        return;
      }
      try {
        const response = await api.register(this.username, this.password);
        if (response.status === 201) {
          // Redirect or perform any other action upon successful signup
          this.$store.commit("setAuthenticated", true);
          this.$router.push("/lancentric");
        } else {
          this.error = "An error occurred during signup";
        }
      } catch (error) {
        this.error = error.response.data.message || "An error occurred";
      }
    },
    goToLogin() {
      // Redirect to the login page
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
.signup {
  padding: 4rem;
}
/* Add your styles here */
</style>
