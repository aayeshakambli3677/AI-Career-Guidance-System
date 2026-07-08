
import "./Profile.css";
function Profile() {
    return (
        <div className="profile-page">

            <h1>My Profile</h1>

            <div className="profile-card">

                <div className="profile-image">
                    <img
                        src="/profile.png"
                        alt="Profile"
                    />
                </div>

                <div className="profile-details">

                    <h2>Student Name</h2>

                    <p>Email: student@gmail.com</p>

                    <p>Education: Computer Engineering</p>

                    <p>Skills: React, Python, FastAPI</p>

                    <p>Career Goal: Software Developer</p>

                    <button>Edit Profile</button>

                </div>

            </div>

        </div>
    );
}

export default Profile;