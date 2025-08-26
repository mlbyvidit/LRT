import React from "react";

export default function StyledButton({ children, className = "", ...props }) {
  return (
    <button
      className={`bg-accent text-dark font-bold text-lg w-full mt-4 py-3 rounded-lg shadow-md transition-colors duration-200 hover:bg-green-400 focus:outline-none ${className}`}
      {...props}
    >
      {children}
    </button>
  );
} 