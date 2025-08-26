import React, { useEffect, useState } from "react";
import StyledCard from "../components/StyledCard";
import axios from "axios"; // Import axios

export default function Dashboard() {
  const dashboardId = "45a55726-d11c-477a-8773-a2eb15ec407e";
  const supersetHost = "http://localhost:8089";
  const backendApiUrl = "http://localhost:8002"; // Your backend API URL

  const [guestToken, setGuestToken] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchGuestToken = async () => {
      try {
        setLoading(true);
        const response = await axios.post(
          `${backendApiUrl}/superset/guest_token`,
          { dashboard_id: dashboardId }
        );
        setGuestToken(response.data.guest_token);
      } catch (err) {
        setError("Failed to fetch Superset guest token.");
        console.error("Error fetching guest token:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchGuestToken();
  }, [dashboardId, backendApiUrl]);

  if (loading) {
    return (
      <div className="flex justify-center p-8 w-full h-screen">
        <StyledCard className="w-full flex flex-col items-center overflow-hidden">
          <div className="text-gray-400">Loading Superset Dashboard...</div>
        </StyledCard>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center p-8 w-full h-screen">
        <StyledCard className="w-full flex flex-col items-center overflow-hidden">
          <div className="text-red-500">{error}</div>
        </StyledCard>
      </div>
    );
  }

  // Construct the embed URL with the guest token
  const embedUrl = `${supersetHost}/superset/dashboard/p/${dashboardId}/?standalone=true&guest_token=${guestToken}`;

  return (
    <div className="flex justify-center p-8 w-full h-screen">
      <StyledCard className="w-full flex flex-col items-center overflow-hidden">
        <iframe
          src={embedUrl}
          width="100%"
          height="100%"
          frameBorder="0"
          title="Superset Dashboard"
          allow="fullscreen" // Allow fullscreen for the iframe
        ></iframe>
      </StyledCard>
    </div>
  );
}
