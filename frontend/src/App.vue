<script setup lang="ts">
import { RouterView } from 'vue-router'
import PageHeader from './components/PageHeader.vue';
</script>

<template>
  <PageHeader title="新規タスク登録" username="ぷぐま"/>
  <RouterView />
</template>
