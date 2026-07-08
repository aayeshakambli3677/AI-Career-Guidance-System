import { NavLink } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
    return (
        <div className="sidebar">

            <h2 className="logo">CareerGPT</h2>

            <nav>
                <nav>
                    <ul className="sidebar-menu">
                        <li>
                            <NavLink to="/dashboard">🏠 Dashboard</NavLink>
                        </li>

                        <li>
                            <NavLink to="/profile">👤 Profile</NavLink>
                        </li>

                        <li>
                            <NavLink to="/career">🎯 Career Guidance</NavLink>
                        </li>

                        <li>
                            <NavLink to="/resume">📄 Resume Analyzer</NavLink>
                        </li>

                        <li>
                            <NavLink to="/interviewPreparation">🎤 Mock Interview</NavLink>
                        </li>

                        <li>
                            <NavLink to="/roadmap">🛣 Career Roadmap</NavLink>
                        </li>

                        <li>
                            <NavLink to="/skills">💡 Skill Recommendation</NavLink>
                        </li>

                        <li>
                            <NavLink to="/settings">⚙ Settings</NavLink>
                        </li>
                    </ul>
                </nav>

            </nav>

        </div>
    );
}

export default Sidebar;