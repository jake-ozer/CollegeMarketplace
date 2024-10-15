import React from "react";

function Listing({listing}) {
    const formattedDate = new Date(listing.created_at).toLocaleDateString("en-US")

    return (
        <div className="listing-container">
            <h2 className="listing-title">{listing.title}</h2>
            <p className="listing-content">{listing.content}</p>
            <p className="listing-date">{formattedDate}</p>
        </div>
    );
}
/*
<button className="delete-button" onClick={() => onDelete(listing.id)}>
                Delete
            </button>
*/
export default Listing
