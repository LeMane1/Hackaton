<template>
  <div class="wallet">
    <MetalSelector/>
  </div>
</template>

<script>
import MetalSelector from '@/components/MetalSelector.vue'
export default {
  name: 'Wallet',
  components: {
    MetalSelector
  }
}
</script>


<style scoped>
    .wallet{
      padding: 20px 20px;
    }
</style>
