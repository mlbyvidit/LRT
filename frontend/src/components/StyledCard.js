import React from "react";

export default function StyledCard({ children, className = "", style }) {
  return (
    <div
      className={`bg-card rounded-2xl shadow-xl p-8 m-4 ${className}`}
      style={style}
    >
      {children}
    </div>
  );
} 