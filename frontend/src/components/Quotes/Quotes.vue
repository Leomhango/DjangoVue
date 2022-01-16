<template>
    <div class="flex flex-col justify-center items-center mt-5">
        <div class="flex flex-col space-y-3 border-2 md:border shadow md:shadow-xl px-5 py-5 md:px-16 md:py-10 my-2 md:my-5 w-11/12 md:w-10/12 rounded-md" v-for="quote in quotes" :key="quote.id">
            <p class="text-green-500 font-semibold text-xl">{{ quote.quotee }}</p>
            <p class="text-lg font-medium text-gray-700 capitalize">"{{ quote.description }}..."</p>
        </div>
    </div>
</template>

<script>
    export default{
        name: "Quote",
        props: ['quotes']
    }
</script>