var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer({antialias: true});
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

 var light = new THREE.PointLight(0xe44269, 1, 0)
 var light2 = new THREE.PointLight(0xe44269, 1, 0)
 var light3 = new THREE.PointLight(0xe44269, 1, 0)
 
light.position.set(-10, 1, 10)
light2.position.set(10, 1, 10)
// light3.position.set(-20, 0, -20)

scene.add(light);
scene.add(light2);
// scene.add(light3);

var geometry = new THREE.BoxGeometry( 1, 1, 1 );
var material = new THREE.MeshPhongMaterial( { color: 0xffffff, side: THREE.DoubleSide } );

var HEIGHT = 20;
var WIDTH = 20;

cubes = [];

var gofCurrentStep = [];
var gofNextStep = [];

// initialize gof
for (var i = 0; i < WIDTH; i++) {
  gofCurrentStep[i] = []
  gofNextStep[i] = []
  for (var j = 0; j < HEIGHT; j++) {
        gofCurrentStep[i][j] = Math.random() > 0.5;
    }
}

function refreshTable() {
    for (var i = 0; i < WIDTH; i++) {
    for (var j = 0; j < HEIGHT; j++) {
      gofCurrentStep[i][j] = gofNextStep[i][j];
    }
  }
}

function doGofStep() {
  for (var i = 0; i < WIDTH; i++) {
    for (var j = 0; j < HEIGHT; j++) {
      var aliveNeighbours = (i > 0 && j > 0 && gofCurrentStep[i - 1][j - 1]) + 
                            (i > 0 && gofCurrentStep[i - 1][j]) +
                            (i > 0 && (j+1) < HEIGHT && gofCurrentStep[i - 1][j + 1]) +
                            (j > 0 && gofCurrentStep[i][j - 1]) +
                            ((j+1) < HEIGHT && gofCurrentStep[i][j + 1]) + 
                            ( (i+1) < WIDTH && j > 0 && gofCurrentStep[i + 1][j - 1]) +
                            ( (i+1) < WIDTH && gofCurrentStep[i + 1][j]) +
                            ( (i+1) < WIDTH && (j+1) < HEIGHT && gofCurrentStep[i + 1][j + 1])
      
     
      gofNextStep[i][j] = gofCurrentStep[i][j];
      if (gofCurrentStep[i][j]) {
       if (aliveNeighbours < 2)  gofNextStep[i][j] = false;
       if (aliveNeighbours > 3)  gofNextStep[i][j] = false;
     } else {
       if (aliveNeighbours === 3) gofNextStep[i][j] = true;
     }
      
      
    }
  }
}

function doPlane(r) {
  for (var i = 0; i < WIDTH; i++) {
    for (var j = 0; j < HEIGHT; j++) {
      var cube = new THREE.Mesh( geometry, material );
      cube.position.x = i - 10;
      cube.position.y = -10 + r;
      cube.position.z = j - 10;
      cubes.push(cube);
      if (gofCurrentStep[i][j]) scene.add( cube );
    }
  }
  doGofStep();
  refreshTable();
}

var planeCounter = 1;
doPlane(0);

var controls = new THREE.OrbitControls( camera, renderer.domElement );
controls.autoRotate = true;
controls.enableKeys = true;

camera.position.z = 25;
camera.position.y = 10;
// camera.rotation.z = 0.4;
// camera.rotation.y = 0.4;
// camera.rotation.x = 0.3;
// camera.rotation.x = 1;
// camera.position.y = -25;
// camera.position.x = 10;

controls.update();

var ccc = 0;
var generating = true;

function stop () {
  generating = !generating;
}

function restart() {
  cubes.forEach(function(cube) {
    scene.remove(cube);
  })
  cubes = [];
  for (var i = 0; i < WIDTH; i++) {
  gofCurrentStep[i] = []
  gofNextStep[i] = []
  for (var j = 0; j < HEIGHT; j++) {
          gofCurrentStep[i][j] = Math.random() > 0.5;
      }
  }
  planeCounter = 1;
  camera.position.z = 25;
  camera.position.y = 10;
  light.position.set(-10, 1, 10)
  light2.position.set(10, 1, 10)
  controls.update();
}

/*
document.addEventListener('keyup', function (e) {
  console.log(e.keyCode);
  if (e.keyCode === 82) {
    restart();
  }
  if (e.keyCode === 83) {
    stop();
  }
});
*/
document.getElementById("stop").addEventListener('click', stop);
document.getElementById("restart").addEventListener('click', restart);

function animate() {
	requestAnimationFrame( animate );
  
  if (generating) {
      camera.position.y += 0.025;
      light.position.y += 0.025;
      light2.position.y += 0.025;
      ccc++;
      if (ccc === 42) {
        doPlane(planeCounter);
        planeCounter++;
        ccc = 0;
      }
    }
  
  controls.autoRotate = generating;
  controls.update();
  
	renderer.render( scene, camera );
}
animate();

//TODO: on resize
window.addEventListener( 'resize', onWindowResize, false );

function onWindowResize(){

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}