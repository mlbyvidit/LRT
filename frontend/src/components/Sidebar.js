import React, { useState } from "react";
import StyledCard from "./StyledCard";
import StyledDropdown from "./StyledDropdown";
import StyledButton from "./StyledButton";

const stateOptions = [
  { value: "all", label: "All" },
  { value: "GA", label: "Georgia" },
  { value: "TX", label: "Texas" },
  { value: "MO", label: "Missouri" },
  { value: "IL", label: "Illinois" },
];
const carrierTypeOptions = [
  { value: "all", label: "All" },
  { value: "type1", label: "Type 1" },
  { value: "type2", label: "Type 2" },
];
const shipperTypeOptions = [
  { value: "all", label: "All" },
  { value: "type1", label: "Type 1" },
  { value: "type2", label: "Type 2" },
];

export default function Sidebar({ onApply }) {
  const [state, setState] = useState("all");
  const [carrierType, setCarrierType] = useState("all");
  const [shipperType, setShipperType] = useState("all");

  return (
    <StyledCard className="min-w-[320px] max-w-xs">
      <div className="text-2xl font-bold mb-6">Filter Options</div>
      <StyledDropdown
        label="> Select State"
        options={stateOptions}
        value={state}
        onChange={e => setState(e.target.value)}
      />
      <StyledDropdown
        label="> Carrier Type"
        options={carrierTypeOptions}
        value={carrierType}
        onChange={e => setCarrierType(e.target.value)}
      />
      <StyledDropdown
        label="> Shipper Type"
        options={shipperTypeOptions}
        value={shipperType}
        onChange={e => setShipperType(e.target.value)}
      />
      <StyledButton onClick={() => onApply({ state, carrierType, shipperType })}>
        Apply Filters
      </StyledButton>
    </StyledCard>
  );
} 