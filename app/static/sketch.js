var canvas;
var dotArray=[]
console.log("linked")

function windowResized(){
    console.log("resized");
}

function setup() {
  canvas=createCanvas(windowWidth, windowHeight);
  canvas.position(0,0);
  canvas.style('z-index','-1');
  colorMode(HSB);
  console.log("setup run")
  
    for(var i=0; i<30; i++){
    let x=random(0,width)
    let y=random(0,height)
    
    dotArray[i]= new Constellation(x,y)
    
  }
}

function draw() {
  var hue = map(mouseX,0,windowWidth,0,360);
  var saturation = map(mouseY,0,windowHeight,60,100);
  background(hue,saturation,80);
  
  for(var i=0;i<dotArray.length;i++){
    dotArray[i].move()
    dotArray[i].display()
    
    if (i>0){
      line(dotArray[i].x,dotArray[i].y,dotArray[i-1].x,dotArray[i-1].y)
    }
  }
}

function mouseClicked(){
 dotArray.push(new Constellation(random(0,width),random(0,height))) 
}

//class


class Constellation{
  constructor(x,y){
   this.x=x
   this.y=y
   this.xSpeed = random(-2,2)
   this.ySpeed = random(-2,2)
   this.col = color(255, 50)
   this.diameter = 25
   this.fromMouse = dist(mouseX,mouseY,this.x,this.y)
  }
  
  display(){
    stroke(255);
    fill(this.col);
    strokeWeight(3);
    ellipse(this.x,this.y,this.diameter)
    // scribble.scribbleEllipse(this.x, this.y, this.diameter,this.diameter); 
  }
  
    move(){
    this.x = this.x + this.xSpeed
    this.y = this.y + this.ySpeed
    this.fromMouse=dist(mouseX,mouseY,this.x,this.y)
    
    if (this.x > width || this.x < 0 || this.fromMouse<this.diameter/2){
      this.xSpeed=this.xSpeed*-1
    }
      
    if (this.y > height || this.y < 0 || this.fromMouse<this.diameter/2){
      this.ySpeed=this.ySpeed*-1
    }
  }
  
}