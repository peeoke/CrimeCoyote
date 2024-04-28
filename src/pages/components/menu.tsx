import React, { useState } from 'react';

const Menu = () => {
  return (
    <div className="menu">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/chat">Chat</a></li>
      </ul>
    </div>
  );
};

export default Menu;
