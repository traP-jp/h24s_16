<script setup lang="ts">
import { defineProps } from 'vue'

interface Prop {
  title: string
  username: string
}

defineProps<Prop>()
</script>

<template>
  <header>
    <h1>{{ title }}</h1>
    <img
      :src="`https://q.trap.jp/api/v3/public/icon/${username}`"
      alt=""
      width="30px"
      height="30px"
    />
    <span>
      <h3>{{ username }}</h3>
    </span>
  </header>
</template>

<style lang="scss" scoped>
header {
  display: flex;
  align-items: center;
  width: 100%;
  height: 5rem;
  padding: 0 1rem;
  color: $color-text-header;
  background-color: $color-background-header;
}

h1 {
  margin-right: auto;
}

span {
  display: flex;
  margin-right: 0;
}

img {
  width: 2rem;
  height: 2rem;
  border-radius: 1rem;
  margin: 3%;
}
</style>
