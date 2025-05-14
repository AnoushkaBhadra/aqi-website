from flask import Flask, jsonify
from flask_cors import CORS
import traceback
import logging
import sys


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

        import model_runner
        logger.info("model_runner imported successfully")
        
        logger.info("Calling predict_from_db")
        result = model_runner.predict_from_db()
        logger.info(f"Got prediction result: {result}")
        
        return jsonify(result)
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