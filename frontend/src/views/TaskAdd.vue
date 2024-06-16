<script setup lang="ts">
import '@mdi/font/css/materialdesignicons.css'
import { ref } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import PageContainer from '@/components/PageContainer.vue'
import apiClient from '@/apis'
import type { User } from '@/apis/generated'
import PrimaryButton from '@/components/PrimaryButton.vue'

const user = ref<User>({
  id: '',
  remind_channel_id: '',
  periodic_remind_at: '',
  created_at: '',
  updated_at: ''
})

apiClient.default.getUserUsersMeGet().then((res) => (user.value = res))

interface task {
  taskName: string
  assignee: string
  deadline: string
  content: string
  tags: string[]
}

const datePickerDisplay = ref(false)
const taskName = ref('')
const assignee = ref('')
const deadline = ref('')
const content = ref('')
const tags = ref<string[]>([])
const tasks = ref<task[]>([])

const openDatePicker = () => {
  datePickerDisplay.value = !datePickerDisplay.value
}

const createTask = () => {
  // 新しいタスクオブジェクトを作成
  const newTask: task = {
    taskName: taskName.value,
    assignee: assignee.value,
    deadline: deadline.value,
    content: content.value,
    tags: tags.value
  }

  // タスクリストに追加
  tasks.value.push(newTask)

  // 入力フィールドをクリア
  taskName.value = ''
  assignee.value = ''
  deadline.value = ''
  content.value = ''
  tags.value = []
}
</script>

<template>
  <PageHeader title="新規タスクの追加" :username="user.id" />
  <div>
    <PageContainer>
      <div class="field">
        <v-row class="justify-end">
          <v-btn icon variant="flat">
            <v-icon>mdi-close-circle-outline</v-icon>
          </v-btn>
        </v-row>
        <v-text-field v-model="taskName" label="タスク名" clearable />
        <v-text-field v-model="assignee" label="アサイン先(@で指定)" clearable />
        <v-text-field v-model="deadline" label="期日" readonly clearable>
          <template v-slot:prepend>
            <v-btn icon @click="openDatePicker">
              <v-icon>mdi-calendar</v-icon>
            </v-btn>
          </template>
          <v-date-picker v-if="datePickerDisplay === true"></v-date-picker>
        </v-text-field>
        <v-textarea rows="5" v-model="content" label="内容" clearable />
        <v-combobox v-model="tags" chips multiple label="タグ" clearable />
        <v-row class="justify-center">
          <div @click="createTask">
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
</style>
