import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import Dashboard from "./components/Dashboard";

function App() {
  const { loginWithRedirect, logout, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      {!isAuthenticated ? (
        <button onClick={() => loginWithRedirect()}>Log In / Sign Up</button>
      ) : (
        <>
          <button onClick={() => logout({ returnTo: window.location.origin })}>Log Out</button>
          <Dashboard />
        </>
      )}
    </div>
  );
}

export default App;