import { useState } from "react";
import "../styles/ProgressTracker.css";

function ProgressTracker() {

    const [progress] = useState(65);

    return (
        <div className="progress-page">

            <h1>📈 Progress Tracker</h1>
            <p>Track your learning journey and placement readiness.</p>

            <div className="progress-container">

                {/* Overall Progress */}
                <div className="progress-card">

                    <h2>Overall Progress</h2>

                    <div className="progress-bar">
                        <div
                            className="progress-fill"
                            style={{ width: `${progress}%` }}
                        ></div>
                    </div>

                    <h3>{progress}% Completed</h3>

                </div>

                {/* Progress Cards */}
                <div className="progress-grid">

                    <div className="card">
                        <h3>👤 Profile</h3>
                        <p>✅ Completed</p>
                    </div>

                    <div className="card">
                        <h3>📄 Resume</h3>
                        <p>✅ Uploaded</p>
                    </div>

                    <div className="card">
                        <h3>💡 Skills</h3>
                        <p>70% Completed</p>
                    </div>

                    <div className="card">
                        <h3>🛣️ Roadmap</h3>
                        <p>55% Completed</p>
                    </div>

                    <div className="card">
                        <h3>🎤 Interview</h3>
                        <p>6 / 10 Completed</p>
                    </div>

                    <div className="card">
                        <h3>🏆 Placement Readiness</h3>
                        <p>65% Ready</p>
                    </div>

                </div>

                {/* Next Goals */}
                <div className="goals-card">

                    <h2>🎯 Next Goals</h2>

                    <ul>
                        <li>✔ Complete your Career Roadmap</li>
                        <li>✔ Practice 5 Interview Questions</li>
                        <li>✔ Improve Resume Score above 85%</li>
                        <li>✔ Complete Skill Gap Analysis</li>
                    </ul>

                </div>

                {/* Achievements */}
                <div className="badge-card">

                    <h2>🏅 Achievements</h2>

                    <div className="badge-grid">

                        <div className="badge">
                            <h1>🥇</h1>
                            <h4>Profile Master</h4>
                            <p>Profile Completed</p>
                        </div>

                        <div className="badge">
                            <h1>📄</h1>
                            <h4>Resume Ready</h4>
                            <p>Resume Uploaded</p>
                        </div>

                        <div className="badge">
                            <h1>🎤</h1>
                            <h4>Interview Starter</h4>
                            <p>Practiced 5 Questions</p>
                        </div>

                        <div className="badge">
                            <h1>🚀</h1>
                            <h4>Placement Ready</h4>
                            <p>Reach 80% Progress</p>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    );
}

export default ProgressTracker;