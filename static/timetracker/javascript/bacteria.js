// function c3(x, y, r, c3col) {
//   var options = {
//     friction: 0.2,
//     restitution: 0.1,
//     angle: 0,
//     angularVelocity: 0,
//     frictionAir: 0.1,
//     mass: 10,
//   };
//   this.body = Bodies.circle(x, y, r, options);
//   this.r = r;
//   this.r2 = r;
//   this.col1 = c3col;
//   this.col2 = random(0,255);
//   this.col3 = random(0,255);
//   this.layerThickness = 1;
//   World.add(microWorld, this.body);


//   this.isOffScreen = function() {
//     var pos = this.body.position;
//     return (pos.y > height) || (pos.x > width) || (pos.y < -40) || (pos.x < -40);
//   }

//   this.show = function() {
//     var pos = this.body.position; 
//     var angle = this.body.angle;
//     push();
//     translate(pos.x, pos.y);
//     rotate(angle);
//     rectMode(CENTER);
//     strokeWeight(this.layerThickness);
//     stroke(255);
//     fill(this.col1,this.col2,this.col3);
//     ellipse(0, 0, this.r * 2, this.r2 * 2);          // p5 expects diameter!!!
//     pop();
//   }
// }