<script setup>
import Chart from 'chart.js/auto'
import { Bar } from 'vue-chartjs'

const chartData = {
  labels: ["Mon", "T", "W", "T", "F", "S", "S"],
  datasets: [{
    label: "Total € Value",
    tension: 0.4,
    borderWidth: 0,
    borderRadius: 4,
    borderSkipped: false,
    backgroundColor: "rgba(255, 255, 255, .8)",
    data: [13302, 13512, 13910, 14544, 14203, 13900, 14505],
    maxBarThickness: 6
  },]
}

const chartOptions = {
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
        suggestedMin: 0,
        suggestedMax: 500,
        beginAtZero: true,
        padding: 10,
        font: {
          size: 14,
          weight: 300,
          family: '"Roboto", Helvetica, Arial, sans-serif',
          style: 'normal',
          lineHeight: 2
        },
        color: "#fff"
      },
    },
    x: {
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
        font: {
          size: 14,
          weight: 300,
          family: '"Roboto", Helvetica, Arial, sans-serif',
          style: 'normal',
          lineHeight: 2
        }
      }
    }
  }
}

</script>

<template>
    <Bar
      id="chart-bars"
      :options="chartOptions"
      :data="chartData"
    />
</template>