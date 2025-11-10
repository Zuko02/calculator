import React, { useState } from "react";
import axios from "axios";

const Calculator = () => {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [operation, setOperation] = useState("add");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleCalculate = async () => {
    try {
      const response = await axios.post("http://localhost:8000/calculate/", {
        num1,
        num2,
        operation,
      });
      setResult(response.data.result);
      setError(null);
    } catch (err) {
      setResult(null);
      if (err.response) {
        setError(err.response.data.error);
      } else {
        setError("Server error");
      }
    }
  };

  return (
    <div
      style={{
        border: "1px solid #ccc",
        borderRadius: "8px",
        padding: "20px",
        width: "300px",
        margin: "0 auto",
        boxShadow: "0 0 8px rgba(0,0,0,0.1)",
      }}
    >
      <div style={{ marginBottom: "15px" }}>
        <input
          type="number"
          value={num1}
          onChange={(e) => setNum1(e.target.value)}
          placeholder="Enter first number"
          style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
        />
        <input
          type="number"
          value={num2}
          onChange={(e) => setNum2(e.target.value)}
          placeholder="Enter second number"
          style={{ width: "100%", padding: "8px" }}
        />
      </div>

      <div style={{ marginBottom: "15px" }}>
        <select
          value={operation}
          onChange={(e) => setOperation(e.target.value)}
          style={{ width: "100%", padding: "8px" }}
        >
          <option value="add">Add (+)</option>
          <option value="subtract">Subtract (-)</option>
          <option value="multiply">Multiply (×)</option>
          <option value="divide">Divide (÷)</option>
        </select>
      </div>

      <button
        onClick={handleCalculate}
        style={{
          width: "100%",
          padding: "10px",
          backgroundColor: "#007bff",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Calculate
      </button>

      {result !== null && (
        <h3 style={{ marginTop: "20px" }}>Result: {result}</h3>
      )}

      {error && (
        <p style={{ color: "red", marginTop: "20px" }}>Error: {error}</p>
      )}
    </div>
  );
};

export default Calculator;
