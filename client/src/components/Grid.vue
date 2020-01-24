<template>
  <v-row align="center" justify="center">
      <table class="grid-table">
        <tr v-bind:key="index" v-for="(row, index) in gridData.grid">
          <td
            class="grid-cell"
            v-bind:class="{ hasCcs: hasCCS(cell)}"
            v-bind:style="{ backgroundColor: 'rgb(156, 39, 176, '+ ccsDiff(cell) +')', color: ccsDiff(cell) ? 'white' : 'black'}"
            v-bind:key="cell.id"
            v-for="cell in row"
            v-tooltip="tooltipFor(cell)"
          >
            {{ cell.updatedValue }}
          </td>
        </tr>
      </table>
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
    },
    ccsDiff(cell) {
      return cell.originalValue/cell.updatedValue - 1;
         
    }
  }
};
</script>

<style scoped>
.hasCcs {
  background-color: #F44336 !important;
  color: white;
}

.grid-cell {
  height: 10rem;
  width: 10rem;
  text-align: center;
  font-size: 2rem;
}

.grid-table {
  margin-top: 110px;
  border-collapse: collapse;
}

td {
  border:2px solid black;
}
td:hover {
  background-color: white;
  color: black;
}
</style>
