<script lang="ts">
    export default {
        props: ['itemId'],
        data() {
            return {
                getResult: null,
            }
        },
        methods: {
            async postBid() {
                const postData = {
                    bid: (this.$refs.post_bid as any).value,
                }
                try {
                    if (postData.bid != null) {
                        console.log((this.itemId as number));
                        const res = await fetch(`http://localhost:8000/placeBid/${(this.itemId as number)}`, { 
                            method: "post", 
                            headers: {
                                "Content-Type": "application/json"
                            }, 
                            body : JSON.stringify(postData),
                            'credentials': "include",
                        });
                        if (!res.ok) {
                            
                            const message = `An error has occured: ${res.status} - ${res.statusText}`;
                            throw new Error(message);
                        }

                        const data = await res.json();

                        const result = {
                            status: res.status + "-" + res.statusText,
                            headers: {
                                "Content-Type": res.headers.get("Content-Type"),
                                "Content-Length": res.headers.get("Content-Length"),
                            },
                            data: data,
                        };

                        this.getResult = data;
                    }
                    else {console.warn("question is empty");}

                } catch (err) {
                    console.error(err);
                }
            },
        },
    }
</script>


<template>
  <header>
    <div class="bg-light rounded shadow p-3">
        <b>please enter your bid</b>
        <form id="postBid" action="">
            <div class="form-group shadow rounded">
                <input class="form-control" type="number" name="bid" ref="post_bid" placeholder="10" required/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" @click="postBid">SUBMIT BID</button>
            </div>
        </form>
      </div>
  </header>
</template>