<script setup lang="ts">
interface Props {
  text: string
}
defineProps<Props>()
</script>

<template>
  <button>{{ text }}</button>
</template>

<style lang="scss" scoped>
button {
  padding: 8px 16px; /* ボタンの内側の余白 */
  background-color: $color-primary; /* ボタンのテキスト色 */
  border-radius: 5px; /* 枠を丸くする */
  color: white;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border: none; /* ボーダーを削除 */
  cursor: pointer; /* ホバー時にカーソルをポインターにする */
  top: 0;

  &:hover {
    background-color: #6a97a7;
  }
}
</style>
