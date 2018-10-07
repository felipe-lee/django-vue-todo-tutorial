// store.js

import Vue from 'vue';
import Vuex from 'vuex';
import api from './api.js';

Vue.use(Vuex);  // Only required because we are using modules.
const apiRoot = 'http://127.0.0.1:8000/api/';

const store = new Vuex.Store({
  state: {
    todos: [],
  },
  mutations: {
    'GET_TODOS': function (state, response) {
      state.todos = response.data;
    },
    'ADD_TODO': function (state, response) {
      state.todos.push(response.data);
    },
    'CLEAR_TODOS': function (state) {
      const todos = state.todos;

      todos.splice(0, todos.length);
    },
    'API_FAIL': function (state, error) {
      console.log(error);
    },
  },
  actions: {
    getTodos ({commit}) {
      return api.get(apiRoot + 'todos/')
        .then(response => commit('GET_TODOS', response))
        .catch(error => commit('API_FAIL', error));
    },
    addTodo ({commit}, todo) {
      return api.post(apiRoot + 'todos/', todo)
        .then(response => commit('ADD_TODO', response))
        .catch(error => commit('API_FAIL', error));
    },
    clearTodos ({commit}) {
      return api.delete(apiRoot + 'todos/clear_todos/')
        .then(response => commit('CLEAR_TODOS'))
        .catch(error => commit('API_FAIL', error));
    },
  },
});

export default store;
