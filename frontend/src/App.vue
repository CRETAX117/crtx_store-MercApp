<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { useCart } from './composables/useCart'

const { totalItems } = useCart()
</script>

<template>
  <div id="app">
    <nav class="navbar">
      <router-link to="/" class="nav-brand">CRTX Store</router-link>
      <div class="nav-links">
        <router-link to="/" class="nav-link">Catalogo</router-link>
        <router-link to="/product/new" class="nav-link">Nuevo</router-link>
        <router-link to="/cart" class="nav-link nav-cart">
          Carrito
          <span v-if="totalItems > 0" class="cart-badge">{{ totalItems }}</span>
        </router-link>
        <router-link to="/about" class="nav-link">Acerca de</router-link>
      </div>
    </nav>

    <main class="main-content">
      <Suspense>
        <RouterView />
        <template #fallback>
          <div class="state-message">Cargando vista...</div>
        </template>
      </Suspense>
    </main>
  </div>
</template>
