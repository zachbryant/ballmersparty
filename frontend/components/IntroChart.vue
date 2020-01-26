<template>
  <div class="chart-container" style="position: relative; height:75vh; width:100%">
    <canvas id="chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import homeChartData from '../assets/home-chart-data.js'
const canvas = document.getElementById('chart')
export default {
  name: 'IntroChart',
  data() {
    return {
      homeChartData
    }
  },
  methods: {
    createChart(chartId, chartData) {
      const canvas = document.getElementById(chartId)
      const myChart = new Chart(canvas, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      })
      myChart.resize()
    }
  },
  mounted() {
    this.createChart('chart', this.homeChartData)
  }
}
</script>

<style scoped></style>
