import React, { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import RoleAssignment from "./RoleAssignment";

const API_URL = "http://localhost:8000";

function Dashboard() {
  const { getAccessTokenSilently, user } = useAuth0();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      const token = await getAccessTokenSilently();
      const res = await fetch(`${API_URL}/auth/verify-token`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await res.json();
      setProfile(data);
    };
    fetchProfile();
  }, [getAccessTokenSilently]);

  if (!profile) return <div>Loading profile...</div>;

  return (
    <div>
      <h2>Welcome, {profile.first_name} {profile.last_name}</h2>
      <p>Email: {profile.email}</p>
      <p>Status: {profile.status}</p>
      {/* Add more profile info as needed */}
      <RoleAssignment userId={profile.id} />
    </div>
  );
}

export default Dashboard;