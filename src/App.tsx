import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import CityStats from './pages/city-stats'
import Menu from './pages/components/menu';

function App() {
  return (
    <Router>
      <Menu />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/city-stats" element={<CityStats />} />
        </Routes>
    </Router>
  );
};

export default App
