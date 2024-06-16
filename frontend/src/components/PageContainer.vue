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
  padding: 2rem 1.5rem;
  overflow-x: auto;
  overflow-y: auto;
}
</style>
