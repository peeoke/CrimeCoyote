import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const SearchBar = () => {
  const [searchQuery, setSearchQuery] = useState('');

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
  };

  return (
    <div className="search-bar-container">
      <div> 
        <input type="text" placeholder="Where are we going?" value={searchQuery} onChange={handleInputChange} className="search-input" />
      </div>
      <div>
        <button type="button" onClick={handleSearch} className="search-button">
          Let's Go!
        </button>
      </div>
    </div>
  );
};

export default SearchBar;
