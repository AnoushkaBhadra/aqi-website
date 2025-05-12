import type { AqiData } from "./types"

// This function would be replaced with your actual API call
export async function fetchAqiData(): Promise<AqiData> {
  // Simulating API call with a delay
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Simulate API failure 30% of the time to demonstrate fallback
      if (Math.random() < 0.3) {
        reject(new Error("API connection failed"))
        return
      }

      // Generate random AQI values for demonstration
      const currentValue = Math.floor(Math.random() * 300)
      const pm25Value = Math.floor(Math.random() * 150)
      const pm10Value = Math.floor(Math.random() * 200)

      resolve({
        location: "Kolkata, WB",
        current: {
          value: currentValue,
          timestamp: new Date().toISOString(),
        },
        pm25: {
          value: pm25Value,
        },
        pm10: {
          value: pm10Value,
        },
      })
    }, 1500) // Simulate network delay
  })
}
