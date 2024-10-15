import { useState, useEffect } from "react";
import api from "../api";
import ListingFeed from "../components/ListingFeed"

function Home() {
    const [listings, setListings] = useState([]);

    useEffect(() => {
        getListings();
    }, []);

    const getListings = () => {
        api
            .get("/api/listings/")
            .then((response) => response.data)
            .then((data) => {
                setListings(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                <h2>Listings</h2>
                <ListingFeed listings={listings} />
            </div>
            
        </div>
    );
}

export default Home;
