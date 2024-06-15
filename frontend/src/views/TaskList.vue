<script setup lang="ts">
import { ref } from 'vue'

interface Task {
  id: string
  title: string
}

interface Group {
  name: string
}

const tasks = ref<Task[]>([
  { id: '1', title: 'タスク１'},
  { id: '2', title: 'タスク２'}
])

const groups = ref<Group[]>([
  { name: 'グループ１'},
  { name: 'グループ２'},
  { name: 'グループ３'},
])

</script>



<template>
  <!-- トップバー
  <header class = "header">
    <h1>Header</h1>
  </header> -->

  <!-- サイドバー -->
  <div class="sidebar">
    <ul>
      <p v-for="group in groups" :key="group.name" >
        <div>{{ group.name }}</div>
      </p>
    </ul>
  </div>

  <!-- タスク一覧表示 -->
  <div>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <div class="task-container">
          <div class="task-title">{{ task.title }}</div>
          <p>期日：2024年6月15日</p>
        </div>
      </li>
    </ul>
  </div>



  <div class="about">
    <h1>This is an about page</h1>
  </div>
  <p style="color: black;">ぐおおおおお</p>
  <p style="color: black;">わああ</p>

  <ul>
      <p v-for="task in tasks" :key="task.title" >
        <div>名前: {{ task.title }}</div>
      </p>
  </ul>
  
</template>

<style>
.header {
  background-color: #464646;
  color: white;
  text-align: center;
  position: fixed;
  width: 100%;
  left: 0;
  top: 0;
  z-index: 1;
}

.sidebar {
  background-color: #ffffff;
  position: fixed;
  width: 200px;
  height: 100%;
  left: 0;
  top: 0;
  padding-top: 60px; /* Adjust this value to match the height of your header */
  padding-left: 30px;
  overflow: auto;
}

.sidebar p {
  margin-bottom: 20px; /* Adjust this value to increase or decrease the space */
}

.task-container {
  border: none;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px; /* 枠を丸くする */
  padding: 10px;
  margin: 15px;
  margin-left: 230px;
  /* margin-right: 30px; */
  background-color: white; /* 背景色を変更する */
  width: calc(100% - 200px); 
}

.task-title {
  font-weight: bold; /* 太文字にする */
  font-size: 1.2em; /* フォントサイズを20%大きくする */
}

ul {
  list-style-type: none; /* 中黒を消す */
}


@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
  .task-container {
    margin-left: 200px; /* サイドバーの幅 + 30px の余白を確保 */
    width: calc(100% - 200px); /* 全体の幅からサイドバーの幅を引く */
  }
}


</style>
