<template>
  <v-container>
    <h2>Избранные тренды</h2>
    <v-row>
      <v-col cols="2"> </v-col>
      <v-col cols="8">
        <v-row
          class="text-center"
          v-if="favoriteTrends.items.length == 0 && !loadingFavoriteTrends"
        >
          <v-col
            ><p>Здесь пока что ничего нет</p>
            <v-btn color="primary" :to="{ name: 'News' }"
              >Перейти к новостям</v-btn
            ></v-col
          >
        </v-row>
        <v-row
          v-for="trend in favoriteTrends.items"
          :key="`favoriteTrend-${trend.id}`"
          ><v-col> <trend-card :trend="trend" /> </v-col
        ></v-row>

        <div v-if="favoriteTrends.next" v-intersect="getFavoriteTrends">
          <v-row
            ><v-col><digest-skeleton-card /></v-col
          ></v-row>
          <v-row
            ><v-col><digest-skeleton-card /></v-col
          ></v-row>
          <v-row
            ><v-col><digest-skeleton-card /></v-col
          ></v-row>
        </div>
      </v-col>
      <v-col cols="2">&nbsp;</v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import TrendCard from "@/components/cards/TrendCard.vue";
import DigestSkeletonCard from "@/components/cards/DigestSkeletonCard.vue";
import Vue from "vue";
import { mapActions, mapState } from "vuex";
export default Vue.extend({
  components: { DigestSkeletonCard, TrendCard },
  computed: {
    ...mapState(["favoriteTrends", "loadingFavoriteTrends"]),
  },
  methods: {
    ...mapActions(["getFavoriteTrends"]),
  },
  async mounted() {
    await this.getFavoriteTrends({ page: 1 });
  },
});
</script>
<style>
</style>