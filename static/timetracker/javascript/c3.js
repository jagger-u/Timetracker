// function c3(x, y, w, h, c3col) {
//   var options = {
//     friction: 0.3,
//     restitution: 0,
//     angle: 0,
//     angularVelocity: 0,
//     frictionAir: 0.1,
//     mass: 10,
//     chamfer: { radius: 30 }
//   };

//   this.body = Bodies.rectangle(x, y, w, h, options);
//   this.w = w;
//   this.h = h;
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
//     rect(0, 0, this.w*2, this.h*2, 15);          // p5 expects diameter!!!
//     pop();
//   }
// }