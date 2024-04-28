import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SearchBar = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchQuery(event.target.value);
  };

  const handleSearch = () => {
    fetch('http://127.0.0.1:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query: searchQuery}),
    })
    navigate("/city-stats");
  };

  return (
    <div className="flex justify-center items-center h-screen gap-4">
      <div> 
        <input type="text" placeholder="Where are we going?" value={searchQuery} onChange={handleInputChange} className="bg-grey-300 p-4 rounded-lg" />
      </div>
      <br />
      <div>
          <button type="button" onClick={handleSearch} className="bg-black text-white p-6 rounded items-center">
            Let's Go!
          </button>
      </div>
    </div>
  );
};

export default SearchBar;
