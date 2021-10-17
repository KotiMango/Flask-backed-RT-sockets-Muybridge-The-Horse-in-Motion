import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import socket from './socket';

function App() {
  const [horseObj, setHorseObj] = useState('');
  function useInterval(callback, delay) {
    const intervalRef = React.useRef(null);
    const savedCallback = React.useRef(callback);
    React.useEffect(() => {
      savedCallback.current = callback;
    }, [callback]);
    React.useEffect(() => {
      const tick = () => savedCallback.current();
      if (typeof delay === 'number') {
        intervalRef.current = window.setInterval(tick, delay);
        return () => window.clearInterval(intervalRef.current);
      }
    }, [delay]);
    return intervalRef;
  }
  useEffect(() => {
    socket.on('connect', (payload) => {
      setHorseObj((prevState) => {
        return prevState?.idx === 0 ? prevState : payload;
      });
    });
    socket.on('fetch', (payload) => {
      setHorseObj((prevState) => {
        return payload;
      });
    });
    return () => socket.close();
  }, []);

  useInterval(() => socket.emit('send', horseObj), 500);

  return (
    <div className='App'>
      <img src={`data:image/png;base64, ${horseObj.link}`} />
      <h1>{horseObj.idx + 1}</h1>
    </div>
  );
}

export default App;
