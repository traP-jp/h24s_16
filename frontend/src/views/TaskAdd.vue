<script setup lang="ts">
import '@mdi/font/css/materialdesignicons.css'
import { ref } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import PageContainer from '@/components/PageContainer.vue'
import apiClient from '@/apis'
import type { User, CreateTaskReqDTO, Group } from '@/apis/generated'
import PrimaryButton from '@/components/PrimaryButton.vue'
import router from '@/router'

const user = ref<User>({
  id: '',
  name: '',
  remind_channel_id: '',
  periodic_remind_at: '',
  created_at: '',
  updated_at: ''
})
const userGroups = ref<Group[]>([])

apiClient.default.getUserUsersMeGet().then((res) => (user.value = res))
apiClient.default.getUserGroupsUsersGroupsGet().then((res) => (userGroups.value = res))

const datePickerDisplay = ref(false)

const newTask = ref<CreateTaskReqDTO>({
  title: '',
  content: '',
  due_date: '',
  group_id: '',
  label_ids: [],
  assigned_user_ids: []
})

const openDatePicker = () => {
  datePickerDisplay.value = !datePickerDisplay.value
}

const createTask = () => {
  apiClient.default.createTaskTasksPost(newTask.value).catch((v) => console.log(v))

  newTask.value = {
    title: '',
    content: '',
    due_date: '',
    group_id: '',
    label_ids: [],
    assigned_user_ids: []
  }
}
</script>

<template>
  <PageHeader title="新規タスクの追加" :username="user.name" />
  <div>
    <PageContainer>
      <div class="field">
        <v-text-field v-model="newTask.title" label="タスク名" clearable />
        <v-text-field v-model="newTask.assigned_user_ids" label="アサイン先(@で指定)" clearable />
        <v-text-field v-model="newTask.due_date" label="期日" readonly clearable>
          <template v-slot:prepend>
            <v-btn class="secondary-button" icon @click="openDatePicker">
              <v-icon>mdi-calendar</v-icon>
            </v-btn>
          </template>
          <v-date-picker v-if="datePickerDisplay === true"></v-date-picker>
        </v-text-field>
        <v-textarea rows="5" v-model="newTask.content" label="内容" clearable />
        <v-combobox v-model="newTask.assigned_user_ids" chips multiple label="ラベル" clearable />
        <v-row class="justify-end">
          <div @click="createTask">
            <button class="secondary-button" @click="router.push({ name: 'TaskList' })">
              もとのページに戻る
            </button>
            <PrimaryButton text="作成" />
          </div>
        </v-row>
      </div>
    </PageContainer>
  </div>
</template>

<style lang="scss" scoped>
.field {
  width: 80%;
  margin: 0 10%;
}
.secondary-button {
  padding: 8px 16px; /* ボタンの内側の余白 */
  background-color: #777777; /* ボタンのテキスト色 */
  border-radius: 5px; /* 枠を丸くする */
  color: white;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border: none; /* ボーダーを削除 */
  cursor: pointer; /* ホバー時にカーソルをポインターにする */
  top: 0;
  margin-right: 4px;

  &:hover {
    background-color: #444444;
  }
}
</style>
