import { useState, useEffect } from "react";
import api from "../api";
import Listing from "../components/Listing"
import getListings from "./Home"

function PostHandling() {
    const [description, setDescription] = useState("");
    const [title, setTitle] = useState("");

    //temp
    //const [listings, setListings] = useState([]);

    const deleteListing = (id) => {
        api
            .delete(`/api/listing/delete/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Deleted the listing");
                else alert("Failed to delete listing.");
                getListings();
            })
            .catch((error) => alert(error));
    };

    const createListing = (e) => {
        e.preventDefault();
        api
            .post("/api/listings/create/", { description, title })
            .then((res) => {
                if (res.status === 201) alert("Listing created!");
                else alert("Failed to make listing.");
                getListings();
            })
            .catch((err) => alert(err));
    };

    return <div>
        <div>
            <h2>Listings</h2>
            {listings.map((listing) => (<Listing listing={listing} key={listing.id} />
            ))}
        </div>

        <h1>Post creation/deletion page</h1>
        <h2>Create a Listing</h2>
        <form onSubmit={createListing}>
            <label htmlFor="title">Title:</label>
            <br />
            <input
                type="text"
                id="title"
                name="title"
                required
                onChange={(e) => setTitle(e.target.value)}
                value={title}
            />
            <label htmlFor="description">Description:</label>
            <br />
            <textarea
                id="description"
                name="description"
                required
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            ></textarea>
            <br />
            <input type="submit" value="Submit"></input>
        </form>
    </div>
}

export default PostHandling