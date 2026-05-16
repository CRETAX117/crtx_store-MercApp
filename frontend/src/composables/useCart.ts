import { ref, computed } from 'vue'
import type { Product } from '../types/Product'

interface CartItem {
  product: Product
  quantity: number
}

const STORAGE_KEY = 'crtx_cart'

function loadFromStorage(): CartItem[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : []
  } catch {
    return []
  }
}

function saveToStorage(items: CartItem[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items))
}

const items = ref<CartItem[]>(loadFromStorage())

export function useCart() {
  function addItem(product: Product) {
    const existing = items.value.find(i => i.product._id === product._id)
    if (existing) {
      if (existing.quantity < product.stock) {
        existing.quantity++
      }
    } else {
      items.value.push({ product, quantity: 1 })
    }
    saveToStorage(items.value)
  }

  function removeItem(productId: string) {
    items.value = items.value.filter(i => i.product._id !== productId)
    saveToStorage(items.value)
  }

  function updateQuantity(productId: string, quantity: number) {
    const item = items.value.find(i => i.product._id === productId)
    if (!item) return
    if (quantity <= 0) {
      removeItem(productId)
    } else if (quantity <= item.product.stock) {
      item.quantity = quantity
      saveToStorage(items.value)
    }
  }

  function clearCart() {
    items.value = []
    saveToStorage(items.value)
  }

  const totalItems = computed(() =>
    items.value.reduce((acc, i) => acc + i.quantity, 0)
  )

  const totalPrice = computed(() =>
    items.value.reduce((acc, i) => acc + i.product.price * i.quantity, 0)
  )

  return {
    items,
    totalItems,
    totalPrice,
    addItem,
    removeItem,
    updateQuantity,
    clearCart
  }
}
