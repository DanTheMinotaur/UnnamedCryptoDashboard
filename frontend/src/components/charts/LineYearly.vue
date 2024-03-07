<script setup>
import Chart from 'chart.js/auto'
import { Line } from 'vue-chartjs'
import { fontConfig } from './_common'

const data = {
    labels: ["2019", "2020", "2021", "2022", "2023", "2024"],
    datasets: [{
        label: "Year",
        tension: 0,
        borderWidth: 0,
        pointRadius: 5,
        pointBackgroundColor: "rgba(255, 255, 255, .8)",
        pointBorderColor: "transparent",
        borderColor: "rgba(255, 255, 255, .8)",
        borderWidth: 4,
        backgroundColor: "transparent",
        fill: true,
        data: [7020, 8203, 8400, 11020, 13408, 17830],
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
        }
    }
}
</script>

<template>
    <Line :options="options" :data="data" />
</template>