import pathway as pw
import openai
import os

# RAG Assistant: Connecting Live Pathway Metrics to an LLM
# This allows real-time natural language reasoning over a changing ecosystem.

class GreenVisionRAG:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def query_live_data(self, user_query, current_metrics):
        """
        Simulates querying the live Pathway vector index.
        In a full setup, this uses pw.io.http.wait_for_request() or similar.
        """
        
        # In production, current_metrics would be retrieved from the nearest 
        # neighbors in Pathway's live vector store.
        context = f"""
        LIVE ENVIRONMENTAL DATA:
        - Timestamp: {current_metrics.get('timestamp')}
        - Vegetation Index: {current_metrics.get('vegetation_index', 0):.2%}
        - Drought Risk: {current_metrics.get('drought_risk', 0):.2%}
        - Rock Density: {current_metrics.get('rock_density', 0):.2%}
        - Status: {current_metrics.get('eco_alert', 'UNKNOWN')}
        """

        prompt = f"""
        You are GreenVision AI, an environmental monitoring assistant.
        Base your answer ONLY on the live data provided below.
        
        Live Context:
        {context}
        
        User Question: {user_query}
        
        Helpful Response:
        """
        
        try:
            # Mock LLM response for demonstration
            # In real hackathon, this would be a actual OpenAI/Mistral call
            response = f"Based on the live telemetry from {current_metrics.get('timestamp')}, " \
                       f"the area shows a drought risk of {current_metrics.get('drought_risk', 0):.2%}. " \
                       "Vegetation levels are stable. I recommend re-checking after the next stream update."
            return response
        except Exception as e:
            return f"Error connecting to LLM: {str(e)}"

if __name__ == "__main__":
    # Demo test
    assistant = GreenVisionRAG(api_key="mock_key")
    sample_metrics = {
        "timestamp": "2024-03-24T12:00:00",
        "vegetation_index": 0.12,
        "drought_risk": 0.72,
        "eco_alert": "HIGH_RISK_DROUGHT"
    }
    print(assistant.query_live_data("What is the current risk level?", sample_metrics))
