import { ref, computed } from 'vue'
import { getProducts } from '../services/products.service'
import { getCategories } from '../services/categories.service'
import type { Product, Category } from '../types/Product'

// maneja el catalogo de productos con busqueda y filtro por categoria
export function useProducts() {
  const products = ref<Product[]>([])
  const categories = ref<Category[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const search = ref('')
  const selectedCategory = ref('')

  async function loadCategories() {
    try {
      categories.value = await getCategories()
    } catch {
      // si falla, el select queda vacio
    }
  }

  async function loadProducts() {
    loading.value = true
    error.value = null
    try {
      const params: { search?: string; category?: string } = {}
      if (search.value.trim()) params.search = search.value.trim()
      if (selectedCategory.value) params.category = selectedCategory.value
      products.value = await getProducts(params)
    } catch (err: any) {
      error.value = err.response?.data?.error || 'No se pudieron cargar los productos'
    } finally {
      loading.value = false
    }
  }

  const categoryName = computed(() => {
    return (id: string) => {
      const cat = categories.value.find(c => c._id === id)
      return cat ? cat.name : 'Sin categoria'
    }
  })

  return {
    products,
    categories,
    loading,
    error,
    search,
    selectedCategory,
    loadProducts,
    loadCategories,
    categoryName
  }
}
