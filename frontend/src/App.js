
import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { Auth0Provider, useAuth0 } from "@auth0/auth0-react";
import SideNav from "./components/SideNav";
import Dashboard from "./pages/Dashboard";
import CarriersPage from "./pages/CarriersPage";
import ShippersPage from "./pages/ShippersPage";
import GeoDataPage from "./pages/GeoDataPage";

// Login/Logout buttons
const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();
  return (
    <button
      onClick={() => loginWithRedirect()}
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Log In
    </button>
  );
};

const LogoutButton = () => {
  const { logout } = useAuth0();
  return (
    <button
      onClick={() => logout({ returnTo: window.location.origin })}
      className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
    >
      Log Out
    </button>
  );
};

function AppContent() {
  const { isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-dark text-white">
        Loading authentication...
      </div>
    );
  }

  if (!isAuthenticated) {
    return (
      <div className="flex flex-col justify-center items-center min-h-screen bg-dark text-white p-4">
        <h2 className="text-3xl font-bold mb-6">
          Please log in to access the application.
        </h2>
        <LoginButton />
      </div>
    );
  }

  return (
    <>
      <SideNav />
      <div className="flex-grow flex flex-col items-center ml-64 bg-dark min-h-screen">
        {/* Logout button at the top right */}
        <div className="w-full flex justify-end p-4">
          <LogoutButton />
        </div>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/carriers" element={<CarriersPage />} />
          <Route path="/shippers" element={<ShippersPage />} />
          <Route path="/geo" element={<GeoDataPage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </>
  );
}

function App() {
  return (
    <Auth0Provider
      domain={process.env.REACT_APP_AUTH0_DOMAIN}
      clientId={process.env.REACT_APP_AUTH0_CLIENT_ID}
      authorizationParams={{
        redirect_uri: window.location.origin,
        audience: process.env.REACT_APP_AUTH0_AUDIENCE,
      }}
    >
      <Router>
        <AppContent />
      </Router>
    </Auth0Provider>
  );
}

export default App;
