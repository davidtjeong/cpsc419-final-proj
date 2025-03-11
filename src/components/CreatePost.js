import React, { useState } from "react";
import './CreatePost.css';

function CreatePost() {
	const [listing, setListing] = useState({
	  title: '',
	  location: '',
	  price: '',
	  description: '',
	  startDate: '',
	  endDate: '',
	  apartmentId: '',
});
  
const handleInputChange = (e) => {
	const { name, value } = e.target;
	setListing({
	...listing,
	[name]: value,
	});
};

const handleSubmit = (e) => {
	e.preventDefault();
	console.log('Listing Creating: ', listing);
}
  

return (
    <div className="create-post-container">
      <h1>Create New Listing Post</h1>
	  <h2> Thinking about subletting? </h2>
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
          <label htmlFor="location">Location</label>
          <input
            type="text"
            id="location"
            name="location"
            value={listing.location}
            onChange={handleInputChange}
            placeholder="Enter location"
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
          <label htmlFor="startDate">Start Date</label>
          <input
            type="date"
            id="startDate"
            name="startDate"
            value={listing.startDate}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="endDate">End Date</label>
          <input
            type="date"
            id="endDate"
            name="endDate"
            value={listing.endDate}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="apartmentId">Apartment ID</label>
          <input
            type="text"
            id="apartmentId"
            name="apartmentId"
            value={listing.apartmentId}
            onChange={handleInputChange}
            placeholder="Enter apartment ID"
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
