<template>
  <v-app>
    <nav>
      <Navbar />
    </nav>

    <v-main>

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
