<script setup lang="ts">
import { useCart } from '../composables/useCart'
import { useRouter } from 'vue-router'

const { items, totalItems, totalPrice, removeItem, updateQuantity, clearCart } = useCart()
const router = useRouter()

function formatPrice(price: number) {
  return price.toFixed(2)
}

function goToHome() {
  router.push('/')
}
</script>

<template>
  <div class="cart-view">
    <div class="cart-header">
      <h1>Carrito</h1>
      <span class="cart-count" v-if="totalItems > 0">{{ totalItems }} producto(s)</span>
    </div>

    <div v-if="items.length === 0" class="cart-empty">
      <p>El carrito esta vacio.</p>
      <button class="btn btn-primary" @click="goToHome">Ver catalogo</button>
    </div>

    <div v-else>
      <div class="cart-list">
        <div
          v-for="item in items"
          :key="item.product._id"
          class="cart-item"
        >
          <div class="cart-item-image">
            <img v-if="item.product.imageUrl" :src="item.product.imageUrl" :alt="item.product.name" />
            <div v-else class="image-placeholder small">
              <span>Sin img</span>
            </div>
          </div>

          <div class="cart-item-info">
            <router-link :to="`/product/${item.product._id}`" class="cart-item-name">
              {{ item.product.name }}
            </router-link>
            <span class="cart-item-price">${{ formatPrice(item.product.price) }} c/u</span>
          </div>

          <div class="cart-item-qty">
            <button
              class="qty-btn"
              @click="updateQuantity(item.product._id, item.quantity - 1)"
            >-</button>
            <span class="qty-value">{{ item.quantity }}</span>
            <button
              class="qty-btn"
              @click="updateQuantity(item.product._id, item.quantity + 1)"
              :disabled="item.quantity >= item.product.stock"
            >+</button>
          </div>

          <div class="cart-item-subtotal">
            ${{ formatPrice(item.product.price * item.quantity) }}
          </div>

          <button class="btn-remove" @click="removeItem(item.product._id)">
            Quitar
          </button>
        </div>
      </div>

      <div class="cart-footer">
        <button class="btn btn-outline" @click="clearCart">Vaciar carrito</button>
        <div class="cart-total">
          <span>Total:</span>
          <strong>${{ formatPrice(totalPrice) }}</strong>
        </div>
      </div>

      <div class="cart-actions">
        <button class="btn btn-outline" @click="goToHome">Seguir comprando</button>
        <button class="btn btn-primary">Confirmar pedido</button>
      </div>
    </div>
  </div>
</template>
