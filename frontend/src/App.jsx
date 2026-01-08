import { useState } from "react";
import { generatePlan } from "./api";

function App() {
  const [loading, setLoading] = useState(false);
  const [plan, setPlan] = useState(null);
  const [error, setError] = useState("");

  const handleGenerate = async () => {
    setLoading(true);
    setError("");

    try {
      const data = await generatePlan();
      setPlan(data);
    } catch (error) {
      console.error("API Error:", error); // 👈 important
      setError("Backend not running or API error");
    } finally {
      setLoading(false); // 👈 always executes
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1> Smart B-Roll Inserter</h1>

      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate B-Roll Plan"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {plan && (
        
        <pre style={{ marginTop: "20px", background: "#f4f4f4", padding: "15px",color:"#000" }}>
          {JSON.stringify(plan, null, 2)}
        </pre>
        
      )}
    </div>
  );
}

export default App;
