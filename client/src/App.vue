<template>
  <v-app>
    <nav>
      <Navbar />
    </nav>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  },
  data() {
    return {

    }
  }
};
</script>
