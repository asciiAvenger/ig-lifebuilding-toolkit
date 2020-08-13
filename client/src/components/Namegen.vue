<template>
  <v-container>
    <v-card>
      <v-card-title>
        IG name generator
      </v-card-title>
      <v-card-subtitle>
        because your name is your brand!
      </v-card-subtitle>
      <v-card-text>
        <div class="d-flex align-center">
          <v-text-field v-model="inputName" class="mr-4" label="Your name" prepend-icon="mdi-form-textbox" />
          <v-btn @click="generateName">generate name</v-btn>
        </div>
        <div class="d-flex align-center">
          <v-text-field v-model="userName" class="mr-4" label="IG name" prepend-icon="mdi-account" disabled />
          <v-btn @click="copyName" icon><v-icon>mdi-content-copy</v-icon></v-btn>
        </div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'Namegen',
  data() {
    return {
      inputName: '',
      userName: ''
    }
  },
  methods: {
    generateName() {
      this.userName = this.inputName;
    },
    copyName() {
      navigator.clipboard.writeText(this.userName);
    }
  }
}
</script>

<style scoped>

</style>