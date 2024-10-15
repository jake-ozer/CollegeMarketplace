import React from 'react';
import Listing from "./Listing";
// A function that returns a listing feed
function ListingFeed({ listings }) {
  return (
    <div className="listing-feed">
      {listings.map((listing, index) => (
        <Listing key={index} listing={listing} />
      ))}
    </div>
  );
}

export default ListingFeed;