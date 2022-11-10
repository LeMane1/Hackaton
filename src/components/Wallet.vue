<template>
  <div class="wallet-selector-wrapper">
    <h3 class="block-title">Кошелек</h3> 
    <div class="perevod-wrapper">
        <div>
            <p class="coin-count">
                {{curAURC}} AURC
            </p>
            <p class="coin-count">
                {{curAUC}} AUC
            </p>
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
            metals: [
                {
                    name:'Золото',
                    chamName: 'Au',
                    index:0
                },
                {
                    name:'Серебро',
                    chamName:'Ag',
                    index:1
                },
                {
                    name:'Платина',
                    chamName:'Pt',
                    index:2
                }
            ],
            curAURC: "",
            curAUC: "",
        };
    },
    async mounted() {
        try {
            this.curAURC = await this.sendReq(
            "http://localhost:8000/api/users/get_acc_balance?user_id=1&currency=AURC",
            "GET"
        )
        this.curAURC = this.curAURC[0]
        } catch (error) {
            this.curAURC = 0
        }
        try {
            this.curAUC = await this.sendReq(
            "http://localhost:8000/api/users/get_acc_balance?user_id=1&currency=PDC",
            "GET"
        )
        this.curAUC = this.curAUC[0]
        } catch (error) {
            this.curAUC = 0
        }
        
    }
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

    .block-title{
        font-size:40px;
        font-weight: bold;
        margin-bottom: 20px;
        margin-top:10px;
    }

    .coin-count{
        font-size: 17px;
        font-weight: bold;
        margin-bottom: 15px;
    }
</style>