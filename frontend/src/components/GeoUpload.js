import React, { useState } from "react";
import axios from "axios";

export default function GeoUpload({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post(`${process.env.REACT_APP_API_URL || "http://localhost:8000"}/upload/geo`, formData, {
      headers: { "Content-Type": "multipart/form-data" }
    });
    onUpload();
  };

  return (
    <div className="flex items-center gap-4 my-4">
      <input
        type="file"
        accept=".csv"
        onChange={e => setFile(e.target.files[0])}
        className="block w-full text-sm text-gray-300 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-accent file:text-dark hover:file:bg-green-300"
      />
      <button
        onClick={handleUpload}
        disabled={!file}
        className="bg-accent text-dark font-bold px-6 py-2 rounded-lg shadow hover:bg-green-400 transition"
      >
        Upload
      </button>
    </div>
  );
} 