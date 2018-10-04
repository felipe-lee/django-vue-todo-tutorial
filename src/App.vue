// src/App.vue

<template>
  <div id="app">
    <user-input></user-input>
    <todo-list></todo-list>
  </div>
</template>

<script>
  import UserInput from './components/UserInput';
  import TodoList from './components/TodoList';

  export default {
    name: 'app',
    components: {TodoList, UserInput},
}
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
}

</style>
