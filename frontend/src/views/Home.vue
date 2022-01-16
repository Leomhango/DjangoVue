<template>
  <Quotes :quotes="quotes"/>
</template>

<script>
  import Quotes from '@/components/Quotes/Quotes.vue'

  import axios from 'axios'

  export default{
    name: 'Home',
    components: {
      Quotes
    },
    data() {
      return{
        quotes: []
      }
    },
    mounted() {
      this.getQuotes()
    },
    methods: {
      getQuotes() {
        axios({
          method: 'get',
          url: 'http://192.168.0.112:8000/quotes',
          auth: {
            username: 'Skye',
            password: 'renegade123'
          }
        }).then(response => this.quotes = response.data)
      }
    }
  }

</script>