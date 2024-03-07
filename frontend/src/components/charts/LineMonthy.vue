<script setup>
import Chart from 'chart.js/auto'
import { Line } from 'vue-chartjs'
import { fontConfig } from './_common'

const data = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
  datasets: [{
    label: "End Of Month",
    tension: 0,
    borderWidth: 0,
    pointRadius: 5,
    pointBackgroundColor: "rgba(255, 255, 255, .8)",
    pointBorderColor: "transparent",
    borderColor: "rgba(255, 255, 255, .8)",
    borderColor: "rgba(255, 255, 255, .8)",
    borderWidth: 4,
    backgroundColor: "transparent",
    fill: true,
    data: [12345, 13800, 13523, 14233, 14550, 15020, 16533, 15866, 16200, 17022, 16888, 17830],
    maxBarThickness: 6
  }],
}

const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: false,
              borderDash: [5, 5],
              color: 'rgba(255, 255, 255, .2)'
            },
            ticks: {
              display: true,
              color: '#f8f9fa',
              padding: 10,
              font: fontConfig,
            }
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
              borderDash: [5, 5]
            },
            ticks: {
              display: true,
              color: '#f8f9fa',
              padding: 10,
              font: fontConfig,
            }
          },
        },
      }
</script>

<template>
  <Line :options="options" :data="data" />
</template>