import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import SearchBar from './componenets/search';

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div className="search-page">
        <SearchBar />
      </div>
    </div>
  )
}

export default App
