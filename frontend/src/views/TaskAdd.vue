<script setup lang="ts">
import '@mdi/font/css/materialdesignicons.css'
import { ref } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import PageContainer from '@/components/PageContainer.vue'
import apiClient from '@/apis'
import type { User, CreateTaskReqDTO } from '@/apis/generated'
import PrimaryButton from '@/components/PrimaryButton.vue'

const user = ref<User>({
  id: '',
  remind_channel_id: '',
  periodic_remind_at: '',
  created_at: '',
  updated_at: ''
})

apiClient.default.getUserUsersMeGet().then((res) => (user.value = res))

const datePickerDisplay = ref(false)

const newTask = ref<CreateTaskReqDTO>({
  title: 'string',
  content: 'string',
  due_date: 'string',
  group_id: 'string',
  // labels: [],
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
    // labels: [],
    assigned_user_ids: []
  }
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
        <v-text-field v-model="newTask.title" label="タスク名" clearable />
        <v-text-field v-model="newTask.assigned_user_ids" label="アサイン先(@で指定)" clearable />
        <v-text-field v-model="newTask.due_date" label="期日" readonly clearable>
          <template v-slot:prepend>
            <v-btn icon @click="openDatePicker">
              <v-icon>mdi-calendar</v-icon>
            </v-btn>
          </template>
          <v-date-picker v-if="datePickerDisplay === true"></v-date-picker>
        </v-text-field>
        <v-textarea rows="5" v-model="newTask.content" label="内容" clearable />
        <v-combobox v-model="newTask.assigned_user_ids" chips multiple label="ラベル" clearable />
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
