import Vue from 'vue';
import Router from 'vue-router';
import Anime from '../components/Anime.vue';

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Anime',
      component: Anime,
    },
  ],
});
