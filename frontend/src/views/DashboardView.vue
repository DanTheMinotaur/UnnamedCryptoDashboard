<script setup>
import BarWeekly from '../components/charts/BarWeekly.vue'
import LineM from '../components/charts/LineMonthy.vue'
import LineY from '../components/charts/LineYearly.vue'
import HoldingsTable from '../components/holdings/HoldingsTable.vue'
</script>

<template>
	<div class="container-fluid py-4">
		<div class="row">
			<div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
				<div class="card">
					<div class="card-header p-3 pt-2">
						<div
							class="icon icon-lg icon-shape bg-gradient-dark shadow-dark text-center border-radius-xl mt-n4 position-absolute">
							<i class="material-icons opacity-10">weekend</i>
						</div>
						<div class="text-end pt-1">
							<p class="text-sm mb-0 text-capitalize">Today's Money</p>
							<h4 class="mb-0">€17,830</h4>
						</div>
					</div>
					<hr class="dark horizontal my-0">
					<div class="card-footer p-3">
						<p class="mb-0"><span class="text-success text-sm font-weight-bolder">+55% </span>than last week</p>
					</div>
				</div>
			</div>
			<div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
				<div class="card">
					<div class="card-header p-3 pt-2">
						<div
							class="icon icon-lg icon-shape bg-gradient-primary shadow-primary text-center border-radius-xl mt-n4 position-absolute">
							<i class="material-icons opacity-10">show_chart</i>
						</div>
						<div class="text-end pt-1">
							<p class="text-sm mb-0 text-capitalize">Today's Change</p>
							<h4 class="mb-0">€2,300</h4>
						</div>
					</div>
					<hr class="dark horizontal my-0">
					<div class="card-footer p-3">
						<p class="mb-0"><span class="text-success text-sm font-weight-bolder">+3% </span>than yesterday</p>
					</div>
				</div>
			</div>
			<div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
				<div class="card">
					<div class="card-header p-3 pt-2">
						<div
							class="icon icon-lg icon-shape bg-gradient-success shadow-success text-center border-radius-xl mt-n4 position-absolute">
							<i class="material-icons opacity-10">show_chart</i>
						</div>
						<div class="text-end pt-1">
							<p class="text-sm mb-0 text-capitalize">Monthly Change</p>
							<h4 class="mb-0">€3,462</h4>
						</div>
					</div>
					<hr class="dark horizontal my-0">
					<div class="card-footer p-3">
						<p class="mb-0"><span class="text-danger text-sm font-weight-bolder">-2%</span> than last month</p>
					</div>
				</div>
			</div>
			<div class="col-xl-3 col-sm-6">
				<div class="card">
					<div class="card-header p-3 pt-2">
						<div
							class="icon icon-lg icon-shape bg-gradient-info shadow-info text-center border-radius-xl mt-n4 position-absolute">
							<i class="material-icons opacity-10">weekend</i>
						</div>
						<div class="text-end pt-1">
							<p class="text-sm mb-0 text-capitalize">Year Change</p>
							<h4 class="mb-0">€22,430</h4>
						</div>
					</div>
					<hr class="dark horizontal my-0">
					<div class="card-footer p-3">
						<p class="mb-0"><span class="text-success text-sm font-weight-bolder">+5% </span>than last year</p>
					</div>
				</div>
			</div>
		</div>
		<div class="row mt-4">
			<div class="col-lg-4 col-md-6 mt-4 mb-4">
				<div class="card z-index-2 ">
					<div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
						<div class="bg-gradient-primary shadow-primary border-radius-lg py-3 pe-1">
							<div class="chart">
								<!-- <canvas id="chart-bars" class="chart-canvas" height="170"></canvas> -->
								<BarWeekly id="chart-bars" class="chart-canvas" height="170" />
							</div>
						</div>
					</div>
					<div class="card-body">
						<h6 class="mb-0 ">Weekly Performance</h6>
						<!-- <p class="text-sm ">Last Campaign Performance</p> -->
						<hr class="dark horizontal">
						<div class="d-flex ">
							<i class="material-icons text-sm my-auto me-1">schedule</i>
							<p class="mb-0 text-sm"> Updated 7 Hours ago </p>
						</div>
					</div>
				</div>
			</div>
			<div class="col-lg-4 col-md-6 mt-4 mb-4">
				<div class="card z-index-2  ">
					<div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
						<div class="bg-gradient-success shadow-success border-radius-lg py-3 pe-1">
							<div class="chart">
								<LineM id="chart-line-tasks" class="chart-canvas" height="170" />
							</div>
						</div>
					</div>
					<div class="card-body">
						<h6 class="mb-0 "> Monthly Performance </h6>
						<!-- <p class="text-sm "> (<span class="font-weight-bolder">+15%</span>) increase in today sales. </p> -->
						<hr class="dark horizontal">
						<div class="d-flex ">
							<i class="material-icons text-sm my-auto me-1">schedule</i>
							<p class="mb-0 text-sm"> updated 4 min ago </p>
						</div>
					</div>
				</div>
			</div>
			<div class="col-lg-4 mt-4 mb-3">
				<div class="card z-index-2 ">
					<div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
						<div class="bg-gradient-dark shadow-dark border-radius-lg py-3 pe-1">
							<div class="chart">
								<!-- <canvas id="chart-line-tasks" class="chart-canvas" height="170"></canvas> -->
								<LineY id="chart-line-tasks" class="chart-canvas" height="170" />
							</div>
						</div>
					</div>
					<div class="card-body">
						<h6 class="mb-0 ">Yearly Performance</h6>
						<!-- <p class="text-sm ">Last Campaign Performance</p> -->
						<hr class="dark horizontal">
						<div class="d-flex ">
							<i class="material-icons text-sm my-auto me-1">schedule</i>
							<p class="mb-0 text-sm">just updated</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="row mb-4">
			<div class="col-lg-8 col-md-6 mb-md-0 mb-4">
				<div class="card">
					<div class="card-header pb-0">
						<div class="row">
							<div class="col-lg-6 col-7">
								<h6>Top Holdings</h6>
								<p class="text-sm mb-0">
									<i class="fa fa-check text-info" aria-hidden="true"></i>
									<span class="font-weight-bold ms-1">1 added</span> this month
								</p>
							</div>
						</div>
					</div>
					<HoldingsTable/>
				</div>
			</div>
			<div class="col-lg-4 col-md-6">
				<div class="card h-100">
					<div class="card-header pb-0">
						<h6>Activities</h6>
						<p class="text-sm">
							<!-- <i class="fa fa-arrow-up text-success" aria-hidden="true"></i> -->
							<!-- <span class="font-weight-bold">24%</span> this month -->
						</p>
					</div>
					<div class="card-body p-3">
						<div class="timeline timeline-one-side">
							<div class="timeline-block mb-3">
								<span class="timeline-step">
									<i class="material-icons text-success text-gradient">notifications</i>
								</span>
								<div class="timeline-content">
									<h6 class="text-dark text-sm font-weight-bold mb-0">Added 0.02 BTC</h6>
									<p class="text-secondary font-weight-bold text-xs mt-1 mb-0">22 DEC 7:20 PM</p>
								</div>
							</div>
							<div class="timeline-block mb-3">
								<span class="timeline-step">
									<i class="material-icons text-danger text-gradient">code</i>
								</span>
								<div class="timeline-content">
									<h6 class="text-dark text-sm font-weight-bold mb-0">Added 0.44 ETH</h6>
									<p class="text-secondary font-weight-bold text-xs mt-1 mb-0">21 DEC 11 PM</p>
								</div>
							</div>
							<div class="timeline-block mb-3">
								<span class="timeline-step">
									<i class="material-icons text-info text-gradient">shopping_cart</i>
								</span>
								<div class="timeline-content">
									<h6 class="text-dark text-sm font-weight-bold mb-0">Removed 0.02 BTC</h6>
									<p class="text-secondary font-weight-bold text-xs mt-1 mb-0">21 DEC 9:34 PM</p>
								</div>
							</div>
							<div class="timeline-block mb-3">
								<span class="timeline-step">
									<i class="material-icons text-warning text-gradient">credit_card</i>
								</span>
								<div class="timeline-content">
									<h6 class="text-dark text-sm font-weight-bold mb-0">Added 12 ADA</h6>
									<p class="text-secondary font-weight-bold text-xs mt-1 mb-0">20 DEC 2:20 AM</p>
								</div>
							</div>
							<div class="timeline-block mb-3">
								<span class="timeline-step">
									<i class="material-icons text-primary text-gradient">key</i>
								</span>
								<div class="timeline-content">
									<h6 class="text-dark text-sm font-weight-bold mb-0">Removed 1.2 XMR</h6>
									<p class="text-secondary font-weight-bold text-xs mt-1 mb-0">18 DEC 4:54 AM</p>
								</div>
							</div>
							<div class="timeline-block">
								<span class="timeline-step">
									<i class="material-icons text-dark text-gradient">payments</i>
								</span>
								<div class="timeline-content">
									<h6 class="text-dark text-sm font-weight-bold mb-0">Added 1.5 XMR</h6>
									<p class="text-secondary font-weight-bold text-xs mt-1 mb-0">17 DEC</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>