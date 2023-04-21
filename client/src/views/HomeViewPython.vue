<template>
  <div class="home-view">
    <!-- <div class="buttons">
      <button @click="testLogin">Login</button>
      <button @click="testLogout">Logout</button>
      <button @click="getLessonsByDifficulty">Get Lessons by Difficulty</button>
      <button @click="testUpdateUserProgress">Update Progress</button>
      <button @click="testCreateLesson">Create Lesson</button>
      <button @click="clearAllLessonsAndQuestions">Clear Tables</button>
    </div> -->

    <GPTPrompt />

    <LessonModal
      :showModal="showLessonModal"
      :lessonObject="lessonObject"
      @update-showModal="updateShowModal"
    />

    <div class="group-title">Beginner</div>

    <div class="lessons-group">
      <div v-for="lesson in beginner" :key="lesson.id">
        <div class="lesson-card">
          <div class="lesson-card-theme">{{ lesson.theme }}</div>
          <div class="lesson-card-buttons">
            <button @click="startLesson(lesson)">Start</button>
          </div>
        </div>
      </div>
    </div>

    <div class="group-title">Intermediate</div>

    <div class="lessons-group">
      <div v-for="lesson in intermediate" :key="lesson.id">
        <div class="lesson-card">
          <div class="lesson-card-theme">{{ lesson.theme }}</div>
          <div class="lesson-card-buttons">
            <button @click="startLesson(lesson)">Start</button>
          </div>
        </div>
      </div>
    </div>

    <div class="group-title">Advanced</div>

    <div class="lessons-group">
      <div v-for="lesson in advanced" :key="lesson.id">
        <div class="lesson-card">
          <div class="lesson-card-theme">{{ lesson.theme }}</div>
          <div class="lesson-card-buttons">
            <button @click="startLesson(lesson)">Start</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as api from "../../api";
// import * as backendLessons from "../helpers/PythonPortugueseLessons.ts";
import GPTPrompt from "../components/GPTPrompt";
import LessonModal from "../components/LessonModal";

export default {
  components: {
    LessonModal,
    GPTPrompt,
  },
  data() {
    return {
      // backendPortugueseLessons: backendLessons.backendPortugueseLessons,
      beginner: [],
      intermediate: [],
      advanced: [],
      lessonObject: {},
      showLessonModal: false,
    };
  },
  async mounted() {
    this.beginner = await this.getLessonsByDifficulty("Beginner");
    this.intermediate = await this.getLessonsByDifficulty("Intermediate");
    this.advanced = await this.getLessonsByDifficulty("Advanced");
  },
  methods: {
    updateShowModal(bool) {
      this.showLessonModal = bool;
    },
    async startLesson(lesson) {
      this.lessonObject = {
        ...lesson,
        questions: await this.fetchQuestions(lesson.id),
      };
      // console.log(this.lessonObject);
      this.showLessonModal = true;
    },
    // login logout
    async testLogin() {
      try {
        const response = await api.login("email@example.com", "password");
        // console.log("Login response:", response);
        this.loginMessage = response;
      } catch (error) {
        console.error("Error in testLogin:", error);
      }
    },
    async testLogout() {
      try {
        const response = await api.logout();
        // console.log("Logout response:", response);
        this.logoutMessage = response;
      } catch (error) {
        console.error("Error in testLogout:", error);
      }
    },
    // Lessons
    async getLessonContent() {
      // console.log(this.backendPortugueseLessons);
      try {
        const response = await api.getLessonContent(25);
        // console.log("Get Lesson Content response:", response);
        this.getLessonContentMessage = response;
        this.fetchQuestions(response.id);
      } catch (error) {
        console.error("Error in testGetLessonContent:", error);
      }
    },
    async fetchQuestions(lessonId) {
      const response = await api.getQuestionsByLessonId(lessonId);
      // console.log(response.questions);
      return response.questions;
    },
    async getLessonsByDifficulty(difficulty) {
      const response = await api.getLessonsByDifficulty(difficulty);
      return response.lessons;
    },

    // async testCreateLesson() {
    //   // console.log(this.backendPortugueseLessons);
    //   try {
    //     for (let i = 0; i < this.backendPortugueseLessons.length; i++) {
    //       console.log(this.backendPortugueseLessons[i]);
    //       const response = await api.createLesson(
    //         this.backendPortugueseLessons[i]
    //       );

    //       this.createLessonMessage.push(response);

    //       console.log("Create Lesson response:", this.createLessonMessage);
    //     }
    //   } catch (error) {
    //     console.error("Error in testCreateLesson:", error);
    //   }
    // },

    // update account

    async testUpdateUserProgress() {
      try {
        const response = await api.updateUserProgress(1, 1, {
          progressData: "test data",
        });
        // console.log("Update User Progress response:", response);
        this.updateUserProgressMessage = response;
      } catch (error) {
        console.error("Error in testUpdateUserProgress:", error);
      }
    },

    // Admin
    // Add this method to the methods object in your Vue component
    async clearAllLessonsAndQuestions() {
      try {
        const response = await api.clearLessonsAndQuestions();
        console.log("Clear lessons and questions response:", response);
        // You may display a success message or perform any other action you need here
      } catch (error) {
        console.error("Error in clearAllLessonsAndQuestions:", error);
        // You may display an error message or handle the error in any way you prefer
      }
    },
  },
};
</script>

<style scoped>
.home-view {
  font-family: "Comic Sans MS", cursive, sans-serif;
  padding: 3rem;
  padding-top: 5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.lessons-group {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}
.lesson-card {
  background: #ddd;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 250px;
  margin: 1rem;
  padding: 1rem;
  border-radius: 20px;
  border: 1px solid #4b4c9d;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.group-title {
  font-size: 2rem;
  font-weight: bold;
  margin: 2rem;
}
button {
  font-family: "Comic Sans MS", cursive, sans-serif;
  margin: 10px;
  padding: 10px 20px;
  border-radius: 30px;
  border: 1px solid #4b4c9d;
  background-color: #e5e5ff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}
button:hover {
  cursor: pointer;
  background: #4b4c9d;
  color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
