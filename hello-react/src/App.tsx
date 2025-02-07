import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/hello')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error fetching API', error));
  }, [])

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Full Stack App</h1>
      <p>{message ? message: "Loading..."}</p>
    </div>
  )
}

export default App;