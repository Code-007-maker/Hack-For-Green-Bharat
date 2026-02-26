# GreenVision AI — Real-Time Environmental Intelligence

**First Prize Submission for "Hack For Green Bharat" National Hackathon**

## 🌍 Overview
GreenVision AI is a production-grade environmental monitoring platform that transforms semantic segmentation outputs from offroad sensors into **real-time environmental intelligence**. It detects desertification, vegetation loss, and ecological risks as they happen.

## 🛠 Tech Stack
- **Duality AI**: Offroad Synthetic Desert Dataset for training semantic segmentation models.
- **ML Architecture**: **SegFormer-B0** (Transformer-based) for high-speed, accurate pixel-wise classification.
- **Pathway Framework**: Real-time streaming engine for data ingestion, feature engineering, and live RAG (Retrieval-Augmented Generation).
- **LLM**: Reasoning engine for explainable AI alerts.

## 🚀 Key Features
1. **Live Environmental Risk Engine**: Continuous calculation of Drought Risk and Vegetation Health.
2. **Real-Time RAG**: Allows users to query the live state of an ecosystem via natural language.
3. **Reactive Vector Store**: Automatic index updates as new image frames are processed.
4. **Offroad Edge Ready**: Optimized for low-latency inference in remote areas.

## 📁 Project Structure
- `src/ml/`: Training and evaluation pipeline for the Duality AI dataset.
- `src/pathway/`: Streaming logic and real-time feature engineering.
- `docs/`: Technical report and presentation materials.

## 🏃 Quick Start

> [!IMPORTANT]
> **Operating System**: The ML pipeline (Duality AI) runs natively on Windows. However, the **Pathway Framework** requires a Linux environment. On Windows, please use **WSL2 (Ubuntu)** or **Docker**.

1. **Install Dependencies** (Inside WSL2):
   ```bash
   pip install pathway torch transformers numpy openai
   ```
2. **Train Model**:
   ```bash
   python src/ml/train.py
   ```
3. **Run Pipeline**:
   ```bash
   python src/pathway/pipeline.py
   ```

## 📊 Impact on Green Bharat
- **Desertification Monitoring**: Automated detection of soil exposure in Rajasthan and Kutch.
- **Disaster Prevention**: Real-time alerts for drought-prone regions.
- **Ecological Conservation**: Quantitative tracking of vegetation growth/loss over time.
