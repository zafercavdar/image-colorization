from os import listdir
from os import makedirs
from os.path import join
from PIL import Image as PImage

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import transforms
from src.preprocess import GrayscaleImageFolder
from src.ColorizationNet import ColorizationNet
from src.helpers import is_gpu_available
from src.validation import validate

# CNN model
model = ColorizationNet()
# loss function = mean squared error
criterion = nn.MSELoss()

if is_gpu_available():
    criterion = criterion.cuda()
    model = model.cuda()

# Load model
pretrained = torch.load('model41k-epoch-62-losses-0.002.pth', map_location=lambda storage, loc: storage)
model.load_state_dict(pretrained)

# create output folders
makedirs('outputs/color', exist_ok=True)
makedirs('outputs/gray', exist_ok=True)

# Validation
val_transforms = transforms.Compose(
    [transforms.Resize(256), transforms.CenterCrop(224)])
val_imagefolder = GrayscaleImageFolder('./images/demo', val_transforms)
val_loader = torch.utils.data.DataLoader(
    val_imagefolder, batch_size=64, shuffle=False)


# Validate
save_images = True
with torch.no_grad():
    validate(val_loader, model, criterion, save_images, 0)


# load output and original images for display
def loadImages(path):
    # return array of images
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        full_path = join(path, image)
        img = PImage.open(full_path)
        loadedImages.append(img)
    return loadedImages


path_org = "./images/demo/256x256/"
path_gray = "./outputs/gray/"
path_colorized = "./outputs/color/"

# images in arrays
org = loadImages(path_org)
gray = loadImages(path_gray)
color = loadImages(path_colorized)
n = len(org)

for i in range(n):
    # shows every image tuple(org, gray, colorized)
    f, axarr = plt.subplots(1, 3)
    axarr[0].imshow(org[i])
    axarr[1].imshow(gray[i])
    axarr[2].imshow(color[i])
    plt.show()
