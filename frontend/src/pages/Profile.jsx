import "./Profile.css";
import { useNavigate } from "react-router-dom";

function Profile() {

    const navigate = useNavigate();

    const profile =
        JSON.parse(localStorage.getItem("profile"));

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

                    <h2>
                        {profile?.full_name || "Student Name"}
                    </h2>

                    <p>
                        Email: {profile?.email || "student@gmail.com"}
                    </p>

                    <p>
                        Education: {profile?.education || "Computer Engineering"}
                    </p>

                    <p>
                        Skills: {profile?.skills || "React, Python, FastAPI"}
                    </p>

                    <p>
                        Career Goal: {profile?.career_goal || "Software Developer"}
                    </p>

                    <button
                        onClick={() => navigate("/edit-profile")}
                    >
                        Edit Profile
                    </button>

                </div>

            </div>

        </div>
    );
}

export default Profile;