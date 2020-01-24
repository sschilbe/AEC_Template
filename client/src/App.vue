<template>
  <v-app>
    <TopNav/>
  </v-app>
</template>

<script>
import TopNav from './components/TopNav';

export default {
  name: 'App',

  components: {
    TopNav,
  },

  data: () => ({
    //
  }),
};
</script>
