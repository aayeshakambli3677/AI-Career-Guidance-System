import { NavLink } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
    return (
        <div className="sidebar">

            <h2 className="logo">CareerGPT</h2>

            <nav>
                <NavLink to="/dashboard">
                    🏠 Dashboard
                </NavLink>

                <NavLink to="/profile">
                    👤 Profile
                </NavLink>

                <NavLink to="/career">
                    🎯 Career Guidance
                </NavLink>

                <NavLink to="/resume">
                    📄 Resume Analyzer
                </NavLink>

                <NavLink to="/interview">
                    🎤 Mock Interview
                </NavLink>

                <NavLink to="/roadmap">
                    🛣 Career Roadmap
                </NavLink>

                <NavLink to="/skills">
                    💡 Skill Recommendation
                </NavLink>

                <NavLink to="/settings">
                    ⚙ Settings
                </NavLink>

            </nav>

        </div>
    );
}

export default Sidebar;