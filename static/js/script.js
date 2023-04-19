const canvas = document.getElementById('whiteboard');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.8;

let drawing = false;
let color = 'black';
let tool = 'freehand';

const clearButton = document.getElementById('clear');
clearButton.addEventListener('click', () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});

const setColorButtons = () => {
  const colorButtons = document.querySelectorAll('.color');
  colorButtons.forEach((button) => {
    button.style.backgroundColor = button.id;
    button.addEventListener('click', () => {
      color = button.id;
    });
  });
};
setColorButtons();

const playerButton = document.getElementById('player');
playerButton.addEventListener('click', () => {
  tool = 'player';
});

const arrowButton = document.getElementById('arrow');
arrowButton.addEventListener('click', () => {
  tool = 'arrow';
});

const lineButton = document.getElementById('line');
lineButton.addEventListener('click', () => {
  tool = 'line';
});

const eraseButton = document.getElementById('erase');
eraseButton.addEventListener('click', () => {
  tool = 'erase';
});

const freehandButton = document.getElementById('freehand');
if (freehandButton) {
  freehandButton.addEventListener('click', () => {
    tool = 'freehand';
  });
}

const drawLine = (x1, y1, x2, y2) => {
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;
  ctx.stroke();
};

const drawPlayer = (x, y) => {
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, 2 *Math.PI);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.stroke();
  };
  
  const drawArrow = (fromX, fromY, toX, toY) => {
  const headLen = 10;
  const dx = toX - fromX;
  const dy = toY - fromY;
  const angle = Math.atan2(dy, dx);
  
  drawLine(fromX, fromY, toX, toY);
  
  const x1 = toX - headLen * Math.cos(angle - Math.PI / 6);
  const y1 = toY - headLen * Math.sin(angle - Math.PI / 6);
  const x2 = toX - headLen * Math.cos(angle + Math.PI / 6);
  const y2 = toY - headLen * Math.sin(angle + Math.PI / 6);
  
  drawLine(toX, toY, x1, y1);
  drawLine(toX, toY, x2, y2);
  };
  
  const erase = (x, y) => {
  ctx.clearRect(x - 10, y - 10, 20, 20);
  };
  
  let startX;
  let startY;
  let savedCanvas;
  
  const saveCanvasState = () => {
  savedCanvas = ctx.getImageData(0, 0, canvas.width, canvas.height);
  };
  
  canvas.addEventListener('mousedown', (e) => {
  drawing = true;
  startX = e.clientX - canvas.offsetLeft;
  startY = e.clientY - canvas.offsetTop;
  saveCanvasState();
  
  if (tool === 'player') {
  drawPlayer(startX, startY);
  } else if (tool === 'freehand') {
  ctx.beginPath();
  ctx.moveTo(startX, startY);
  }
  });
  
  canvas.addEventListener('mousemove', (e) => {
  if (!drawing) return;
  
  const x = e.clientX - canvas.offsetLeft;
  const y = e.clientY - canvas.offsetTop;
  
  if (tool === 'freehand') {
  ctx.lineTo(x, y);
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;
  ctx.lineCap = 'round';
  ctx.stroke();
  } else if (tool === 'line') {
  ctx.putImageData(savedCanvas, 0, 0);
  drawLine(startX, startY, x, y);
  } else if (tool === 'arrow') {
  ctx.putImageData(savedCanvas, 0, 0);
  drawArrow(startX, startY, x, y);
  } else if (tool === 'erase') {
  erase(x, y);
  }
  });
  
  canvas.addEventListener('mouseup', () => {
  drawing = false;
  });
  
  canvas.addEventListener('mouseleave', () => {
  drawing = false;
  });
  
  let activeTextElement;

  const createTextElement = (x, y, text) => {
    const textDiv = document.createElement('div');
    textDiv.style.position = 'absolute';
    textDiv.style.left = `${x}px`;
    textDiv.style.top = `${y}px`;
    textDiv.style.color = color;
    textDiv.style.font = '16px Arial';
    textDiv.textContent = text;
    textDiv.classList.add('draggable-text');
    document.body.appendChild(textDiv);
  
    $(textDiv).draggable({
      stop: () => {
        activeTextElement = textDiv;
      },
    });
  };
  
  canvas.addEventListener('click', (e) => {
    if (tool === 'text') {
      const x = e.clientX - canvas.offsetLeft + window.pageXOffset;
      const y = e.clientY - canvas.offsetTop + window.pageYOffset;
      createTextElement(x, y, textInput.value);
    }
  });
  

  
  