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

const datePickerDisplay = ref(false)

const openDatePicker = () => {
  datePickerDisplay.value = !datePickerDisplay.value
}
</script>

<template>
  <PageHeader title="新規タスクの追加" :username="user.id" />
  <div>
    <PageContainer>
      <div class="field">
        <v-text-field label="タスク名" clearable> </v-text-field>
        <v-text-field label="アサイン先(@で指定)" clearable> </v-text-field>
        <v-text-field label="期日" readonly clearable>
          <template v-slot:prepend>
            <v-btn icon @click="openDatePicker">
              <v-icon>mdi-calendar</v-icon>
            </v-btn>
          </template>
          <v-date-picker v-if="datePickerDisplay === true"></v-date-picker>
        </v-text-field>
        <v-text-field label="内容" clearable> </v-text-field>
        <v-text-field label="タグ"> </v-text-field>
        <v-row class="justify-center">
          <PrimaryButton text="作成" />
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
