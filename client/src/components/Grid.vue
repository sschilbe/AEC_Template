<template>
  <v-container>
    <v-row  align="center" justify="center">
      <table class="grid-table">
        <tr v-bind:key="index" v-for="(row, index) in gridData.grid">
          <td class="grid-cell"
              v-bind:class="{ hasCcs: hasCCS(cell) }"
              v-bind:key="cell.id" v-for="cell in row"
              v-tooltip="tooltipFor(cell)"
          >
            {{ cell.upatedValue }}
          </td>
        </tr>
      </table>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: "Grid",
    props: { gridData: {
      type: Object,
      required: true
    }},
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
  }
</script>

<style>
  .hasCcs {
    background-color: fuchsia;
  }

  .grid-cell {
    height: 100px;
    width: 100px;
    text-align: center;
  }

  .grid-table {
    table-layout: fixed;
    border-collapse: collapse;
  }

  td {
    border: 1px solid black;
  }
</style>

