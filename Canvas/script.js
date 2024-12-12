const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const drawButton = document.getElementById('drawButton');

//full window size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Store clicked points
let points = [];

//  mouse click
canvas.addEventListener('click', (event) => {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;

  const newPoint = { x, y };
  points.push(newPoint);

  drawDot(newPoint); // Show clicked point
});

// Draw a dot 
function drawDot(point) {
  ctx.beginPath();
  ctx.arc(point.x, point.y, 3, 0, 2 * Math.PI);
  ctx.fill();
}

//  draw a circle
function drawCircle(p1, p2) {
  const centerX = (p1.x + p2.x) / 2;
  const centerY = (p1.y + p2.y) / 2;

  const dx = p2.x - p1.x;
  const dy = p2.y - p1.y;
  const radius = Math.sqrt(dx * dx + dy * dy)/2;

  ctx.beginPath();
  ctx.arc(centerX,centerY, radius, 0, 2 * Math.PI);
  ctx.stroke();
}

//  draw a rectangle
function drawRectangle(p1, p2, p3, p4) {
  ctx.beginPath();
  ctx.moveTo(p1.x, p1.y);
  ctx.lineTo(p2.x, p2.y);
  ctx.lineTo(p3.x, p3.y);
  ctx.lineTo(p4.x, p4.y);
  ctx.closePath();
  ctx.stroke();
}

//  to draw a triangle
function drawTriangle(p1, p2, p3) {
  ctx.beginPath();
  ctx.moveTo(p1.x, p1.y);
  ctx.lineTo(p2.x, p2.y);
  ctx.lineTo(p3.x, p3.y);
  ctx.closePath();
  ctx.stroke();
}

// draw shape
drawButton.addEventListener('click', () => {
  
  if (points.length === 2) {
    drawCircle(points[0], points[1]);
  } else if (points.length === 3) {
    drawTriangle(points[0], points[1], points[2]);
  } else if (points.length === 4) {
    drawRectangle(points[0], points[1], points[2], points[3]);
  } else {
    alert('Click 2 points for a circle,3 for a triangle, or 4 for a rectangle!');
  }

  points = []; //reset point
});
          