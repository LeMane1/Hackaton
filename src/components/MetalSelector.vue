<template>
  <div class="metal-selector-wrapper">
    <h3 class="block-title">Перевод</h3>
    <div class="perevod-wrapper">
        <div>
            <div class="selector-block">
                <img src="../assets/gold.png" alt="Металл" class="img-selector">
                <div>
                    <p class="form-title">Выберите драгоценный металл</p>
                    <select
                        v-model="selectedMetal"
                        class="metal-selector"
                    >
                        <option disabled value="">Выберите один из вариантов</option>
                        <option
                        v-for="metal in metals"
                        :key="metal.index"
                        :value="metal.index"
                        >
                        {{ metal.name }}
                        </option>
                    </select>
                </div>
                
            </div>

            <div class="selector-block">
                <img src="../assets/mass.png" alt="Масса" class="img-selector">
                <div>
                    <p class="form-title">Выберите массу металла в граммах</p>
                        <input type="number" v-model="choosenWeight" name="points" min="0" max="1000" step="0.001" value="1">
                </div>
            </div>

            <button @click="callApiSearch">
                Перевести
            </button>
        </div>

        <div class="arrow-wrapper">
            <img src="../assets/arrow.png" alt="Перевести" class="img-arrow">
        </div>

        <div class="counted-coin-wrapper">
            <div class="counted-coin" :style="{ backgroundColor: selectColor }">
                <h4 class="metal-name">{{selectMetal}}</h4>
                <h5 class="coin-name">StableCoin</h5>
                <h3 class="coin-count">{{(choosenWeight - choosenWeight*0.01).toFixed(5)}}</h3>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import CallApi from "../mixins/callApi";
export default {
    mixins: [CallApi],
    data() {
        return {
            selectedMetal: 0,
            selectedMass: "",
            metals: [
                {
                    name:'Золото',
                    chamName: 'Au',
                    color: '#ffd700',
                    index:0
                },
                {
                    name:'Серебро',
                    chamName:'Ag',
                    color: '#bac9d8',
                    index:1
                },
                {
                    name:'Платина',
                    chamName:'Pt',
                    color: '#e5f5b9',
                    index:2
                }
            ],
            choosenWeight: 0,
            buying: "0"
        };
    },
    computed: {                    
        selectMetal: function () {
            return this.metals.find(element => element.index === this.selectedMetal).chamName;
        },
        selectColor: function () {
            return this.metals.find(element => element.index === this.selectedMetal).color;
        }
    },
    methods:{
        async callApiSearch() {
            this.buying = await this.sendReq(
                "http://127.0.0.1:8000/api/marketplace/buy_currency/",
                "POST",
                { currency_type: "AURC", amount: this.choosenWeight, user_id: 1 }
            )
        },
    }
}
</script>

<style scoped>
    .metal-selector-wrapper{
        padding: 10px 20px;
        border-radius: 20px;
        box-shadow: 0 2px 5px 2px rgba(0, 0, 0, 0.1);
        background-color: white;
    }

    .perevod-wrapper{
        display: flex;
        flex-wrap:wrap;
        height:400px;
    }

    .form-title{
        font-size: 20px;
        font-weight: 500;
        margin-bottom: 10px;
    }

    .selector-block{
        width:100%;
        margin-bottom: 20px;
    }

    .metal-selector{
        padding: 10px;
    }

    .img-selector{
        width:50px;
        height:50px;
        margin-right: 10px;
    }

    .block-title{
        font-size:40px;
        font-weight: bold;
        margin-bottom: 10px;
        margin-top:10px;
    }

    button{
        padding: 10px 20px;
        border-radius: 6px;
        background-color: #2c3e50;
        color:white;
        font-size: 16px;
        margin-right: 40px;
        border:none;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
    }

    button:hover{
        background-color: white;
        border: 1px solid #2c3e50;
        color: #2c3e50;
    }

    .img-arrow{
        width:60px;
        height:60px;
    }

    .arrow-wrapper{
        height: 100%;
        width:100px;
        display: flex;
        flex-wrap:wrap;
        align-items:center;
        justify-content: center;
        margin-right:40px;
    }

    .counted-coin-wrapper{
        height:100%;
        display: flex;
        flex-wrap:wrap;
        align-items:center;
        justify-content: center;
    }

    .counted-coin{
        position: relative;
        width:100px;
        height:150px;
        border-radius: 15px;
        padding: 8px 10px;
    }

    .metal-name{
        font-size:30px;
        font-weight:bold;
        margin-bottom: 4px;
    }

    .coin-name{
        font-size:15px;
        font-weight: 400;
    }

    .coin-count{
        position: absolute;
        bottom:8px;
        right:10px;
        font-size:25px;
        font-weight: bold;
    }
</style>