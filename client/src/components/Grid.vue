<template>
  <v-row align="center" justify="center">
    <v-col class="text-center">
      <table class="grid-table">
        <tr v-bind:key="index" v-for="(row, index) in gridData.grid">
          <td
            class="grid-cell"
            v-bind:class="{ hasCcs: hasCCS(cell) }"
            v-bind:key="cell.id"
            v-for="cell in row"
            v-tooltip="tooltipFor(cell)"
          >
            {{ cell.updatedValue }}
          </td>
        </tr>
      </table>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "Grid",
  props: {
    gridData: {
      type: Object,
      required: true
    }
  },
  methods: {
    hasCCS(cell) {
      return cell.deviceAtLocation !== "";
    },
    tooltipFor(cell) {
      let tooltip = "Original value: " + cell.originalValue;
      if (cell.deviceAtLocation !== "") {
        tooltip += "<br>CCS Device Used: " + cell.deviceAtLocation.deviceName;
      }
      return tooltip;
    }
  }
};
</script>

<style scoped>
.hasCcs {
  background-color: #9c27b0;
  color: white;
}

.grid-cell {
  height: 6rem;
  width: 6rem;
  text-align: center;
  font-size: 2rem;
}

.grid-table {
  margin-top: 110px;
  border-collapse: collapse;
}

td {
  border: 1px solid black;
}
td:hover {
  background-color: #adadad;
}
</style>
