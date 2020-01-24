<template>
  <v-app>
    <TopNav/>
    <Grid :grid-data="data"/>
  </v-app>
</template>

<script>
import TopNav from './components/TopNav';
import Grid from './components/Grid';

export default {
  name: 'App',

  components: {
    TopNav,
    Grid,
  },

  data: () => ({
    data: {
      "city": "halifax",
      "gridDimensions": {
        "length": 3,
        "width": 3
      },
      "grid": [
        [
          {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
   {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
          {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
          {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
   {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
          {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
          {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
   {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ],
        [
          {
            "id": 1,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 2,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 3,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 4,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 5,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 6,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 7,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 8,
            "originalValue": 7,
            "upatedValue": 6,
            "deviceAtLocation": ""
          },
          {
            "id": 9,
            "originalValue": 5,
            "upatedValue": 5,
            "deviceAtLocation": {
              "deviceName": "CCS1",
              "radii": 4
            },
          },
          {
            "id": 10,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 11,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 12,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 13,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
          {
            "id": 14,
            "originalValue": 7,
            "upatedValue": 5,
            "deviceAtLocation": ""
          },
        ]
      ],
      "result": {
        "budget": 1.75,
        "moneySpent": 0.45,
        "targetReduction": 21,
        "actualReduction": 24
      }
    }
  }),
};
</script>
