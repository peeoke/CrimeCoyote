import React, { useEffect, useState } from 'react';

const City = () => {
    const [data, setData] = useState(null);

    const getCity = () => {
        fetch('http://127.0.0.1:5000/result')
            .then(response => response.json())
            .then(data => {
                setData(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
      });
    }

    useEffect(() => {
        getCity(); // Call getCity function on mount
      }, []);
  
    return (
    <div className="city">
        
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default City;
