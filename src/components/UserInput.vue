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
        console.log(this.newTodoText, 'created!')
      },
      clearTodos () {
        console.log('Todos cleared!')
      }
    }
  }
</script>

<style scoped>

</style>
