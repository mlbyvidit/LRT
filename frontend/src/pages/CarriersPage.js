import React, { useState, useEffect } from "react";
import Upload from "../components/Upload";
import DataTable from "../components/DataTable";
import Charts from "../components/Charts";
import StyledCard from "../components/StyledCard";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

function groupByCitySumCapacity(data) {
  const map = {};
  data.forEach(row => {
    if (!row.origin_city) return;
    if (!map[row.origin_city]) map[row.origin_city] = 0;
    map[row.origin_city] += Number(row.capacity) || 0;
  });
  return Object.entries(map).map(([origin_city, capacity]) => ({ origin_city, capacity }));
}

export default function CarriersPage() {
  const [carriers, setCarriers] = useState([]);

  const fetchCarriers = async () => {
    const res = await axios.get(`${API_URL}/data/carriers`);
    setCarriers(res.data.map(({_sa_instance_state, ...rest}) => rest));
  };

  useEffect(() => { fetchCarriers(); }, []);

  const chartData = groupByCitySumCapacity(carriers);

  return (
    <div className="flex justify-center p-8">
      <StyledCard className="w-[900px]">
        <h2 className="font-bold text-2xl mb-6">Carriers</h2>
        <Upload type="carriers" onUpload={fetchCarriers} />
        <DataTable data={carriers} />
        <h3 className="mt-8 font-semibold">Capacity by Origin City</h3>
        <Charts data={chartData} dataKey="capacity" xKey="origin_city" />
      </StyledCard>
    </div>
  );
} 