<template>
  <div class="modal" v-if="showModal">
    <span class="close" @click="closeModal">&times;</span>
    <div class="modal-content">
      <h2>{{ lessonObject.title }}</h2>
      <h3>{{ lessonObject.theme }}</h3>
      <div v-for="(question, index) in generatedQuestions" :key="index">
        <div v-if="index === questionIndex">
          <p>{{ question.question_text }}</p>
          <div v-if="question.question_type === 'Multiple Choice'">
            <label
              v-for="(option, optionIndex) in question.multiple_choice_options"
              :key="optionIndex"
            >
              <input
                type="radio"
                :name="'question' + index"
                :value="option"
                @keyup.enter="submitAnswerAndUpdateUserKnowledge"
                v-model="userAnswers[index]"
              />
              {{ option }}
            </label>
          </div>
          <div v-else>
            <textarea
              :name="'question' + index"
              @keyup.enter="submitAnswerAndUpdateUserKnowledge"
              v-model="userAnswers[index]"
              :style="{ width: '300px', height: '100px' }"
              ref="answerArea"
            ></textarea>
          </div>
          <button @click="submitAnswerAndUpdateUserKnowledge">Answer</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { generateText } from "../../api"; // Import the generateText function from your API file

export default {
  props: {
    showModal: {
      type: Boolean,
      required: true,
    },
    lessonObject: {
      type: Object,
      required: true,
    },
  },
  async created() {
    if (this.lessonObject.word && this.lessonObject.word_translation) {
      const generatedSentence = await generateText(this.lessonObject.word);
      this.generatedQuestions = [
        {
          question_text: `Translate the word: "${this.lessonObject.word}"`,
          question_type: "Text",
          answer_text: this.lessonObject.word_translation,
        },
        {
          question_text: `Translate the following sentence: "${generatedSentence}"`,
          question_type: "Text",
          answer_text: "", // You'll need to provide the correct translation for the generated sentence
        },
      ];
    } else {
      this.generatedQuestions = this.lessonObject.questions;
    }
  },
  // ...rest of your component...
  data() {
    return {
      userAnswers: [],
      questionIndex: 0,
      correctAnswers: [],
      incorrectAnswers: [],
      generatedQuestions: [],
    };
  },
  // ...rest of your component...
};
</script>

<style scoped>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: hidden; /* Add this to disable scrolling inside the modal */
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  /* Remove margin and update width and height to 100% */

  margin: 0;
  padding: 20px;
  border: 1px solid #888;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Add styles for rounded edges and slightly 3D buttons */
.close {
  /* ... */
  padding: 0.5rem;
  position: absolute;
  top: 4rem;
  left: 1rem;
  font-size: 1.85rem;
  font-weight: bold;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.1);
  padding: 0 5px;
}

.close:hover,
.close:focus {
  font-size: 2rem;
  cursor: pointer;
  background-color: rgba(0, 0, 0, 0.2);
  /* ... */
}
</style>
