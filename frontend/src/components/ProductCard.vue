<script setup lang="ts">
import type { Product } from '../types/Product'

const props = defineProps<{
  product: Product
  categoryName: string
}>()

const emit = defineEmits<{
  'added-to-cart': [product: Product]
}>()

function handleAddToCart() {
  emit('added-to-cart', props.product)
}

function formatPrice(price: number) {
  return price.toFixed(2)
}
</script>

<template>
  <div class="product-card">
    <div class="card-image">
      <img
        v-if="product.imageUrl"
        :src="product.imageUrl"
        :alt="product.name"
      />
      <div v-else class="image-placeholder">
        <span>Sin imagen</span>
      </div>
      <span class="badge-category">{{ categoryName }}</span>
    </div>

    <div class="card-body">
      <h3 class="card-title">{{ product.name }}</h3>
      <p class="card-description">{{ product.description }}</p>

      <div class="card-footer">
        <span class="card-price">${{ formatPrice(product.price) }}</span>
        <span class="card-stock" :class="{ 'out': product.stock === 0 }">
          {{ product.stock > 0 ? `${product.stock} en stock` : 'Sin stock' }}
        </span>
      </div>

      <div class="card-actions">
        <router-link :to="`/product/${product._id}`" class="btn btn-outline">
          Ver detalle
        </router-link>
        <button
          class="btn btn-primary"
          :disabled="product.stock === 0"
          @click="handleAddToCart"
        >
          Agregar
        </button>
      </div>
    </div>
  </div>
</template>
