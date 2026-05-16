<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProductById, createProduct, updateProduct } from '../services/products.service'
import { getCategories } from '../services/categories.service'
import type { Category } from '../types/Product'

const route = useRoute()
const router = useRouter()

const isEdit = !!route.params.id

// campos del formulario
const name = ref('')
const price = ref<number | ''>('')
const description = ref('')
const categoryId = ref('')
const stock = ref<number | ''>(0)
const imageUrl = ref('')

const categories = ref<Category[]>([])
const loading = ref(false)
const loadingData = ref(false)
const errors = ref<Record<string, string>>({})
const submitError = ref<string | null>(null)

onMounted(async () => {
  loadingData.value = true
  try {
    categories.value = await getCategories()

    if (isEdit) {
      const product = await getProductById(route.params.id as string)
      name.value = product.name
      price.value = product.price
      description.value = product.description
      categoryId.value = product.categoryId
      stock.value = product.stock
      imageUrl.value = product.imageUrl || ''
    }
  } catch {
    submitError.value = 'No se pudo cargar la informacion'
  } finally {
    loadingData.value = false
  }
})

function validate(): boolean {
  errors.value = {}

  if (!name.value || name.value.trim().length < 3) {
    errors.value.name = 'El nombre debe tener al menos 3 caracteres'
  }
  if (price.value === '' || Number(price.value) <= 0) {
    errors.value.price = 'El precio debe ser mayor a 0'
  }
  if (!description.value.trim()) {
    errors.value.description = 'La descripcion es obligatoria'
  }
  if (!categoryId.value) {
    errors.value.categoryId = 'Selecciona una categoria'
  }
  if (stock.value !== '' && (Number(stock.value) < 0 || !Number.isInteger(Number(stock.value)))) {
    errors.value.stock = 'El stock debe ser un numero entero mayor o igual a 0'
  }

  return Object.keys(errors.value).length === 0
}

async function handleSubmit() {
  if (!validate()) return

  loading.value = true
  submitError.value = null

  const payload = {
    name: name.value.trim(),
    price: Number(price.value),
    description: description.value.trim(),
    categoryId: categoryId.value,
    stock: stock.value === '' ? 0 : Number(stock.value),
    imageUrl: imageUrl.value.trim()
  }

  try {
    if (isEdit) {
      await updateProduct(route.params.id as string, payload)
      router.push(`/product/${route.params.id}`)
    } else {
      const created = await createProduct(payload)
      router.push(`/product/${created._id}`)
    }
  } catch (err: any) {
    submitError.value = err.response?.data?.error || 'Error al guardar el producto'
  } finally {
    loading.value = false
  }
}

function goBack() {
  router.back()
}
</script>

<template>
  <div class="form-view-full">
    <div class="form-header">
      <h1>{{ isEdit ? 'Editar producto' : 'Nuevo producto' }}</h1>
      <button class="btn btn-outline" @click="goBack">Volver</button>
    </div>

    <div v-if="loadingData" class="state-message">Cargando...</div>

    <form v-else class="product-form" @submit.prevent="handleSubmit">
      <div v-if="submitError" class="form-alert error">{{ submitError }}</div>

      <div class="form-group">
        <label for="field-name">Nombre</label>
        <input
          id="field-name"
          v-model="name"
          type="text"
          class="form-input"
          :class="{ invalid: errors.name }"
          placeholder="Nombre del producto"
        />
        <span v-if="errors.name" class="field-error">{{ errors.name }}</span>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="field-price">Precio ($)</label>
          <input
            id="field-price"
            v-model="price"
            type="number"
            step="0.01"
            min="0.01"
            class="form-input"
            :class="{ invalid: errors.price }"
            placeholder="0.00"
          />
          <span v-if="errors.price" class="field-error">{{ errors.price }}</span>
        </div>

        <div class="form-group">
          <label for="field-stock">Stock</label>
          <input
            id="field-stock"
            v-model="stock"
            type="number"
            min="0"
            step="1"
            class="form-input"
            :class="{ invalid: errors.stock }"
            placeholder="0"
          />
          <span v-if="errors.stock" class="field-error">{{ errors.stock }}</span>
        </div>
      </div>

      <div class="form-group">
        <label for="field-category">Categoria</label>
        <select
          id="field-category"
          v-model="categoryId"
          class="form-input"
          :class="{ invalid: errors.categoryId }"
        >
          <option value="" disabled>Selecciona una categoria</option>
          <option
            v-for="cat in categories"
            :key="cat._id"
            :value="cat._id"
          >
            {{ cat.name }}
          </option>
        </select>
        <span v-if="errors.categoryId" class="field-error">{{ errors.categoryId }}</span>
      </div>

      <div class="form-group">
        <label for="field-description">Descripcion</label>
        <textarea
          id="field-description"
          v-model="description"
          class="form-input form-textarea"
          :class="{ invalid: errors.description }"
          placeholder="Describe el producto..."
          rows="4"
        ></textarea>
        <span v-if="errors.description" class="field-error">{{ errors.description }}</span>
      </div>

      <div class="form-group">
        <label for="field-image">URL de imagen (opcional)</label>
        <input
          id="field-image"
          v-model="imageUrl"
          type="text"
          class="form-input"
          placeholder="https://..."
        />
      </div>

      <div class="form-submit">
        <button type="submit" class="btn btn-primary btn-full" :disabled="loading">
          {{ loading ? 'Guardando...' : isEdit ? 'Guardar cambios' : 'Crear producto' }}
        </button>
      </div>
    </form>
  </div>
</template>
