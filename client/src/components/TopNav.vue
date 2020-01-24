<template>
  <v-card class="overflow-hidden">
    <v-app-bar absolute color="purple" dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>AEC 2020: Programming Competition</v-toolbar-title>

      <template v-slot:extension>
        <v-tabs align-with-title background-color="transparent">
          <v-tab>Saint John, NB</v-tab>
          <v-tab>Halifax, NS</v-tab>
          <v-tab>St. John's, NF</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-sheet>
      <v-container style="height: 1000px;"></v-container>
    </v-sheet>
  </v-card>
</template>

<script>
export default {
  name: "TopNav",

  data() {
    return {};
  }
};
</script>
