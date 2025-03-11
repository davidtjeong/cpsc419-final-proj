import React from 'react';
import { useParams } from 'react-router-dom';

function ListItem() {
  const { id } = useParams(); 

  return (
    <div>
      <h2>Details for Item {id}</h2>
      <p>Post: {id}.</p>
    </div>
  );
}

export default ListItem;
