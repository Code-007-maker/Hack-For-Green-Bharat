# GreenVision AI — Architecture Diagram Description

This document provides a descriptive breakdown for a technical architecture diagram. This description is intended for the judges to understand the "continuously updating LIVE AI SYSTEM" flow.

## 1. Data Ingestion Layer (Duality AI Source)
- **Component**: Synthetic Offroad Stream Simulator
- **Logic**: Replays high-fidelity synthetic desert frames at 0.5Hz - 1Hz.
- **Data Shape**: `[Batch, 3, 512, 512]` Image Tensors.

## 2. Perception Engine (Inferencing)
- **Model**: SegFormer-B0 (Edge-optimized Transformer).
- **Process**: Performs realtime semantic segmentation on incoming frames.
- **Output**: Multi-class pixel masks (Trees, Rocks, Dry Grass, etc.).

## 3. Real-Time Streaming Backbone (Pathway)
- **Pathway Connector**: Ingests JSON-metadata streams from the perception engine.
- **Reactive Engine**: As soon as a mask is generated, Pathway triggers a `computation graph` update.
- **Windowed Aggregates**: Calculates moving averages of vegetation loss over the last 60 seconds.

## 4. Environmental Intelligence Engine
- **Features**: 
    - `Vegetation health index` computation.
    - `Drought risk estimation` (Dry grass vs Ground ratio).
    - `Soil exposure alerting`.

## 5. Live RAG & Reasoning Layer
- **Pathway Vector Index**: A dynamic index that stores summarized environmental states.
- **Vector Search**: BM25 + Vector embedding search on the *streaming* data.
- **LLM Reasoning**: GPT-4o (or local Mistral) interprets the metrics to provide "Explainable AI" alerts.

## 6. Feedback & Alert Loop
- **Alerts**: Push notifications trigger if `drought_risk > threshold`.
- **Live UI**: Real-time CSV/Websockets sink for the GreenVision dashboard.
