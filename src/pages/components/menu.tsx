import React, { useState } from 'react';

const Menu = () => {
  return (
    <div className="bg-sage-green text-white absolute top-10 right-10 w-full">
      <ul className="list-none m-0 text-right gap-4">
        <li className="inline-block mr-20"><a href="/" className="text-white hover:text-gray-300">Home</a></li>
        <li className="inline-block mr-20"><a href="/about" className="text-white hover:text-gray-300">About</a></li>
        <li className="inline-block mr-20"><a href="http://127.0.0.1:5001/" className="text-white hover:text-gray-300">Chat</a></li>
      </ul>
    </div>
  );
};

export default Menu;
