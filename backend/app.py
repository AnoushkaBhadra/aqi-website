from flask import Flask, jsonify
from flask_cors import CORS
import traceback
import logging
import sys
import sqlite3
 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)
 
app = Flask(__name__)
CORS(app)
 
@app.route('/predict', methods=['GET'])
def predict():
    try:
        logger.info("Predict endpoint called")
 
        # Import model runner
        import model_runner
        logger.info("model_runner imported successfully")
 
        # Run prediction
        logger.info("Calling predict_from_db")
        # result = model_runner.predict_from_db()
        raw_result = model_runner.predict_from_db()
        result = raw_result["predicted_aqi"] if isinstance(raw_result, dict) else raw_result

        logger.info(f"Prediction result: {result}")
 
        # Get last available AQI from DB
        conn = sqlite3.connect("aqi_data.db")
        cursor = conn.cursor()
 
        cursor.execute("SELECT AQI FROM aqi_readings ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()
 
        current_aqi = row[0] if row else None
        if current_aqi is None:
            logger.warning("Database is empty or AQI is missing")
 
        # Final response
        response = {
            "predicted_aqi": result,
            "current_aqi": current_aqi
            # "predicted_aqi": 54.56,
            # "current_aqi": 34.56
            
        }
        # print(type(result))
 
        return jsonify(response)
 
    except Exception as e:
        error_detail = traceback.format_exc()
        logger.error(f"Error in prediction: {str(e)}\n{error_detail}")
        return jsonify({"error": str(e), "traceback": error_detail}), 500
 

 
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API is running"})
 
if __name__ == '__main__':
    logger.info("Starting Flask app")
    app.run(host='0.0.0.0', port=5000, debug=True)