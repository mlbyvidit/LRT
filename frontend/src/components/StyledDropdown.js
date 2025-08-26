import React from "react";

export default function StyledDropdown({ options, value, onChange, label }) {
  return (
    <div className="mb-6">
      {label && <div className="mb-2 font-semibold text-base">{label}</div>}
      <select
        value={value}
        onChange={onChange}
        className="w-full py-3 px-3 rounded-lg bg-dark text-white text-base shadow focus:outline-none mb-2"
      >
        {options.map(opt => (
          <option key={opt.value} value={opt.value}>{opt.label}</option>
        ))}
      </select>
    </div>
  );
} 