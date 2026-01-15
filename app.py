from flask import Flask, jsonify
from reports import generate_report
from distributed_processor import simulate_distributed_processing

app = Flask(__name__)

@app.route("/process-data", methods=["POST"])
def process_data():
    simulate_distributed_processing()
    return jsonify({"status": "Data processed successfully"})

@app.route("/generate-report", methods=["POST"])
def report():
    generate_report()
    return jsonify({"status": "Report generated"})

if __name__ == "__main__":
    app.run(debug=True)
