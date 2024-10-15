import testImage from '../assets/test.jpg';

function Profile() {
    return <div>
        <h1>Profile page</h1>
        <p>You are logged in</p>
        <img src={testImage} alt="The man himself" />
    </div>
}

export default Profile