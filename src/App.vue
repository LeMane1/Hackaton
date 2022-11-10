<template>
  <div id="app">
    <Header/>
    <div class="nav-wrapper">
      <div class="nav">
        <router-link to="/transfer" class="router-link">Перевод</router-link>
        <router-link to="/" class="router-link">Кошелек</router-link>
        <router-link to="/account" class="router-link">Мой аккаунт</router-link>
      </div>
    </div>
    <router-view class="router-view"/>
  </div>
</template>

<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>


<style>

@import 'assets/styles/reset.css';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

body{
  background-color: rgb(225, 225, 225);
}

.nav-wrapper{
  width:300px;
  height:100vh;
  /* background-color: rgb(230, 230, 230); */
  position: absolute;
  left:0;
}

.nav {
  width:100%;
  display: flex;
  flex-wrap: wrap;
  margin-top: 100px;
}

.router-link{
  padding: 16px 40px;
  width:100%;
  font-size: 20px;
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  color:rgb(31, 31, 31);
  margin-bottom: 20px;
  margin-left:20px;
  border-radius: 15px;
}

.router-link:hover{
   background-color:rgb(248, 248, 248);
}

.router-link-exact-active{
  background-color: white;
}

.router-view{
  margin-left:400px;
  margin-top:60px;
}
</style>
