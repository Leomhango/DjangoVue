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
          url: 'http://localhost:8000/quotes',
          auth: {
            username: 'leomhango',
            password: '1234'
          }
        }).then(response => this.quotes = response.data)
      }
    }
  }

</script>