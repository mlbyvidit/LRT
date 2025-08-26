import React, { useState, useEffect } from "react";
import Upload from "../components/Upload";
import DataTable from "../components/DataTable";
import Charts from "../components/Charts";
import StyledCard from "../components/StyledCard";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

function groupByCitySumVolume(data) {
  const map = {};
  data.forEach(row => {
    if (!row.origin_city) return;
    if (!map[row.origin_city]) map[row.origin_city] = 0;
    map[row.origin_city] += Number(row.volume) || 0;
  });
  return Object.entries(map).map(([origin_city, volume]) => ({ origin_city, volume }));
}

export default function ShippersPage() {
  const [shippers, setShippers] = useState([]);

  const fetchShippers = async () => {
    const res = await axios.get(`${API_URL}/data/shippers`);
    setShippers(res.data.map(({_sa_instance_state, ...rest}) => rest));
  };

  useEffect(() => { fetchShippers(); }, []);

  const chartData = groupByCitySumVolume(shippers);

  return (
    <div className="flex justify-center p-8">
      <StyledCard className="w-[900px]">
        <h2 className="font-bold text-2xl mb-6">Shippers</h2>
        <Upload type="shippers" onUpload={fetchShippers} />
        <DataTable data={shippers} />
        <h3 className="mt-8 font-semibold">Volume by Origin City</h3>
        <Charts data={chartData} dataKey="volume" xKey="origin_city" />
      </StyledCard>
    </div>
  );
} 