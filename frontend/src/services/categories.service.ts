import api from './api'
import type { Category } from '../types/Product'

export async function getCategories() {
  const response = await api.get<any[]>('/categories')
  return response.data.map((c: any) => ({ ...c, _id: c._id || c.id }))
}
