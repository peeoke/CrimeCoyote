import City from './components/city';
import Graph from './components/graph'

const cityStats = () => {
    return (
    <div className="flex">
        <div className="w-1/2">
            <Graph />
        </div>
        <div className="w-1/2">
            <h1 className=""> <City /> </h1>
        </div>
    </div>
    );
  };
  
export default cityStats;