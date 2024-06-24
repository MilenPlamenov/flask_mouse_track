const socket = io();

document.addEventListener('mousemove', (event) => {
    const x = event.clientX;
    const y = event.clientY;
    socket.emit('mouse_move', { x, y });
});

document.addEventListener('click', (event) => {
    const x = event.clientX;
    const y = event.clientY;
    socket.emit('mouse_click', { x, y });
});

socket.on('update_position', (data) => {
    document.getElementById('position').innerText = `X: ${data.x}, Y: ${data.y}`;
});
