<template>
  <v-app-bar absolute color="purple" dark>
    <v-spacer></v-spacer>
    <v-toolbar-title>AEC 2020: Programming Competition</v-toolbar-title>
    <v-spacer></v-spacer>
    <template v-slot:extension>
      <v-tabs align-with-title grow="grow" background-color="transparent">
        <v-tab @click="$emit('map-change', 'NB')">Saint John, NB</v-tab>
        <v-tab @click="$emit('map-change', 'NS')">Halifax, NS</v-tab>
        <v-tab @click="$emit('map-change', 'NL')">St. John's, NL</v-tab>
      </v-tabs>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  name: "TopNav",
};
</script>

<style scoped></style>
