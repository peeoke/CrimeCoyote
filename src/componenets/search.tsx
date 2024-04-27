import React from 'react';

const SearchBar = () => {
  return (
    <div className="search-bar-container">
      <div> 
        <input type="text" placeholder="Where are we going?" className="search-input" />
      </div>
      <div>
        <button type="button" onClick={handleClick} className="search-button">
          Let's Go!
        </button>
      </div>
    </div>
  );
};

const handleClick = () => {
  // implementation details
};


export default SearchBar;
