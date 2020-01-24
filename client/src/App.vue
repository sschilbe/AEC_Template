<template>
  <v-app>
    <TopNav v-on:map-change="mapChange"/>
    <v-content>
      <v-container fluid>
          <Grid :grid-data="gridData" class="large-background"
          :style="{ backgroundImage: 'url(' + require('./assets/map-' + provinceCode + '.png') + ')' }"/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import TopNav from "./components/TopNav";
import Grid from "./components/Grid";

export default {

  name: 'App',
  components: {
    TopNav,
    Grid
  },
  methods: {
    mapChange(code) {
      this.provinceCode = code;
    },
  },
  data: () => ({
    provinceCode: 'NB',
    gridData: {
      "city": "halifax",
      "gridDimensions": {
        "length": 3,
        "width": 3
      },
      grid: [
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ],
        [
          {
            id: 1,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 2,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 3,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 4,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 5,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 6,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 7,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 8,
            originalValue: 7,
            updatedValue: 6,
            deviceAtLocation: ""
          },
          {
            id: 9,
            originalValue: 5,
            updatedValue: 5,
            deviceAtLocation: {
              deviceName: "CCS1",
              radii: 4
            }
          },
          {
            id: 10,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 11,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 12,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 13,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          },
          {
            id: 14,
            originalValue: 7,
            updatedValue: 5,
            deviceAtLocation: ""
          }
        ]
      ],
      result: {
        budget: 1.75,
        moneySpent: 0.45,
        targetReduction: 21,
        actualReduction: 24
      }
    }
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
