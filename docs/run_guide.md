# GreenVision AI — Final Execution Guide

Because GreenVision AI uses two cutting-edge technologies with different OS affinities, follow this dual-path guide.

## Part 1: Perception Engine (Windows)
*Already verified on your machine!*

1.  **Run the ML Training Simulation**:
    ```powershell
    python d:\projects\test\src\ml\train.py
    ```
2.  **Run the ML Evaluation**:
    ```powershell
    python d:\projects\test\src\ml\test.py
    ```
    *Result: This generates `greenvision_model.pth` and confirms IoU accuracy.*

---

## Part 2: Environmental Intelligence (WSL2 / Ubuntu)
*This is where the Pathway Framework lives.*

1.  **Open your Ubuntu Terminal** (Search 'Ubuntu' in Windows Start).
2.  **Navigate to the project folder**:
    ```bash
    cd /mnt/d/projects/test
    ```
3.  **Install project dependencies**:
    ```bash
    pip3 install pathway torch transformers numpy openai
    ```
4.  **Run the Real-Time Streaming Pipeline**:
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)/src/ml:$(pwd)/src/pathway
    python3 src/pathway/pipeline.py
    ```
5.  **Test the RAG Assistant** (In a new Ubuntu tab):
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)/src/ml:$(pwd)/src/pathway
    python3 src/pathway/rag_assistant.py
    ```

---

## Technical Summary for Judges
- **Real-Time Simulation**: We use a custom generator in `connectors.py` to simulate live robot telemetry.
- **Reactive Features**: Pathway transforms pixel data into "Drought Risk" and "Vegetation Index" within milliseconds.
- **Explainable AI**: The RAG assistant uses the *live* index to explain environmental changes (e.g., "The alert was triggered because dry grass increased by 12%").
