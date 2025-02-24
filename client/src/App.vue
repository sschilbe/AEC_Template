<template>
  <v-app>
    <TopNav v-on:map-change="mapChange" />
    <v-content>
      <v-container fluid>
        <InfoForm :results="gridData.results"/>
        <Grid
          :grid-data="gridData"
          class="large-background"
          :style="{
            backgroundImage: 'url(' + require('./assets/map-' + provinceCode + '.png') + ')'
          }"
        />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import TopNav from "./components/TopNav";
import Grid from "./components/Grid";
import axios from "axios";
import InfoForm from "./components/InfoForm";

export default {
  name: "App",
  components: {
    TopNav,
    Grid,
    InfoForm
  },
  methods: {
    mapChange(code) {
      this.provinceCode = code;

      let cityName;
      switch (code) {
        case "NB":
          cityName = "Saint John";
          break;
        case "NS":
          cityName = "Halifax";
          break;
        case "NL":
          cityName = "Saint John's";
          break;
      }

      axios
        .get("http://localhost:5000/cityGrid/" + cityName)
        .then(response => (this.gridData = response.data));
    }
  },
  created() {
    this.mapChange(this.provinceCode);
  },
  data: () => ({
    provinceCode: "NB",
    gridData: {}
  })
};
</script>

<style>
.large-background {
  background-size: cover;
}

/* Tooltip styling from v-tooltip */
.tooltip {
  display: block !important;
  z-index: 10000;
}

.tooltip .tooltip-inner {
  background: black;
  color: white;
  border-radius: 16px;
  padding: 5px 10px 4px;
  font-family: "Roboto", sans-serif;
}

.tooltip .tooltip-arrow {
  width: 0;
  height: 0;
  border-style: solid;
  position: absolute;
  margin: 5px;
  border-color: black;
  z-index: 1;
}

.tooltip[x-placement^="top"] {
  margin-bottom: 5px;
}

.tooltip[x-placement^="top"] .tooltip-arrow {
  border-width: 5px 5px 0 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  bottom: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="bottom"] {
  margin-top: 5px;
}

.tooltip[x-placement^="bottom"] .tooltip-arrow {
  border-width: 0 5px 5px 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-top-color: transparent !important;
  top: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="right"] {
  margin-left: 5px;
}

.tooltip[x-placement^="right"] .tooltip-arrow {
  border-width: 5px 5px 5px 0;
  border-left-color: transparent !important;
  border-top-color: transparent !important;
  border-bottom-color: transparent !important;
  left: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip[x-placement^="left"] {
  margin-right: 5px;
}

.tooltip[x-placement^="left"] .tooltip-arrow {
  border-width: 5px 0 5px 5px;
  border-top-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  right: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip.popover .popover-inner {
  background: #f9f9f9;
  color: black;
  padding: 24px;
  border-radius: 5px;
  box-shadow: 0 5px 30px black;
}

.tooltip.popover .popover-arrow {
  border-color: #f9f9f9;
}

.tooltip[aria-hidden="true"] {
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.15s, visibility 0.15s;
}

.tooltip[aria-hidden="false"] {
  visibility: visible;
  opacity: 1;
  transition: opacity 0.15s;
}
</style>
