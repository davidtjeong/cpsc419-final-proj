import React, { useState, useEffect } from "react";

function Favorites() {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    const savedFavorites = JSON.parse(localStorage.getItem("saved")) || [];
    setFavorites(savedFavorites);
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Favorited Listings</h1>
      {favorites.length === 0 ? (
        <p>No favorite listings yet.</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {favorites.map((listing) => (
            <div key={listing.id} className="border p-4 rounded shadow">
              <h2 className="text-lg font-semibold">{listing.title}</h2>
              <p>{listing.description}</p>
              <p className="font-bold">${listing.price}/month</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Favorites;
