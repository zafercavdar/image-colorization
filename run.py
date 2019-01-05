import os

import torch
import torch.nn as nn
from torchvision import transforms

from src.preprocess import GrayscaleImageFolder
from src.ColorizationNet import ColorizationNet
from src.helpers import is_gpu_available
from src.training import train
from src.validation import validate

# CNN model
model = ColorizationNet()
# loss function = mean squared error
criterion = nn.MSELoss()
# optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=1e-2, weight_decay=0.0)

if is_gpu_available():
    criterion = criterion.cuda()
    model = model.cuda()


# Training
train_transforms = transforms.Compose(
    [transforms.RandomResizedCrop(224), transforms.RandomHorizontalFlip()])
train_imagefolder = GrayscaleImageFolder('./training/', train_transforms)
train_loader = torch.utils.data.DataLoader(
    train_imagefolder, batch_size=64, shuffle=True)

# Validation
val_transforms = transforms.Compose(
    [transforms.Resize(256), transforms.CenterCrop(224)])
val_imagefolder = GrayscaleImageFolder('./validation/', val_transforms)
val_loader = torch.utils.data.DataLoader(
    val_imagefolder, batch_size=64, shuffle=False)

# Make folders and set parameters
os.makedirs('outputs/color', exist_ok=True)
os.makedirs('outputs/gray', exist_ok=True)
os.makedirs('checkpoints', exist_ok=True)
save_images = True
best_losses = 0.005
epochs = 100

# Train model
for epoch in range(epochs):
    # Train for one epoch, then validate
    train(train_loader, model, criterion, optimizer, epoch)
    torch.save(model.state_dict(), 'checkpoints/model-epoch-{}.pth'.format(epoch + 1))

with torch.no_grad():
    losses = validate(val_loader, model, criterion, save_images, epoch)

# Save checkpoint and replace old best model if current model is better
# if losses < best_losses:
# best_losses = losses
torch.save(model.state_dict(), 'checkpoints/model-epoch-{}-losses-{:.3f}.pth'.format(epoch + 1, losses))