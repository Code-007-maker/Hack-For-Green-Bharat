import torch
import sys
import os
print(f"Python Executable: {sys.executable}")
print(f"Python Path: {sys.path}")
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
from model import get_green_vision_model
import numpy as np

# Mock Dataset to simulate Duality AI Offroad Synthetic Desert Dataset
class DualityDesertDataset(Dataset):
    def __init__(self, size=100, img_size=(512, 512), num_classes=10):
        self.size = size
        self.img_size = img_size
        self.num_classes = num_classes

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        # In a real scenario, this would load images and labels from the Duality dataset
        image = torch.randn(3, *self.img_size)
        mask = torch.randint(0, self.num_classes, self.img_size)
        return {"pixel_values": image, "labels": mask}

def train():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training on: {device}")

    model = get_green_vision_model(num_labels=10).to(device)
    optimizer = optim.AdamW(model.parameters(), lr=6e-5)
    
    dataset = DualityDesertDataset(size=50) # Small subset for demonstration
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    model.train()
    for epoch in range(1): # Single epoch for hackathon demo reproducibility
        total_loss = 0
        for batch in dataloader:
            pixel_values = batch["pixel_values"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(pixel_values=pixel_values, labels=labels)
            loss = outputs.loss
            
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch+1} completed. Avg Loss: {total_loss/len(dataloader):.4f}")

    # Save model
    torch.save(model.state_dict(), "greenvision_model.pth")
    print("Model saved to greenvision_model.pth")

if __name__ == "__main__":
    train()
