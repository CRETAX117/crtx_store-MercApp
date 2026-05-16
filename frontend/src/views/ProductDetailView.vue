<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProductById, deleteProduct } from '../services/products.service'
import { getCategories } from '../services/categories.service'
import { useCart } from '../composables/useCart'
import type { Product, Category } from '../types/Product'

const route = useRoute()
const router = useRouter()
const { addItem } = useCart()

const product = ref<Product | null>(null)
const categories = ref<Category[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const deleting = ref(false)
const added = ref(false)

onMounted(async () => {
  try {
    const [prod, cats] = await Promise.all([
      getProductById(route.params.id as string),
      getCategories()
    ])
    product.value = prod
    categories.value = cats
  } catch {
    error.value = 'No se encontro el producto'
  } finally {
    loading.value = false
  }
})

function getCategoryName(id: string) {
  const cat = categories.value.find(c => c._id === id)
  return cat ? cat.name : 'Sin categoria'
}

function formatPrice(price: number) {
  return price.toFixed(2)
}

function handleAddToCart() {
  if (!product.value) return
  addItem(product.value)
  added.value = true
  setTimeout(() => { added.value = false }, 1500)
}

async function handleDelete() {
  if (!product.value) return
  if (!confirm('¿Eliminar este producto?')) return
  deleting.value = true
  try {
    await deleteProduct(product.value._id)
    router.push('/')
  } catch {
    alert('No se pudo eliminar el producto')
    deleting.value = false
  }
}

function goBack() {
  router.push('/')
}
</script>

<template>
  <div class="detail-view">
    <button class="btn btn-outline back-btn" @click="goBack">Volver al catalogo</button>

    <div v-if="loading" class="state-message">Cargando...</div>
    <div v-else-if="error" class="state-message error">{{ error }}</div>

    <div v-else-if="product" class="detail-card">
      <div class="detail-image">
        <img v-if="product.imageUrl" :src="product.imageUrl" :alt="product.name" />
        <div v-else class="image-placeholder large">
          <span>Sin imagen</span>
        </div>
      </div>

      <div class="detail-info">
        <span class="badge-category">{{ getCategoryName(product.categoryId) }}</span>
        <h1>{{ product.name }}</h1>
        <p class="detail-description">{{ product.description }}</p>
        <p class="detail-price">${{ formatPrice(product.price) }}</p>
        <p class="detail-stock" :class="{ 'out': product.stock === 0 }">
          {{ product.stock > 0 ? `${product.stock} unidades disponibles` : 'Sin stock' }}
        </p>

        <div class="detail-actions">
          <button
            class="btn btn-primary"
            :disabled="product.stock === 0"
            @click="handleAddToCart"
          >
            {{ added ? 'Agregado!' : 'Agregar al carrito' }}
          </button>
          <router-link :to="`/product/${product._id}/edit`" class="btn btn-outline">
            Editar
          </router-link>
        </div>

        <button
          class="btn btn-danger"
          :disabled="deleting"
          @click="handleDelete"
        >
          {{ deleting ? 'Eliminando...' : 'Eliminar producto' }}
        </button>
      </div>
    </div>
  </div>
</template>
