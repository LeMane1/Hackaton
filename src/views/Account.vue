<template>
  <div class="wallet">
    <BankWallet/>
  </div>
</template>

<script>
import BankWallet from '@/components/BankWallet.vue'
export default {
  name: 'Account',
  components: {
    BankWallet
  }
}
</script>


<style scoped>
    .wallet{
      padding: 20px 20px;
    }
</style>