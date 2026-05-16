export interface Category {
  _id: string
  name: string
}

export interface Product {
  _id: string
  name: string
  price: number
  description: string
  categoryId: string
  stock: number
  imageUrl: string
}
