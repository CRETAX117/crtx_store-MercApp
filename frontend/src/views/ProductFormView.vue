<script setup lang="ts">
// placeholder para la Fase 3 (formulario crear/editar producto)
import { useRoute } from 'vue-router'

const route = useRoute()
const isEdit = !!route.params.id
</script>

<template>
  <div class="form-view">
    <h1>{{ isEdit ? 'Editar producto' : 'Nuevo producto' }}</h1>
    <p class="state-message">Formulario disponible en la Fase 3.</p>
    <router-link to="/" class="btn btn-outline">Volver</router-link>
  </div>
</template>
