import City from './components/city';
import Graph from './components/graph'

const cityStats = () => {
    return (
        <div className="city-info">
            <Graph />
            <h1 className="city-name"> <City /> </h1>
        </div>
    );
  };
  
export default cityStats;