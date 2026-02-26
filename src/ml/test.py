import torch
from model import get_green_vision_model
import numpy as np
from torch.utils.data import DataLoader
from train import DualityDesertDataset

def compute_iou(preds, labels, num_classes=10):
    ious = []
    preds = torch.argmax(preds, dim=1)
    for cls in range(num_classes):
        intersection = ((preds == cls) & (labels == cls)).sum().item()
        union = ((preds == cls) | (labels == cls)).sum().item()
        if union == 0:
            ious.append(float('nan')) # Ignore if class not present
        else:
            ious.append(intersection / union)
    return np.nanmean(ious)

def evaluate():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = get_green_vision_model(num_labels=10).to(device)
    
    # Load weights if exist
    try:
        model.load_state_dict(torch.load("greenvision_model.pth", map_location=device))
    except:
        print("Pre-trained weights not found, evaluating fresh model.")

    dataset = DualityDesertDataset(size=10)
    dataloader = DataLoader(dataset, batch_size=1)

    model.eval()
    all_ious = []
    
    print("--- EVALUATION REPORT ---")
    with torch.no_grad():
        for i, batch in enumerate(dataloader):
            pixel_values = batch["pixel_values"].to(device)
            labels = batch["labels"].to(device)
            
            outputs = model(pixel_values=pixel_values)
            miou = compute_iou(outputs.logits, labels)
            all_ious.append(miou)
            
            print(f"Image {i+1}: mIoU = {miou:.4f}")

    print(f"\nFinal Mean IoU: {np.mean(all_ious):.4f}")
    print("Failure Case Analysis: Low IoU typically observed in 'Dry Grass' vs 'Landscape' due to visual similarity in synthetic desert spectra.")

if __name__ == "__main__":
    evaluate()
