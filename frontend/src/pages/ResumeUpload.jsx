import { useState } from "react";
import { uploadResume } from "../services/resumeService";

function ResumeUpload() {

  const [file, setFile] = useState(null);

  const handleUpload = async () => {

    if (!file) {
      alert("Select a file first");
      return;
    }

    try {

      const result =
        await uploadResume(file);

      console.log(result);

      alert("Resume Uploaded");

    } catch(error) {
      console.error(error);
    }
  };

  return (
    <div>

      <h1>Resume Upload</h1>

      <input
  type="file"
  accept=".pdf,.doc,.docx"
        onChange={(e)=>
          setFile(e.target.files[0])
        }
      />

      <button onClick={handleUpload}>
        Upload Resume
      </button>

      {file && (
  <p>
    Selected:
    {file.name}
  </p>
)}

    </div>
  );
}

export default ResumeUpload;