import { useEffect, useState } from 'react'

function App() {
  const [workers, setWorkers] = useState([])
  const [newName, setNewName] = useState('')
  const [newLocation, setNewLocation] = useState('')

  // 1. Fetch the list (Existing)
  const fetchWorkers = () => {
    fetch("http://127.0.0.1:8000/workers")
      .then((res) => res.json())
      .then((data) => setWorkers(data))
  }

  useEffect(() => {
    fetchWorkers()
  }, [])

  // 2. The "Add Worker" Function
  const addWorker = (e) => {
    e.preventDefault() // Prevents the page from refreshing
    
    fetch(`http://127.0.0.1:8000/workers?name=${newName}&location=${newLocation}`, {
      method: 'POST'
    })
    .then(() => {
      fetchWorkers() // Refresh the list after adding
      setNewName('') // Clear the inputs
      setNewLocation('')
    })
  }

  return (
    <div style={{ padding: '40px', backgroundColor: '#f0fdf4', minHeight: '100vh', fontFamily: 'sans-serif' }}>
      <h1 style={{ color: '#166534' }}>🌿 TeamTrace: Plant Manager</h1>

      {/* --- ADD WORKER FORM --- */}
      <form onSubmit={addWorker} style={{ marginBottom: '30px', background: '#dcfce7', padding: '20px', borderRadius: '12px' }}>
        <h3>Add New Worker</h3>
        <input 
          placeholder="Name (e.g. Orlandy)" 
          value={newName} 
          onChange={(e) => setNewName(e.target.value)}
          style={{ padding: '8px', marginRight: '10px', borderRadius: '4px', border: '1px solid #ccc' }}
        />
        <input 
          placeholder="Location (e.g. Greenhouse A)" 
          value={newLocation} 
          onChange={(e) => setNewLocation(e.target.value)}
          style={{ padding: '8px', marginRight: '10px', borderRadius: '4px', border: '1px solid #ccc' }}
        />
        <button type="submit" style={{ padding: '8px 16px', backgroundColor: '#22c55e', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
          Add +
        </button>
      </form>

      {/* --- WORKER LIST --- */}
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {workers.map((worker) => (
          <li key={worker.id} style={{ background: 'white', margin: '10px 0', padding: '15px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
            <strong>{worker.name}</strong> — {worker.location}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App