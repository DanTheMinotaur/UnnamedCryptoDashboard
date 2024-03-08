<script setup lang="ts">
import HoldingsTable from '../components/holdings/HoldingsTable.vue'
</script>

<template>
  <div class="container-fluid py-4">
    <div class="row">
      <div class="col-12">
        <div class="card my-4">
          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <div class="bg-gradient-primary shadow-primary border-radius-lg pt-4 pb-3">
              <div class="row">
                <div class="col-6 d-flex align-items-center">
                  <h6 class="text-white text-capitalize ps-3">Holdings</h6>
                </div>
                <div class="col-6 text-end">
                  <a class="btn btn-success" href="javascript:;"><i class="material-icons text-sm">add</i>&nbsp;&nbsp;Add New Crypto</a>
                </div>
              </div>
            </div>
          </div>
          <HoldingsTable/>
        </div>
      </div>
    </div>
  </div>
</template>