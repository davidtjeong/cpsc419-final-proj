import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from 'axios'

function Home() {
  const [search, setSearch] = useState({
    location: "",
    minPrice: "",
    maxPrice: "",
  });
  const [listings, setListings] = useState([]);
  const [filteredListings, setFilteredListings] = useState([]);
  const [loading, setLoading] = useState(true);

  // simulates fetching listings from  backend
  useEffect(() => {
    // Example listings REPLAACE LATER
    const fetchedListings = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://localhost:5000/api/listings?limit=4');

        const formattedListings = response.data.map(listing => ({
          id: listing.listing_id,
          title: listing.title,
          price: listing.price,
          location: `${listing.city}, ${listing.state}`,
        }));
        
        setListings(formattedListings);
        setFilteredListings(formattedListings);
      } catch (error) {
        console.error('Error fetching listings:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchedListings();
  }, []);

  const handleSearchChange = (e) => {
    setSearch({
      ...search,
      [e.target.name]: e.target.value,
    });
  };

  const handleSearch = () => {
    const filtered = listings.filter((listing) => {
      return (
        (search.location === "" ||
          listing.location.toLowerCase().includes(search.location.toLowerCase())) &&
        (search.minPrice === "" || listing.price >= parseInt(search.minPrice)) &&
        (search.maxPrice === "" || listing.price <= parseInt(search.maxPrice))
      );
    });
    setFilteredListings(filtered);
  };

  return (
    <div className="home-container">
      <h1 className="title">Yale Sublet</h1>
	  <h2 className="subtitle">Search below to get started:</h2>
      <div className="search-box">
        <input
          type="text"
          name="location"
          value={search.location}
          placeholder="Search by location"
          onChange={handleSearchChange}
          className="search-input"
        />
        <input
          type="number"
          name="minPrice"
          value={search.minPrice}
          placeholder="Search by Minimum Price"
          onChange={handleSearchChange}
          className="search-input"
        />
        <input
          type="number"
          name="maxPrice"
          value={search.maxPrice}
          placeholder="Search by Maximum Price"
          onChange={handleSearchChange}
          className="search-input"
        />
        <button onClick={handleSearch} className="search-button">
          Search
        </button>
      </div>

      <div className="listing-container">
        <h2>Listings</h2>
        {loading ? (
          <p>Loading listings...</p>
        ) : (
          <div className="listing-layout">
            {filteredListings.map((listing) => (
              <div key={listing.id} className="listing-item">
                <h3>{listing.title}</h3>
                <p>Location: {listing.location}</p>
                <p>Price: ${listing.price}</p>
                <Link to={`/item/${listing.id}`} className="view-details-link">
                  View Details
                </Link>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="create-post-button">
        <Link to="/create-post">
          <button className="create-button">Create New Listing</button>
        </Link>
      </div>
    </div>
  );
}

export default Home;
