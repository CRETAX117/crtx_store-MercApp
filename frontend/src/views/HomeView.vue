<script setup lang="ts">
import { onMounted, watch } from 'vue'
import { useProducts } from '../composables/useProducts'
import { useCart } from '../composables/useCart'
import ProductCard from '../components/ProductCard.vue'
import type { Product } from '../types/Product'

const {
  products,
  categories,
  loading,
  error,
  search,
  selectedCategory,
  loadProducts,
  loadCategories,
  categoryName
} = useProducts()

const { addItem } = useCart()

onMounted(async () => {
  await loadCategories()
  await loadProducts()
})

watch([search, selectedCategory], () => {
  loadProducts()
})

function onAddedToCart(product: Product) {
  addItem(product)
}
</script>

<template>
  <div class="home-view">
    <header class="home-header">
      <h1>CRTX Store</h1>
      <p>Encuentra lo que necesitas</p>
    </header>

    <section class="filters">
      <input
        v-model="search"
        type="text"
        class="input-search"
        placeholder="Buscar productos..."
      />
      <select v-model="selectedCategory" class="select-category">
        <option value="">Todas las categorias</option>
        <option
          v-for="cat in categories"
          :key="cat._id"
          :value="cat._id"
        >
          {{ cat.name }}
        </option>
      </select>
    </section>

    <div v-if="loading" class="state-message">Cargando productos...</div>
    <div v-else-if="error" class="state-message error">{{ error }}</div>
    <div v-else-if="products.length === 0" class="state-message">
      No hay productos que coincidan con la busqueda.
    </div>

    <section v-else class="product-grid">
      <ProductCard
        v-for="product in products"
        :key="product._id"
        :product="product"
        :categoryName="categoryName(product.categoryId)"
        @added-to-cart="onAddedToCart"
      />
    </section>
  </div>
</template>
