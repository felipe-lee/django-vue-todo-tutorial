// src/components/Todo.vue

<template>
  <li>
    {{ todo.text }}
  </li>
</template>

<script>
  export default {
    props: ['todo']
  }
</script>

<style scoped>

</style>
