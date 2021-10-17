import io from 'socket.io-client';
let socket = io('http://localhost:5000', {
  transports: [
    'websocket',
    'flashsocket',
    'jsonp-polling',
    'xhr-polling',
    'htmlfile',
  ],
});

export default socket;
