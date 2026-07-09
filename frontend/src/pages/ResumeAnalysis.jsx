import { useState } from "react";
import "../styles/ResumeAnalysis.css";
import { uploadResume, analyzeResume } from "../services/resumeService";

function ResumeAnalysis() {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState("");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setError("");
        setResult(null);
    };

    const handleAnalyze = async () => {
        if (!file) {
            setError("Please select a resume first.");
            return;
        }

        try {
            setLoading(true);
            setError("");

            // Upload resume
            const uploadResponse = await uploadResume(file);

            // Get resume ID from backend response
            const resumeId =
                uploadResponse.resumeId ||
                uploadResponse.resume_id ||
                uploadResponse.id;

            if (!resumeId) {
                throw new Error("Resume ID not received from server.");
            }

            // Analyze resume
            const analysis = await analyzeResume(resumeId);

            setResult(analysis);
        } catch (err) {
            console.error(err);
            setError("Failed to analyze resume. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="resume-page">
            <h1 style={{ color: "black", fontSize: "50px" }}>
                THIS IS MY RESUME PAGE 📄
            </h1>

            <p>
                Upload your resume and get AI-based feedback to improve your profile.
            </p>

            <div className="resume-box">
                <h2>Upload Resume</h2>

                <input
                    type="file"
                    accept=".pdf,.doc,.docx"
                    onChange={handleFileChange}
                />

                {file && (
                    <p className="selected-file">
                        <strong>Selected File:</strong> {file.name}
                    </p>
                )}

                <button onClick={handleAnalyze} disabled={loading}>
                    {loading ? "Analyzing..." : "Analyze Resume"}
                </button>

                {error && <p className="error-message">{error}</p>}

                {result && (
                    <div className="result-box">
                        <h2>Analysis Result</h2>

                        <pre>{JSON.stringify(result, null, 2)}</pre>
                    </div>
                )}
            </div>
        </div>
    );
}

export default ResumeAnalysis;