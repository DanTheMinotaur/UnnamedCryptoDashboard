<script setup lang="ts">
defineProps({
    name: String,
    icon: String,
    code: String,
    units: Number,
    value: Number,
    change: Number,
    currency: String
})
</script>

<template>
    <tr>
        <td>
            <div class="d-flex px-2 py-1">
                <div>
                    <img :src="`/img/icons/${icon}`" class="avatar avatar-sm me-3" alt="xd">
                </div>
                <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm">{{ name }}({{ code }})</h6>
                </div>
            </div>
        </td>
        <td class="align-middle  text-sm">
            <span class="text-xs font-weight-bold"> {{ units }} </span>
        </td>
        <td class="align-middle text-center text-sm">
            <span class="text-xs font-weight-bold"> {{ currency }} {{ value }} </span>
        </td>
        <td class="align-middle text-center">
            <span class="text-danger text-sm font-weight-bolder">{{ change }}%</span>
        </td>
    </tr>

</template>