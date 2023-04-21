import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Login/ Logout

export const login = async (username, password) => {
  try {
    const response = await apiClient.post("/login", { username, password });
    return response.data;
  } catch (error) {
    console.error("Error logging in:", error);
    throw error;
  }
};

export const logout = async () => {
  try {
    const response = await apiClient.get("/logout");
    return response.data;
  } catch (error) {
    console.error("Error logging out:", error);
    throw error;
  }
};

export const register = async (username, password) => {
  try {
    const response = await apiClient.post("/register", { username, password });
    return response;
  } catch (error) {
    console.error("Error signing up:", error);
    throw error;
  }
};

// User Progress

export const updateUserProgress = async (wordId, correct) => {
  try {
    const response = await apiClient.post("/update_user_progress", {
      wordId,
      correct,
    });
    return response.data;
  } catch (error) {
    console.error("Error updating user progress:", error);
    throw error;
  }
};

// Words

export const getWords = async () => {
  try {
    const response = await apiClient.get("/words");
    return response.data;
  } catch (error) {
    console.error("Error getting words:", error);
    throw error;
  }
};

export const addWord = async (wordData) => {
  try {
    const response = await apiClient.post("/words/add", wordData);
    return response.data;
  } catch (error) {
    console.error("Error adding word:", error);
    throw error;
  }
};

export const addWordToMastered = async (wordId) => {
  try {
    const response = await apiClient.post("/words/mastered/add", { wordId });
    return response.data;
  } catch (error) {
    console.error("Error adding word to mastered list:", error);
    throw error;
  }
};

// OpenAI API

export async function generateText(prompt) {
  try {
    const response = await apiClient.post(`/test_openai_with_custom_prompt`, {
      prompt,
    });
    return response.data.generated_text;
  } catch (error) {
    console.error(error);
    return null;
  }
}
