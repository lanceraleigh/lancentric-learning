import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
  },
  mutations: {
    setAuthenticated(state, payload) {
      state.isAuthenticated = payload;
    },
  },
  actions: {},
  modules: {},
});
