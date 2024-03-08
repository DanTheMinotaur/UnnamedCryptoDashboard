<script setup lang="ts">
import HoldingsTableRow from './HoldingsTableRow.vue'
import { mockHoldings } from '../../__mockdata__/holdings' 

const holdings = mockHoldings
const currency = 'EUR'

</script>

<template>
	<div class="card-body px-0 pb-2">
		<div class="table-responsive p-0">
			<table class="table align-items-center mb-0">
				<thead>
					<tr>
						<th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Asset</th>
						<th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Units</th>
						<th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">EUR Value</th>
						<th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">24h change</th>
					</tr>
				</thead>
				<tbody>
					<HoldingsTableRow v-for="h in holdings" :key="h.code" :name="h.name" :code="h.code" :icon="h.icon"
						:units="h.units" :change="h.change" :value="h.value" :currency="currency"></HoldingsTableRow>
				</tbody>
			</table>
		</div>
	</div>
</template>