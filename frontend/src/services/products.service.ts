import api from './api'
import type { Product } from '../types/Product'

export async function getProducts(params?: { search?: string; category?: string }) {
  const response = await api.get<Product[]>('/products', { params })
  return response.data
}

export async function getProductById(id: string) {
  const response = await api.get<Product>(`/products/${id}`)
  return response.data
}

export async function createProduct(data: Omit<Product, '_id'>) {
  const response = await api.post<Product>('/products', data)
  return response.data
}

export async function updateProduct(id: string, data: Partial<Omit<Product, '_id'>>) {
  const response = await api.put<Product>(`/products/${id}`, data)
  return response.data
}

export async function deleteProduct(id: string) {
  const response = await api.delete(`/products/${id}`)
  return response.data
}
