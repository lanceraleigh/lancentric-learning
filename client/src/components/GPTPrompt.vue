<template>
  <div>
    <h1>API Test Component</h1>

    <div>
      <h3>Register</h3>
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button @click="register">Register</button>
    </div>

    <div>
      <h3>Login</h3>
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button @click="login">Login</button>
    </div>

    <div>
      <h3>Logout</h3>
      <button @click="logout">Logout</button>
    </div>

    <div>
      <h3>Get Words</h3>
      <button @click="getWords">Get Words</button>
    </div>

    <div>
      <h3>Get Progress</h3>
      <button @click="getProgress">Get Progress</button>
    </div>

    <div>
      <h3>Update Progress</h3>
      <input type="number" v-model="wordId" placeholder="Word ID" />
      <input type="checkbox" v-model="correct" />
      <label for="correct">Correct</label>
      <button @click="updateProgress">Update Progress</button>
    </div>

    <div>
      <h3>Generate Text</h3>
      <input type="text" v-model="prompt" placeholder="Prompt" />
      <button @click="generateText">Generate Text</button>
    </div>
  </div>
</template>

<script>
import * as api from "../../api";

export default {
  data() {
    return {
      username: "",
      password: "",
      wordId: null,
      correct: false,
      prompt: "",
    };
  },
  methods: {
    async register() {
      try {
        const response = await api.register(this.username, this.password);
        console.log(response);
      } catch (error) {
        console.error("Error registering:", error);
      }
    },
    async login() {
      try {
        const response = await api.login(this.username, this.password);
        console.log(response);
      } catch (error) {
        console.error("Error logging in:", error);
      }
    },
    async logout() {
      try {
        const response = await api.logout();
        console.log(response);
      } catch (error) {
        console.error("Error logging out:", error);
      }
    },
    async getWords() {
      try {
        const response = await api.getWords();
        console.log(response);
      } catch (error) {
        console.error("Error getting words:", error);
      }
    },
    async getProgress() {
      try {
        const response = await api.getProgress();
        console.log(response);
      } catch (error) {
        console.error("Error getting progress:", error);
      }
    },
    async updateProgress() {
      try {
        const response = await api.updateProgress(this.wordId, this.correct);
        console.log(response);
      } catch (error) {
        console.error("Error updating progress:", error);
      }
    },
    async generateText() {
      try {
        const response = await api.generateText(this.prompt);
        console.log(response);
      } catch (error) {
        console.error("Error generating text:", error);
      }
    },
  },
};
</script>
