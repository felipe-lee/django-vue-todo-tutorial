// src/components/Todo.vue

<template>
  <p>
    {{ todo.text }}
  </p>
</template>

<script>
  export default {
    props: ['todo']
  }
</script>

<style scoped>

</style>
