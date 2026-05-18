import api from './api'
import type { Product } from '../types/Product'

// El backend devuelve "id" pero el frontend usa "_id"
function mapProduct(data: any): Product {
  return { ...data, _id: data._id || data.id }
}

export async function getProducts(params?: { search?: string; category?: string }) {
  const response = await api.get<any[]>('/products', { params })
  return response.data.map(mapProduct)
}

export async function getProductById(id: string) {
  const response = await api.get<any>(`/products/${id}`)
  return mapProduct(response.data)
}

export async function createProduct(data: Omit<Product, '_id'>) {
  const response = await api.post<any>('/products', data)
  return mapProduct(response.data)
}

export async function updateProduct(id: string, data: Partial<Omit<Product, '_id'>>) {
  const response = await api.put<any>(`/products/${id}`, data)
  return mapProduct(response.data)
}

export async function deleteProduct(id: string) {
  const response = await api.delete(`/products/${id}`)
  return response.data
}
