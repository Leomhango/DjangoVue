<template>
    <div>
        <form v-on:submit="AddQuote" action="">
            <h1>Add a quote</h1>

            <div>
                <label for="">name</label>
                <input type="text" v-model="qoutee">
            </div>

            <div>
                <label for="">name</label>
                <input type="text" v-model="description">
            </div>

            <div>
                <button>Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default{
        name: 'AddQuote'
    }
</script>