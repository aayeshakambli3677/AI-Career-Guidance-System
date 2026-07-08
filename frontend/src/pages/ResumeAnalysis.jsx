import "../styles/ResumeAnalysis.css";

function ResumeAnalysis() {
    return (
        <div className="resume-page">

            <h1>Resume Analyzer</h1>

            <p>
                Upload your resume and get AI-based feedback to improve your profile.
            </p>

            <div className="resume-box">

                <h2>Upload Resume</h2>

                <input type="file" />

                <button>
                    Analyze Resume
                </button>

            </div>

        </div>
    );
}

export default ResumeAnalysis;