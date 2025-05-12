import type { AqiData } from "./types"

export const dummyAqiData: AqiData = {
  location: "San Francisco, CA (Fallback)",
  current: {
    value: 42,
    timestamp: new Date().toISOString(),
  },
  pm25: {
    value: 12,
  },
  pm10: {
    value: 25,
  },
}
