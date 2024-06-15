<script setup lang="ts">
</script>

<template>
  <div id="app">
    <v-app>
    <v-main>
      <v-layout>
        <v-card width="80em" variant="outlined" class="mx-auto">
          <v-container>
            <v-text-field label="タスク名">

            </v-text-field>
            <v-text-field label="アサイン先(@で指定)">

            </v-text-field>
            <v-text-field label="項目">

            </v-text-field>
            <v-text-field label="内容" class="h-30">

            </v-text-field>
            <v-text-field label="タグ">

            </v-text-field>
            <v-row class="justify-center">
              <v-btn color="primary" variant="outlined">
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
