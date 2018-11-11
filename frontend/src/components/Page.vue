<template>
	<div class="loading fa-3x" v-if="$apollo.loading">
		<font-awesome-icon icon="spinner" class="fa-spin"></font-awesome-icon>
	</div>
	<span v-else>
		<span v-html="setTitle()"></span>
		<span v-html="page.content"></span>
	</span>
</template>

<script>
import gql from "graphql-tag";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faSpinner } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faSpinner);

const PageQ = gql`
  query page($url: String!) {
    page(url: $url) {
      title
      content
    }
  }
`;

export default {
  name: "Page",
  components: {
    FontAwesomeIcon
  },
  methods: {
    setTitle() {
      document.title = this.page.title;
    }
  },
  apollo: {
    page() {
      return {
        query: PageQ,
        variables() {
          return {
            url: this.$route.params["0"]
          };
        },
        options: {
          fetchPolicy: "cache-and-network"
        }
      };
    }
  }
};
</script>

<style scoped>
.loading {
  position: relative;
  top: 4em;
  text-align: center;
  color: grey;
  z-index: 1;
}
</style>