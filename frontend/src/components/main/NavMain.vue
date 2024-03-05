<script setup lang="ts">
import routes from '../../router/routes'
</script>

<template>
  <aside class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start ms-3   bg-gradient-dark" id="sidenav-main">
    <hr class="horizontal light mt-0 mb-2">
    <div class="collapse navbar-collapse  w-auto " id="sidenav-collapse-main">
      <ul class="navbar-nav">
        <RouterLink v-for="route in routes" :key="route.path" :to="route.path">
            <li class="nav-item">
                <RouterLink class="nav-link text-white" :to="route.path">
                    <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                    <i class="material-icons opacity-10">{{ route.meta.icon }}</i>
                    </div>
                    <span class="nav-link-text ms-1">{{ route.name }}</span>
                </RouterLink>
            </li>
        </RouterLink>
      </ul>
    </div>

  </aside>
</template>