import { useEffect, useState } from 'react'

function App() {
  const [workers, setWorkers] = useState([])
  const [newName, setNewName] = useState('')
  const [newLocation, setNewLocation] = useState('')

  // States for Editing
  const [editingId, setEditingId] = useState(null)
  const [editName, setEditName] = useState('')
  const [editLocation, setEditLocation] = useState('')

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

   // 3. The "Delete Worker" Function
  const deleteWorker = (id) => {
    fetch(`http://127.0.0.1:8000/workers/${id}`, {
      method: 'DELETE'
    })
    .then(() => {
      fetchWorkers() // Refresh the list after deleting
    })
  }

 // 4. The "Update Worker" Function
  const updateWorker = (id) => {
    fetch(`http://127.0.0.1:8000/workers/${id}?name=${editName}&location=${editLocation}`, {
      method: 'PUT'
    })
    .then(() => {
      fetchWorkers()
      setEditingId(null) // Turn off edit mode
    })
  }

  const startEditing = (worker) => {
    setEditingId(worker.id)
    setEditName(worker.name)
    setEditLocation(worker.location)
  }


 return (
    <div className="min-h-screen bg-linear-to-br from-green-50 to-emerald-100 p-6 md:p-10 font-sans">
      <div className="max-w-5xl mx-auto">
        
        {/* Header Section */}
        <header className="mb-8">
          <h1 className="text-4xl font-extrabold text-emerald-900 flex items-center gap-3">
            <span>🌿</span> TeamTrace
          </h1>
          <p className="text-emerald-700 font-medium mt-1">Indoor Plant Crew & Zone Manager</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* LEFT COLUMN: Add Worker Form */}
          <div className="lg:col-span-1">
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-xs border border-emerald-100">
              <h3 className="text-lg font-bold text-emerald-900 mb-4">Add New Worker</h3>
              <form onSubmit={addWorker} className="flex flex-col gap-4">
                <div>
                  <label className="text-sm font-semibold text-emerald-800 block mb-1">Worker Name</label>
                  <input 
                    placeholder="e.g., Alex" 
                    value={newName} 
                    onChange={(e) => setNewName(e.target.value)} 
                    className="w-full p-2.5 bg-white border border-emerald-200 rounded-lg focus:ring-2 focus:ring-emerald-400 focus:outline-hidden transition-all"
                  />
                </div>
                <div>
                  <label className="text-sm font-semibold text-emerald-800 block mb-1">Assigned Zone</label>
                  <input 
                    placeholder="e.g., Greenhouse A" 
                    value={newLocation} 
                    onChange={(e) => setNewLocation(e.target.value)} 
                    className="w-full p-2.5 bg-white border border-emerald-200 rounded-lg focus:ring-2 focus:ring-emerald-400 focus:outline-hidden transition-all"
                  />
                </div>
                <button 
                  type="submit" 
                  className="w-full mt-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 px-4 rounded-lg shadow-xs hover:shadow-md transition-all cursor-pointer"
                >
                  Add Worker +
                </button>
              </form>
            </div>
          </div>

          {/* RIGHT COLUMN: The Data Table */}
          <div className="lg:col-span-2">
            <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-xs border border-emerald-100 overflow-hidden">
              <div className="p-6 border-b border-emerald-100">
                <h3 className="text-lg font-bold text-emerald-900">Active Crew</h3>
                <p className="text-sm text-emerald-600">Managing placement and coverage</p>
              </div>

              <div className="overflow-x-auto">
                <table className="w-full text-left">
                  <thead className="bg-emerald-50 text-emerald-800 text-sm uppercase">
                    <tr>
                      <th className="px-6 py-3 font-semibold">Name</th>
                      <th className="px-6 py-3 font-semibold">Location / Zone</th>
                      <th className="px-6 py-3 font-semibold text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-emerald-50">
                    {workers.map((worker) => (
                      <tr key={worker.id} className="hover:bg-emerald-50/50 transition-colors">
                        
                        {/* NAME & LOCATION CELLS */}
                        {editingId === worker.id ? (
                          <>
                            <td className="px-6 py-4">
                              <input 
                                value={editName} 
                                onChange={(e) => setEditName(e.target.value)} 
                                className="w-full p-1.5 border border-emerald-300 rounded-md focus:outline-hidden focus:ring-2 focus:ring-emerald-400"
                              />
                            </td>
                            <td className="px-6 py-4">
                              <input 
                                value={editLocation} 
                                onChange={(e) => setEditLocation(e.target.value)} 
                                className="w-full p-1.5 border border-emerald-300 rounded-md focus:outline-hidden focus:ring-2 focus:ring-emerald-400"
                              />
                            </td>
                          </>
                        ) : (
                          <>
                            <td className="px-6 py-4 font-bold text-emerald-900">{worker.name}</td>
                            <td className="px-6 py-4 text-emerald-700">
                              <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800">
                                {worker.location}
                              </span>
                            </td>
                          </>
                        )}

                        {/* ACTION BUTTONS CELL */}
                        <td className="px-6 py-4 text-right">
                          <div className="flex justify-end gap-2">
                            {editingId === worker.id ? (
                              <button 
                                onClick={() => updateWorker(worker.id)} 
                                className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold py-1.5 px-3 rounded-md transition-colors cursor-pointer"
                              >
                                Save
                              </button>
                            ) : (
                              <button 
                                onClick={() => startEditing(worker)} 
                                className="bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold py-1.5 px-3 rounded-md transition-colors cursor-pointer"
                              >
                                Edit
                              </button>
                            )}
                            
                            <button 
                              onClick={() => deleteWorker(worker.id)} 
                              className="bg-rose-500 hover:bg-rose-600 text-white text-xs font-bold py-1.5 px-3 rounded-md transition-colors cursor-pointer"
                            >
                              Delete
                            </button>
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>

                {workers.length === 0 && (
                  <div className="text-center py-10 text-emerald-600">
                    <p className="text-3xl mb-2">🍃</p>
                    <p className="font-medium">No workers registered in the greenhouse yet.</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App