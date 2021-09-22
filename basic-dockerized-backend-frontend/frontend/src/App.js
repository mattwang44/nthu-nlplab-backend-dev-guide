import React, { useState, useEffect } from "react";
import './App.css';

function App() {
  const [counter, setCounter] = useState({
    loading: false,
    count: null,
  });
  const api_host = process.env.REACT_APP_API_HOST;

  useEffect(() => {
    setCounter({loading: true})
    fetch(`${api_host}/counter`)
      .then((res) => res.json())
      .then(({count}) => {
        setCounter({ loading: false, count: count });
      });
  }, [api_host, setCounter]);


  // increment on click
  const handleClick = (num) =>  async () => {
    setCounter({ loading: false });
    await fetch(`${api_host}/counter`, {
      method: "POST",
      body: JSON.stringify({num}),
      dataType: "JSON",
      headers: {
          "Content-Type": "application/json; charset=utf-8"
      }
    })
      .then((res) => res.json())
      .then(({count}) => {
        setCounter({ loading: false, count: count });
      });
  }

  if (counter.loading) {
    return "loading...";
  }

  return (
    <div style={{ 'margin-left': '10px' }}>
      <p style={{'font-size':'30px'}}>{counter.count}</p>
      <button onClick={handleClick(1)}>+1</button>
      <button onClick={handleClick(-1)}>-1</button>
    </div>
  );
}

export default App;
