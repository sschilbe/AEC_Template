<template>
  <v-form class="form">
    <v-container>
      <!-- <v-row>
        <v-col cols="8" sm="4">
          <input color="purple" :v-model="budget" label="Budget" outlined/>
        </v-col>

        <v-col cols="8" sm="4">
          <input
            color="purple"
            :v-model="capture"
            label="Target Carbon Capture Percentage"
            outlined
          />
        </v-col>
        <v-col cols="8" sm="4">
          <v-btn class="mr-4" @click="submitForm()">submit</v-btn>
        </v-col>
      </v-row> -->

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

input {
	outline: none;
    padding: 10px;
	border: 2px solid #9c27b0;
    border-radius: 15px;
}

textarea {
  outline: none;
  border: none;
}

textarea:focus, input:focus {
  border-color: #d6d6d6;
}

input:focus::-webkit-input-placeholder { color:transparent; }
input:focus:-moz-placeholder { color:transparent; }
input:focus::-moz-placeholder { color:transparent; }
input:focus:-ms-input-placeholder { color:transparent; }

textarea:focus::-webkit-input-placeholder { color:transparent; }
textarea:focus:-moz-placeholder { color:transparent; }
textarea:focus::-moz-placeholder { color:transparent; }
textarea:focus:-ms-input-placeholder { color:transparent; }

input::-webkit-input-placeholder { color: #acacac; }
input:-moz-placeholder { color: #acacac; }
input::-moz-placeholder { color: #acacac; }
input:-ms-input-placeholder { color: #acacac; }

textarea::-webkit-input-placeholder { color: #acacac; }
textarea:-moz-placeholder { color: #acacac; }
textarea::-moz-placeholder { color: #acacac; }
textarea:-ms-input-placeholder { color: #acacac; }

/*---------------------------------------------*/
button {
	outline: none !important;
	border: none;
	background: transparent;
}

button:hover {
	cursor: pointer;
}

</style>
