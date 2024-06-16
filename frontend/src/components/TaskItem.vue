<script setup lang="ts">
import { ref } from 'vue'
import type { TaskDetails } from '@/apis/generated'

const openDetail = ref<boolean>(false)

interface Props {
  task: TaskDetails
}

defineProps<Props>()
</script>

<template>
  <div class="task-container">
    <div class="task-title">{{ task.title }}</div>

    <div class="task-details">
      <p>期日：2024年6月15日</p>
      <!-- 詳細を表示のテキストを追加 -->
      <div v-if="openDetail == false" class="additional-details">
        <button class="detail-button" @click="openDetail = !openDetail">詳細を表示</button>
      </div>
    </div>

    <!-- 詳細情報を条件付きで表示 -->
    <div v-if="openDetail" class="additional-details">
      <!-- 隠されていた詳細情報 -->
      {{ task.content }}
    </div>

    <div v-if="openDetail" class="additional-details">
      <div class="button-right">
        <button class="close-button" @click="openDetail = !openDetail">閉じる</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.task-container {
  border: none;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px; /* 枠を丸くする */
  padding: 10px;
  margin: 15px 30px;
  background-color: white; /* 背景色を変更する */
  /* width: calc(100% - 230px);  */
}

.task-title {
  font-weight: bold; /* 太文字にする */
  font-size: 1.2em; /* フォントサイズを20%大きくする */
}
.task-details {
  display: flex;
  justify-content: space-between; /* 左右にコンテンツを分散 */
  align-items: center; /* 中央揃え */
  *{
    padding: 8px 0;
  }
}

.detail-button {
  padding: 8px 16px; /* ボタンの内側の余白 */
  color: $color-primary; /* ボタンのテキスト色 */
  border: none; /* ボーダーを削除 */
  cursor: pointer; /* ホバー時にカーソルをポインターにする */
  // margin-bottom: 3px; /* ボタンと詳細情報の間の余白 */
}

.detail-button:hover {
  text-decoration: underline;
}

.close-button {
  padding: 8px 16px; /* ボタンの内側の余白 */
  color: $color-primary; /* ボタンのテキスト色 */
  border: none; /* ボーダーを削除 */
  cursor: pointer; /* ホバー時にカーソルをポインターにする */
  // margin-bottom: 3px; /* ボタンと詳細情報の間の余白 */
}

.close-button:hover {
  text-decoration: underline;
}

.button-right {
  text-align: right;
}
</style>
