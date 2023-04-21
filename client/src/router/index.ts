import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeViewPython.vue";
import store from "../store";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
    meta: {
      title: "Let's Learn",
    },
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../views/RegisterView.vue"),
    meta: {
      title: "Register to Lancentric",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () =>
      //   import(/* webpackChunkName: "about" */ "../views/LandingPage.vue"),
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("jwt_token");

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.state.isAuthenticated || !token) {
      next({
        path: "/login",
        query: { redirect: to.fullPath },
      });
      document.title = `Login`;
    } else {
      next();
      document.title = `${to.meta.title}`;
    }
  } else {
    next();
    document.title = `${to.meta.title}`;
  }
});

export default router;
