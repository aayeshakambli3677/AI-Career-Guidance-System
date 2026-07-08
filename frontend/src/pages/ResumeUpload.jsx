import { useState } from "react";

function ResumeUpload() {

  const [file, setFile] = useState(null);

  return (
    <div>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button>
        Upload Resume
      </button>

    </div>
  );
}

export default ResumeUpload;