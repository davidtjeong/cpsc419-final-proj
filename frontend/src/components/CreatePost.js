import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './CreatePost.css';

function CreatePost() {
  const navigate = useNavigate();
  const [listing, setListing] = useState({
    street_address: '',
    city: '',
    state: '',
    zip_code: '',
    country: '',
    bedrooms: '',
    bathrooms: '',
    square_footage: '',
    title: '',
    price: '',
    description: '', 
    start_date: '',
    end_date: '',
  });
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setListing({
      ...listing,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Listing Creating: ', listing);
    
    try {
      // Send data to Flask backend API
      const response = await axios.post('http://localhost:5000/api/listings', listing);
      console.log('Listing created:', response.data);
      
      // Reset form after successful submission
      setListing({
        street_address: '',
        city: '',
        state: '',
        zip_code: '',
        country: '',
        bedrooms: '',
        bathrooms: '',
        square_footage: '',
        title: '',
        price: '',
        description: '', 
        start_date: '',
        end_date: '',
      });
      
      // Show success message
      alert('Listing created successfully!');
      navigate('/')
    } catch (error) {
      console.error('Error creating listing:', error);
      alert('Failed to create listing');
    }
  };
  
  return (
    <div className="create-post-container">
      <h1>Create New Listing Post</h1>
      <h2>Thinking about subletting?</h2>
      <p>Fill out the form below to create a new listing post.</p>
      <form onSubmit={handleSubmit} className="create-post-form">
        <div className="form-group">
          <label htmlFor="title">Title</label>
          <input
            type="text"
            id="title"
            name="title"
            value={listing.title}
            onChange={handleInputChange}
            placeholder="Enter listing title"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="street_address">Street Address</label>
          <input
            type="text"
            id="street_address"
            name="street_address"
            value={listing.street_address}
            onChange={handleInputChange}
            placeholder="Enter street address"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="city">City</label>
          <input
            type="text"
            id="city"
            name="city"
            value={listing.city}
            onChange={handleInputChange}
            placeholder="Enter city"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="state">State</label>
          <input
            type="text"
            id="state"
            name="state"
            value={listing.state}
            onChange={handleInputChange}
            placeholder="Enter state"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="zip_code">Zip Code</label>
          <input
            type="text"
            id="zip_code"
            name="zip_code"
            value={listing.zip_code}
            onChange={handleInputChange}
            placeholder="Enter zip code"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="country">Country</label>
          <input
            type="text"
            id="country"
            name="country"
            value={listing.country}
            onChange={handleInputChange}
            placeholder="Enter country"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="bedrooms">Bedrooms</label>
          <input
            type="number"
            id="bedrooms"
            name="bedrooms"
            value={listing.bedrooms}
            onChange={handleInputChange}
            placeholder="Enter number of bedrooms"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="bathrooms">Bathrooms</label>
          <input
            type="number"
            id="bathrooms"
            name="bathrooms"
            value={listing.bathrooms}
            onChange={handleInputChange}
            placeholder="Enter number of bathrooms"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="square_footage">Square Footage</label>
          <input
            type="number"
            id="square_footage"
            name="square_footage"
            value={listing.square_footage}
            onChange={handleInputChange}
            placeholder="Enter square footage"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="price">Price</label>
          <input
            type="number"
            id="price"
            name="price"
            value={listing.price}
            onChange={handleInputChange}
            placeholder="Enter price"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            name="description"
            value={listing.description}
            onChange={handleInputChange}
            placeholder="Enter description"
            rows="4"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="start_date">Start Date</label>
          <input
            type="date"
            id="start_date"
            name="start_date"
            value={listing.start_date}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="end_date">End Date</label>
          <input
            type="date"
            id="end_date"
            name="end_date"
            value={listing.end_date}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="center-button-container">
          <button type="submit" className="submit-button">Create Post</button>
        </div>
      </form>
    </div>
  );
}

export default CreatePost;
