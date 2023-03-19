<template >
    <div class="flex flex-col justify-center items-center">
        <div class="flex flex-col justify-center items-center border-2 shadow-xl rounded-xl w-11/12 py-10 px-10">
            <h1 class="text-green-500 text-2xl font-semibold my-5">Add a quote</h1>
            <form class="flex flex-col w-full space-y-4" v-on:submit.prevent="addQuote">
                <input class="border py-2 px-4" type="text" v-model="quotee" placeholder="Enter Name">
                <textarea class="border py-2 px-4" name="" id="" cols="30" rows="10" placeholder="Enter Quote"
                    v-model="description"></textarea>
                <button type="submit" class="bg-green-500 font-semibold text-white py-2 px-10">Submit</button>

            </form>
        </div>

    </div>
</template>

<script>
import AddQuote from '@/components/AddQuote/AddQuote.vue';

import axios from 'axios'

export default {
    name: 'Add',
    components: {
        AddQuote
    },
    data() {
        return {
            quotes: [],
            quotee: '',
            description: ''
        }
    },
    methods: {
        addQuote() {
            if (this.quotee && this.description) {
                axios({
                    method: 'post',
                    url: 'http://localhost:8000/quotes/',
                    data: {
                        quotee: this.quotee,
                        description: this.description
                    },
                    auth: {
                        username: 'leomhango',
                        password: '1234'
                    }
                }).then((response) => {
                    let newQuote = {
                        'id': response.data.id,
                        'quotee': this.quotee,
                        'description': this.description,
                    }

                    this.quotes.push(newQuote)

                    this.quotee = ''
                    this.description = ''
                }).catch((error) => {
                    console.log(error)
                })
            }
        }
    }
}
</script>