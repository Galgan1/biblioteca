import torch
import os

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU count: {torch.cuda.device_count() if torch.cuda.is_available() else 0}")
if torch.cuda.is_available():
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB")
print(f"CPU threads (PyTorch): {torch.get_num_threads()}")
print(f"CPU cores (OS): {os.cpu_count()}")
print(f"PyTorch version: {torch.__version__}")
