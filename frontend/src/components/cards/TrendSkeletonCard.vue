<template>
  <v-card class="mx-auto border border-success">
    <v-skeleton-loader type="card-heading" />
    <v-card-actions>
      <v-skeleton-loader type="button" />
      <v-spacer />
      <v-btn icon disabled color="warning">
        <v-icon>mdi-star-outline</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({});
</script>

<style>
</style>