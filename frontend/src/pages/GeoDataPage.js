import React, { useState, useEffect } from "react";
import GeoUpload from "../components/GeoUpload";
import DataTable from "../components/DataTable";
import axios from "axios";
import StyledCard from "../components/StyledCard";

export default function GeoDataPage() {
  const [geoData, setGeoData] = useState([]);

  const fetchGeoData = async () => {
    const res = await axios.get(`${process.env.REACT_APP_API_URL || "http://localhost:8000"}/data/geo`);
    setGeoData(res.data);
  };

  useEffect(() => { fetchGeoData(); }, []);

  return (
    <div className="flex justify-center p-8">
      <StyledCard className="w-full max-w-[1200px]">
        <h2 className="font-bold text-2xl mb-6">Geographic Data</h2>
        <GeoUpload onUpload={fetchGeoData} />
        <DataTable data={geoData} />
      </StyledCard>
    </div>
  );
} 