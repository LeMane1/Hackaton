<template>
  <div class="wallet-selector-wrapper">
    <h3 class="block-title">Мой аккаунт</h3>
    <div class="perevod-wrapper">
        <p class="bank-wallet-title">Банковские счета</p>
        <p class="wallet-name">Металлический счет AUG</p>
        <p class="wallet-count">203 09 098 9 0020300103</p>
        <p class="wallet-name">Металлический счет AU</p>
        <p>203 09 098 9 0020300104</p>
    </div>
    <button class="btn-add-wallet">Добавить счет</button>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
    .wallet-selector-wrapper{
        padding: 20px 30px;
        border-radius: 20px;
        box-shadow: 0 2px 5px 2px rgba(0, 0, 0, 0.1);
        background-color: white;
        margin-right: 50px;
    }

    .perevod-wrapper{
        display: flex;
        flex-wrap:wrap;
        flex-direction: column;
    }

    .bank-wallet-title{
        font-size:20px;
        margin-bottom: 10px;
    }

    .wallet-name{
        font-size:14px;
        opacity: 0.7;
        margin-bottom: 8px;
    }

    .wallet-count{
        font-size:18px;
        margin-bottom: 10px;
    }

    .btn-add-wallet{
        padding: 10px 20px;
        border-radius: 6px;
        background-color: #2c3e50;
        color:white;
        font-size: 15px;
        border:none;
        margin-top:20px;
    }

    .btn-add-wallet:hover{
        background-color: white;
        border: 1px solid #2c3e50;
        color: #2c3e50;
    }

    .block-title{
        font-size:40px;
        font-weight: bold;
        margin-bottom: 10px;
        margin-top:10px;
    }
</style>