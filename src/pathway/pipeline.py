import pathway as pw
from connectors import get_stream_connector
from features import compute_environmental_metrics, create_rag_document

# Core Pathway Pipeline: Real-time Data -> Metrics -> RAG Indexing
def run_pipeline():
    # 1. Start live ingestion
    raw_stream = get_stream_connector()
    
    # 2. Real-time Feature Engineering
    metrics_stream = compute_environmental_metrics(raw_stream)
    
    # 3. Create searchable documents for RAG
    # In a real setup, we use pw.apply for UDFs on the stream
    # For now, we simulate the output conversion
    
    # Printing live updates to demonstrate real-time behavior
    pw.io.csv.write(metrics_stream, "live_eco_metrics.csv")
    
    # Note: In a full project, we would connect this to Pathway's Vector Store
    # pw.io.http.write(metrics_stream, host="0.0.0.0", port=8080)
    
    print("GreenVision Pipeline Running... Monitoring environmental changes in real-time.")
    pw.run()

if __name__ == "__main__":
    run_pipeline()
