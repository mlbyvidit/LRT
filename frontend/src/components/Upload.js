import React, { useState } from "react";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export default function Upload({ type, onUpload }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post(
      `${API_URL}/upload/${type}`,
      formData,
      { headers: { "Content-Type": "multipart/form-data" } }
    );
    onUpload();
  };

  return (
    <div>
      <input type="file" accept=".csv" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={!file}>Upload {type}</button>
    </div>
  );
} 