import React, { useEffect, useState } from 'react';

export interface City {
  Name: string;
}

const City = () => {
  const [data, setData] = useState(null)

    // const getCity = async () => {
    //   try {
    //     const response = await fetch('http://127.0.0.1:5000/result');
    //     if (!response.ok) {
    //       throw new Error('Failed to fetch data');
    //     }
    //     .then

    //     setData(jsonData);
    //   } catch (error) {
    //     console.error('Error fetching data:', error);
    //     return null;
    //   }
    // }


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
      <div className="text-black lowercase">
      {data ? (
        <h1> {data?.City} </h1>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default City;
