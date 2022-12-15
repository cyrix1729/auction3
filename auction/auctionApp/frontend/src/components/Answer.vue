<template>
    <header>
      <div class="">
          <b>please post your answer</b>
          <form id="postAnswer" action="">
              <div class="form-group">
                  <input class="form-control" type="text" name="name" ref="post_answer" placeholder="put your answer here" required/>
              </div>
              <div class="form-group">
                  <button class="btn btn-primary" @click="postAnswer">SUBMIT</button>
              </div>
          </form>
        </div>
    </header>
  </template>

<script lang="ts"> 
    export default {
        props: ['questionId'],
        data() {
            return {
                getResult: null,
            }
        },
        methods: {
            async postAnswer() {
                const postData = {
                    answer: (this.$refs.post_answer as any).value,
                }
                try {
                    const res = await fetch(`http://localhost:8000/postAnswer/${this.questionId}`,
                        { method: "post", headers: {"Content-Type": "application/json"}, 
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

                } catch (err) {
                    console.error(err);
                }
            },
        },
    }
</script>