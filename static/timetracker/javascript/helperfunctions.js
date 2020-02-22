function randi(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
function initProteins(num) {
  for (i = 0; i < num; i++) {
    proteins.push(new c3(random(100,700), random(100,400), random(3,8), random(0,255)));
  }
}