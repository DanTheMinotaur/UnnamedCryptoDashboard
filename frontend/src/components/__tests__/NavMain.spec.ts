import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import NavMain from '../main/NavMain.vue' // Assuming your component file is named Sidebar.vue

describe('Sidebar', () => {
  it('renders correctly with routes', async () => {
    // Mock routes data
    const routes = [
      { path: '/dashboard', name: 'Dashboard', meta: { icon: 'home' } },
      { path: '/holding', name: 'Holdings', meta: { icon: 'info' } },
      // Add more mock routes if needed
    ]

    // Mount the component with mocked routes
    const wrapper = mount(NavMain, {
      props: { routes }
    })

    // Wait for Vue to finish rendering
    await wrapper.vm.$nextTick()

    // Assert that the component renders correctly
    expect(wrapper.html()).toMatchSnapshot()
  })

  // Add more tests as needed
})