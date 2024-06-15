<script setup lang="ts">
import '@mdi/font/css/materialdesignicons.css'
import { ref } from 'vue';

const datePickerDisplay = ref(false);

const openDatePicker = () => {
  datePickerDisplay.value = !datePickerDisplay.value;
}
</script>

<template>
  <div id="app">
    <v-app>
    <v-main>
      <v-layout>
        <v-card width="80em" variant="outlined" class="mx-auto">
          <v-container>
            <v-text-field label="タスク名" clearable>

            </v-text-field>
            <v-text-field label="アサイン先(@で指定)" clearable>

            </v-text-field>
            <v-text-field label="期日" readonly clearable>
              <template v-slot:prepend>
                <v-btn icon @click="openDatePicker">
                  <v-icon>mdi-calendar</v-icon>
                 </v-btn>
              </template>
              <v-date-picker v-if="datePickerDisplay===true"></v-date-picker>
            </v-text-field>
            <v-text-field label="内容" clearable>

            </v-text-field>
            <v-text-field label="タグ">

            </v-text-field>
            <v-row class="justify-center">
              <v-btn color="primary" variant="flat">
                作成
              </v-btn>
            </v-row>
          </v-container>
        </v-card>
      </v-layout>
    </v-main>
    </v-app>
  </div>
</template>
