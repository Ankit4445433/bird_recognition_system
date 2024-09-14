import os
import numpy as np
import torch
import glob  ## finds all the pathnames matching a specified pattern
import torch.nn as nn   # helps build neural network models
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.autograd import Variable   ## for automatic differentiation that performs back propagation
import torchvision
import pathlib   #  provides various classes representing file system paths with semantics appropriate for different operating systems
import cv2
from PIL import Image
from io import open
import torch.functional as F





