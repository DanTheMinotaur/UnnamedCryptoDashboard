import DashboardView from '../views/DashboardView.vue'
import HoldingsView from '../views/HoldingsView.vue'

const routes = [
    {
      path: '/',
      name: 'Dashboard',
      component: DashboardView,
      meta: {
        icon: 'dashboard'
      }
    },
    {
      path: '/holdings',
      name: 'Holdings',
      component: HoldingsView,
      meta: {
        icon: 'wallet'
      }
    }
]

export default routes