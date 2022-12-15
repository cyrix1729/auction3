<script lang="ts">
import Answer from './Answer.vue';
import GetItem from './getItem.vue';
    export default {
    props: ["userId"],
    data() {
        return {
            getResult: null,
        };
    },
    methods: {
        async getQuestionsAskedToUser() {
            try {
                const res = await fetch(`http://localhost:8000/getQuestionsAskedToUser/${this.userId}`, { method: "get",
                        'credentials': "include", });
                if (!res.ok) {
                    const message = `An error has occured: ${res.status} - ${res.statusText}`;
                    throw new Error(message);
                }
                const data = await res.json();
                if (data.ObjectsFound){
                    delete data.ObjectsFound;
                    this.getResult = data;
                }
            }
            catch (err) {
                console.error(err);
            }
        },
    },
    created() {
        this.getQuestionsAskedToUser();
    },
    components: { Answer, GetItem }
}
</script>


<template>
  <header>
    <div class="">
        <h1>Questions asked about your items</h1>
        <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
            <div class="row" v-for="item in getResult">
                <div class="col-sm-12 text-center">
                    <GetItem :itemId="item.itemId" :showFullData="false"/>
                    <div class="row" v-for="question in item.question">
                        <b class = "w-25 p-3">{{ question.question}}</b>
                    </div>
                </div>
                <div class="col-sm-12 text-center">
                    <b v-if="item.answer" class = "w-25 p-3">{{ item.answer }}</b>
                    <b v-else><Answer v-bind:questionId="item.id"/></b>
                </div>
            </div>
        </div>
        <div v-else>
            <b>You haven't been asked any questions about items you've listed</b>
        </div>
      </div>
  </header>
</template>