<script setup lang="ts">
import { ref } from 'vue'
import PrimaryButton from '@/components/PrimaryButton.vue'
import PageContainer from '@/components/PageContainer.vue'
import PageHeader from '@/components/PageHeader.vue'
import TaskItem from '@/components/TaskItem.vue'

interface Task {
  id: string
  title: string
  content: string
  showDetails: boolean // 詳細表示の状態を追加
}

interface Group {
  name: string
}

const tasks = ref<Task[]>([
  {
    id: '1',
    title: 'タスク１',
    content:
      '内容１あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
    showDetails: false
  },
  { id: '2', title: 'タスク２', content: '内容２', showDetails: false },
  { id: '2', title: 'タスク3', content: '内容３', showDetails: false }
])

const groups = ref<Group[]>([
  { name: 'グループ１' },
  { name: 'グループ２' },
  { name: 'グループ３' }
])

// 詳細表示の切り替え関数
const toggleDetails = (task: Task) => {
  task.showDetails = !task.showDetails
}
</script>

<template>
  <PageHeader title="タスク一覧" />
  <div class="pageContents">
    <!-- サイドバー -->
    <div class="sidebar">
      <ul>
        <li v-for="group in groups" :key="group.name">
          <div>{{ group.name }}</div>
        </li>
      </ul>
      <router-link :to="{ name: 'TaskAdd' }">
        <PrimaryButton text="新規タスクを追加" />
      </router-link>
    </div>
    <PageContainer>
      <!-- タスク一覧表示 -->
      <div>
        <ul>
          <li v-for="task in tasks" :key="task.id">
            <div class="task-container">
              <div class="task-title">{{ task.title }}</div>

          <div class="task-details">
            <p>期日：2024年6月15日</p>
            <!-- 詳細を表示ボタン -->
            <div v-if="task.showDetails == false" class="additional-details">
            <button class="detail-button" @click="toggleDetails(task)">詳細を表示</button>
          </div>
          </div>

          <!-- 詳細情報を表示 -->
          <div v-if="task.showDetails" class="additional-details">
            {{task.content}}
          <div>
            <button class="close-button" @click="toggleDetails(task)">閉じる</button>
          </div>
          </div>

        </div>
      </li>
    </ul>
  </div>
</PageContainer>
  </div>



  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<style lang="scss" scoped>
.sidebar {
  background-color: #ffffff;
  min-width: 200px;
  max-width: 500px;
  height: 100%;
  padding: 60px 30px; /* Adjust this value to match the height of your header */
  overflow: auto;
}

.sidebar li {
  margin-bottom: 20px; /* Adjust this value to increase or decrease the space */
}

.task-container {
  border: none;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px; /* 枠を丸くする */
  padding: 10px;
  margin: 15px;
  margin-left: 230px;
  margin-right: 30px;
  /* margin-right: 30px; */
  background-color: white; /* 背景色を変更する */
  /* width: calc(100% - 230px);  */
}

.task-title {
  font-weight: bold; /* 太文字にする */
  font-size: 1.2em; /* フォントサイズを20%大きくする */
}

ul {
  list-style-type: none; /* 中黒を消す */
}

/* 詳細ボタンのスタイル */
.task-details {
  display: flex;
  justify-content: space-between; /* 左右にコンテンツを分散 */
  align-items: center; /* 中央揃え */
}

.detail-button {
  padding: 8px 16px; /* ボタンの内側の余白 */
  color: $color-primary; /* ボタンのテキスト色 */
  border: none; /* ボーダーを削除 */
  cursor: pointer; /* ホバー時にカーソルをポインターにする */
  margin-bottom: 3px; /* ボタンと詳細情報の間の余白 */
}

.detail-button:hover {
  text-decoration: underline; /* 下線を表示 */
}

.close-button {
  padding: 8px 16px; /* ボタンの内側の余白 */
  color: #6AA2B4; /* ボタンのテキスト色 */
  cursor: pointer; /* ホバー時にカーソルをポインターにする */
}

.close-button:hover {
  text-decoration: underline; /* 下線を表示 */
}

/* グループ選択 */
.groupSelect-button {
  font-weight: bold; /* 太文字にする */
}

.groupSelect-button:hover {
  text-decoration: underline; /* 下線を表示 */
}
.pageContents {
  height: calc(100% - 5rem);
  display: grid;
  grid-template-columns: 1fr 5fr;
  align-content: center;
}

@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
  .task-container {
    margin-left: 230px; /* サイドバーの幅 + 30px の余白を確保 */
    margin-right: 30px;
    /* width: calc(100% - 230px); 全体の幅からサイドバーの幅を引く */
  }
}
</style>
