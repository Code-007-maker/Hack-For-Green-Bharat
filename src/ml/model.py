import torch
import torch.nn as nn
from transformers import SegformerForSemanticSegmentation, SegformerConfig

# Using SegFormer-B0 for its incredible balance of speed (real-time) and accuracy.
# Perfectly suited for live streaming analysis on remote hardware.

def get_green_vision_model(num_labels=10):
    """
    Initializes a SegFormer model for environmental segmentation.
    Classes: Trees, Bushes, Dry Grass, Rocks, Logs, Landscape, Sky, etc.
    """
    config = SegformerConfig.from_pretrained(
        "nvidia/mit-b0", 
        num_labels=num_labels,
        id2label={i: f"class_{i}" for i in range(num_labels)},
        label2id={f"class_{i}": i for i in range(num_labels)}
    )
    
    model = SegformerForSemanticSegmentation.from_pretrained(
        "nvidia/mit-b0",
        config=config,
        ignore_mismatched_sizes=True
    )
    
    return model

if __name__ == "__main__":
    # Smoke test
    model = get_green_vision_model()
    dummy_input = torch.randn(1, 3, 512, 512)
    outputs = model(dummy_input)
    print(f"Model initialized. Output shape: {outputs.logits.shape}")
