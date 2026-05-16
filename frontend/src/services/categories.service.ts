import api from './api'
import type { Category } from '../types/Product'

export async function getCategories() {
  const response = await api.get<Category[]>('/categories')
  return response.data
}
