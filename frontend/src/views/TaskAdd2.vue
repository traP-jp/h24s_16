<script setup lang="ts">
import '@mdi/font/css/materialdesignicons.css'
import { ref } from 'vue'

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
  <div id="app">
    <v-app>
      <v-main>
        <v-layout>
          <v-card width="80em" variant="outlined" class="mx-auto">
            <v-container>
              <v-text-field v-mode="taskName" label="タスク名" clearable></v-text-field>
              <v-text-field v-model="assignee" label="アサイン先(@で指定)" clearable></v-text-field>
              <v-text-field v-mode="deadline" label="期日" readonly clearable>
                <template v-slot:prepend>
                  <v-btn icon @click="openDatePicker">
                    <v-icon>mdi-calendar</v-icon>
                  </v-btn>
                </template>
                <v-date-picker v-if="datePickerDisplay === true"></v-date-picker>
              </v-text-field>
              <v-text-field v-mode="content" label="内容" clearable></v-text-field>
              <v-text-field v-model="tags" label="タグ"></v-text-field>
              <v-row class="justify-center">
                <v-btn color="primary" variant="flat" @click="createTask"> 作成 </v-btn>
              </v-row>
            </v-container>
          </v-card>
        </v-layout>
      </v-main>
    </v-app>
  </div>
</template>
