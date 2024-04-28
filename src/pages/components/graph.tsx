import React, { useState, useEffect } from 'react';

const ChartComponent = () => {
  const [chartUrl, setChartUrl] = useState('');

  useEffect(() => {
    const fetchChart = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/graph');
        if (!response.ok) {
          throw new Error('Failed to fetch chart');
        }
        const imageUrl = await response.blob();
        setChartUrl(URL.createObjectURL(imageUrl));
      } catch (error) {
        console.error('Error fetching chart:', error);
      }
    };

    fetchChart();
  }, []);

  return (
    <div>
      {chartUrl ? (
        <img src={chartUrl} alt="Chart" />
      ) : (
        <p>Loading chart...</p>
      )}
    </div>
  );
};

export default ChartComponent;