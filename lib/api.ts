return {
  location: "Localhost",
  current: {
    value: result.current_aqi, // or result.predicted_aqi if current is unavailable
    timestamp: new Date().toISOString()
  },
  predicted: {
    value: result.predicted_aqi,
    timestamp: new Date(Date.now() + 60 * 60 * 1000).toISOString() // 1 hour later
  },
  pm25: {
    value: result.pm25 ?? 0
  },
  pm10: {
    value: result.pm10 ?? 0
  }
}
