<script setup lang="ts">
import { ref } from 'vue'
import PrimaryButton from '@/components/PrimaryButton.vue'
import PageContainer from '@/components/PageContainer.vue'
import PageHeader from '@/components/PageHeader.vue'
import TaskItem from '@/components/TaskItem.vue'
import apiClient from '@/apis'
import type { User, GroupDetails, TaskDetails } from '@/apis/generated'

apiClient.default.getUserUsersMeGet().then((res) => (user.value = res))
apiClient.default.getUserGroupsUsersGroupsGet().then((res) => (userGroups.value = res))

const user = ref<User>({
  id: '',
  remind_channel_id: '',
  periodic_remind_at: '',
  created_at: '',
  updated_at: ''
})

const userGroups = ref<GroupDetails[]>([
  {
    id: 'Hackathon 24 spring 16',
    remind_channel_id: 'ぐおおおおお',
    periodic_remind_at: 'ああああああああ',
    created_at: 'string',
    updated_at: 'string',
    user_ids: ['Pugma', 'ayana']
  }
])

const selectedGroup = ref<string>('自分のタスク全体')

const tasks = ref<TaskDetails[]>([
{
  title: 'タイトル',
  content:'内容',
  message_id: '',
  due_date: '6月15日',
  id: '',
  group_id: '',
  created_at: '',
  updated_at: '',
  assigned_user_ids: ['ayana']
}
])
</script>

<template>
  <PageHeader title="タスク一覧" :username="user.id" />
  <div class="pageContents">
    <!-- サイドバー -->
    <div class="sidebar">
      <ul>
        <li class="topLevel">
          <button @click="selectedGroup = '自分のタスク全体'">自分のタスク全体</button>
        </li>
        <li v-for="group in userGroups" :key="group.id">
          <button @click="selectedGroup = group.id">{{ group.id }}</button>
        </li>
      </ul>
    </div>
    <PageContainer>
      <div style="display: flex">
        <h2>{{ selectedGroup }}</h2>
        <button>自分のタスク</button>
        <button>タグ</button>
        <router-link :to="{ name: 'TaskAdd' }">
          <PrimaryButton text="新規タスクを追加" />
        </router-link>
      </div>
      <!-- タスク一覧表示 -->
      <ul>
        <li v-for="task in tasks" :key="task.id">
          <TaskItem :task="task" />
        </li>
      </ul>
    </PageContainer>
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
  li {
    padding: 10px 0; /* Adjust this value to increase or decrease the space */
    list-style-type: none; /* 中黒を消す */
    font-size: 1.05rem;
    font-weight: 700;
  }
  .topLevel {
    border-bottom: 2px solid #dddddd;
  }
}

.task-title {
  font-weight: bold; /* 太文字にする */
  font-size: 1.2em; /* フォントサイズを20%大きくする */
}

.pageContents {
  height: calc(100% - 5rem);
  display: grid;
  grid-template-columns: 1fr 5fr;
  h2{
    flex-grow: 1;
  }
  li {
  list-style-type: none; /* 中黒を消す */
  }
}
</style>
