import React, { useEffect, useState } from 'react';

export interface City {
  Name: string;
}

const City = () => {
  const [data, setData] = useState(null)
    useEffect(() => {
        
    const getCity = async () => {
      try{
      const response = await fetch('http://127.0.0.1:5000/result');
      const data = await response.json()
  
        setData(data);
      }catch(error){
        console.error('Error fetching data:', error);      
      }
    };
        getCity(); // Call getCity function on mount
      }, []);
      console.log(data)
    return (
      <div>
      {data ? (
        <div> 
          <h1 className="text-black px-20 py-40 text-4xl"> {data?.City} </h1>
          <p className="text-black px-20 py-40 text-1xl"> {data?.Ranking} </p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default City;
