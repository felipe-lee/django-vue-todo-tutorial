// src/components/UserInput.vue

<template>
  <div id="user-inputs">
    <label for="new-todo">Add a new item:</label>
    <input id="new-todo" v-model="newTodoText" v-on:keyup.enter="createTodo">
    <button v-on:click="clearTodos">
      Clear
    </button>
  </div>
</template>

<script>
  export default {
    name: 'UserInput',
    data: function () {
      return {newTodoText: ''}
    },
    methods: {
      createTodo () {
        this.$store.dispatch('addTodo', {text: this.newTodoText});
        this.newTodoText = '';
      },
      clearTodos () {
        this.$store.dispatch('clearTodos');
      }
    }
  }
</script>

<style scoped>

</style>
