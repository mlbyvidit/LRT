import React from "react";
import { Link, useLocation } from "react-router-dom";

const navLinks = [
  { to: "/carriers", label: "Carrier Home" },
  { to: "/shippers", label: "Shipper Home" },
  { to: "/geo", label: "Geo Data" },
];

export default function SideNav() {
  const location = useLocation();
  return (
    <aside className="fixed left-0 top-0 h-screen w-64 bg-dark flex flex-col items-center py-8 shadow-lg z-20">
      <div className="mb-12">
        <img src="/logo.png" alt="LRT Logo" className="h-16" />
      </div>
      <nav className="flex flex-col gap-y-8 w-full px-6">
        {navLinks.map(link => (
          <Link
            key={link.to}
            to={link.to}
            className={`font-semibold text-lg py-2 px-4 rounded transition-colors duration-200 text-center ${
              location.pathname === link.to
                ? "text-accent bg-card"
                : "text-white hover:text-accent hover:bg-card"
            }`}
          >
            {link.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}