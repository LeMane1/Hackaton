<template>
  <header>
        <div v-if="this.user" key="userName">
            {{this.user}}
        </div>
        <button v-else key="enter" class="button-enter">
          <p class="header-button">Войти</p>
      </button>
  </header>
</template>

<script>
import CallApi from "../mixins/callApi";
export default {
    mixins: [CallApi],
    data() {
        return {
            user: "Nikolay",
        };
    }
}
</script>

<style scoped>
    header{
        position: fixed;
        left:0;
        top:0;
        right:0;
        width:100%;
        height:60px;
        display: flex;
        align-items: center;
        justify-content: right;
        flex-wrap: wrap;
        z-index:1000;
    }

    .button-enter{
        padding: 10px 20px;
        border-radius: 6px;
        background-color: #2c3e50;
        color:white;
        font-size: 15px;
        margin-right: 40px;
        border:none;
    }

    .button-enter:hover{
        background-color: white;
        border: 1px solid #2c3e50;
        color: #2c3e50;
    }
</style>