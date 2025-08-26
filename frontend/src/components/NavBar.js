import React from "react";
import { Link, useLocation } from "react-router-dom";

const navLinks = [
  { to: "/", label: "Dashboard" },
  { to: "/carriers", label: "Carrier Home" },
  { to: "/shippers", label: "Shipper Home" },
];

export default function NavBar() {
  const location = useLocation();
  return (
    <nav className="w-full flex items-center justify-between bg-dark px-8 h-20 shadow-lg">
      <div className="flex items-center">
        <img src="/logo.png" alt="LRT Logo" className="h-12" />
      </div>
      <div className="flex flex-row gap-x-10">
        {navLinks.map(link => (
          <Link
            key={link.to}
            to={link.to}
            className={`font-semibold text-lg py-2 border-b-2 transition-colors duration-200 ${
              location.pathname === link.to
                ? "text-accent border-accent"
                : "text-white border-transparent hover:text-accent hover:border-accent"
            }`}
          >
            {link.label}
          </Link>
        ))}
      </div>
    </nav>
  );
} 