function c3(x, y, r, c3col) {
  var options = {
    friction: 0.2,
    restitution: 0.1,
    angle: 0,
    angularVelocity: 0,
    frictionAir: 0.1,
    mass: 10,
  };
  this.body = Bodies.circle(x, y, r, options);
  this.r = r;
  this.r2 = r;
  this.col1 = 0;
  this.col2 = c3col;
  this.col3 = random(0,255);
  this.layerThickness = 1;
  World.add(microWorld, this.body);


  this.isOffScreen = function() {
    var pos = this.body.position;
    return (pos.y > height) || (pos.x > width) || (pos.y < -40) || (pos.x < -40);
  }

  this.show = function() {
    var pos = this.body.position; 
    var angle = this.body.angle;
    push();
    translate(pos.x, pos.y);
    rotate(angle);
    rectMode(CENTER);
    strokeWeight(this.layerThickness);
    stroke(255);
    fill(this.col1,this.col2,this.col3);
    ellipse(0, 0, this.r * 2, this.r2 * 2);          // p5 expects diameter!!!
    pop();
  }
}
function proteinGenerator(frequency, spwnnumber) {
    if (((60 + frequency) > frameRate() && frameRate() > (60 - frequency)) || (frequency == 555)) {
      for (var i = 0; i < spwnnumber; i++) {
          proteins.push(new c3(random(-50, 0), random(-50, 0), random(5,10), random(5,10), random(0,255)));
      }
    }
  }







var Engine = Matter.Engine, World = Matter.World, Bodies = Matter.Bodies; Body = Matter.Body;
var engine, world;
//********************************************************** */
//* Your variables
//*
//****/
var proteins = [];
var theR = 80;
var theG = 120;
var theB = 60;
var canvasWidth = 800;
var canvasHeight = 500;

function setup() {
  createCanvas(canvasWidth, canvasHeight);
  microEngine = Engine.create();
  microWorld = microEngine.world;
  //********************************************************** */
  //* Setup Code here
  //*
  //****/
  // initProteins(20);
  microWorld.gravity.x = 0.4;
  microWorld.gravity.y = 0.4;









}
// function mouseDragged() {
//   proteins.push(new c3(mouseX, mouseY, random(10,20), random(10,20), random(0,255))); 
// }
function draw() {
  background(theR,theG,theB);
  Engine.update(microEngine);
  //********************************************************** */
  //* Draw Code here
  //*
  //****/
  // console.log(proteins);
  var theframeRate = frameRate();
  proteinGenerator(0.05, 10)
  if (theframeRate < 50) {
    console.log(theframeRate);
  }
  // console.log(theframeRate);
  for (var i = 0; i < proteins.length; i++){
    proteins[i].show();
    proteins[i].body.position.x += random(-0.1,0.2);
    proteins[i].body.position.y += random(-0.1,0.1);
    if (proteins[i].isOffScreen()) {
      proteins.splice(i, 1);
      i--;                                        //to avoid the "blinking"
    }
  }














  
}
