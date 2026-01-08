export async function generatePlan() {
  const response = await fetch("http://localhost:8000/generate-plan", {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error("Failed to generate plan");
  }

  return response.json();
}
