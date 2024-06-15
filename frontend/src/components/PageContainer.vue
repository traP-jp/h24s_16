<template>
  <main>
    <slot />
  </main>
</template>

<style lang="scss" scoped>
main {
  width: 100%;
  height: 100%;
  max-width: 1024px;
  margin: 0 auto;
  padding: 4rem 3rem 3rem;
  overflow-x: auto;
  overflow-y: auto;
}
</style>
