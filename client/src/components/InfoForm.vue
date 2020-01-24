<template>
  <v-form class="form">
    <v-container>
      <v-row>
        <v-col cols="8" sm="4">
          <v-text-field color="purple" :v-model="budget" label="Budget" outlined></v-text-field>
        </v-col>

        <v-col cols="8" sm="4">
          <v-text-field
            color="purple"
            :v-model="capture"
            label="Target Carbon Capture Percentage"
            outlined
          ></v-text-field>
        </v-col>
        <v-col cols="8" sm="4">
          <v-btn class="mr-4" @click="submitForm()">submit</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6">
          <p>Total Spent: {{ results.totalSpent }}</p>
        </v-col>
        <v-col cols="" sm="6">
          <p>Actual Carbon Capture: {{ results.actualCarbonCapture }}</p>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
export default {
  name: "InfoForm",
  data: () => ({
    budget: "1750000",
    capture: "21"
  }),
  props: {
    results: {
      type: Object,
      required: false
    }
  },
  methods: {
    submitForm(form) {
        console.log(form) // eslint-disable-line no-console

    }
  }
};
</script>

<style scoped>
.form {
  margin-top: 110px;
}
</style>
