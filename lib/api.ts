import type { AqiData } from "./types"

export async function fetchAqiData(): Promise<AqiData> {
try {
  // Uncomment this block once your backend provides the actual API endpoint
  /*
  const response = await fetch("https://your-backend-url.com/api/aqi");
  if (!response.ok) {
  throw new Error("Failed to fetch AQI from live API");
  }
  const data = await response.json();

  return {
    location: data.location || "Unknown",
    current: {
      value: data.aqi,
      timestamp: data.timestamp || new Date().toISOString(),
    },
    // Don't need these anymore~
    pm25: { value: 0 },
    pm10: { value: 0 },
  };
  */
  // Fallback logic (simulates API response)
    return await new Promise((resolve, reject) => {
      setTimeout(() => {
        // Simulate failure ~30% of the time
        if (Math.random() < 0.3) {
          reject(new Error("Simulated API failure (fallback triggered)"));
          return;
        }

        const currentValue = Math.floor(Math.random() * 300);

        resolve({
          location: "Kolkata, WB",
          current: {
            value: currentValue,
            timestamp: new Date().toISOString(),
          },
          pm25: { value: 0 },
          pm10: { value: 0 },
        });
      }, 1500);
    });
    } catch (error) {
    console.error("API fetch failed, using fallback:", error);
    const currentValue = Math.floor(Math.random() * 300);

    return {
      location: "Kolkata, WB (Fallback)",
      current: {
        value: currentValue,
        timestamp: new Date().toISOString(),
      },
      pm25: { value: 0 },
      pm10: { value: 0 },
    };
  }
}
