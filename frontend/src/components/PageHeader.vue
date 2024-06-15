<script setup lang="ts">
import { defineProps } from 'vue'

interface Prop {
  title: string
}

defineProps<Prop>()
</script>

<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
</template>

<style lang="scss" scoped>
header {
  width: 100%;
  height: 5rem;
  color: $color-text-header;
  background-color: $color-background-header;
}
</style>
