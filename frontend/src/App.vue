<template>
  <main>
    <nav class="flex justify-center items-center text-2xl border-b py-5 mb-5 space-x-4 shadow-xl" >
      <router-link to="/" class="text-green-500">Quotes</router-link>
      <span class="bg-gray-600 h-8 w-0.5"></span>
      <router-link to="/Add" class="text-gray-600">Add</router-link> 
    </nav>
    <router-view/>
  </main>
</template>
