import React from "react";
import StyledCard from "../components/StyledCard";

export default function Dashboard() {
  // Direct embed without guest token - using your deployed Superset service
  const supersetHost = "https://superset-web-9bo9.onrender.com";
  
  // Dashboard UUID from the new dashboard export
  const dashboardUuid = "59c44a63-edb6-4b5f-be99-da4c6333d037";
  
  // Direct embed URL for the Superset dashboard using UUID
  const embedUrl = `${supersetHost}/superset/dashboard/${dashboardUuid}/?standalone=true`;

  return (
    <div className="flex justify-center p-8 w-full h-screen">
      <StyledCard className="w-full flex flex-col items-center overflow-hidden">
        <div className="w-full h-full">
          <iframe
            src={embedUrl}
            width="100%"
            height="100%"
            frameBorder="0"
            title="Superset Dashboard"
            allow="fullscreen"
          ></iframe>
        </div>
      </StyledCard>
    </div>
  );
}
