<template>
  <div class="hello">
    <h1>Baby growth chart</h1>
    <div class="chart">
      <object type="image/svg+xml" data="/charts/growthChart.svg">Your browser does not support iframes</object>
    </div>
   
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.chart object{
  width: 443px;
}
</style>
