# ZED-Cloudpoint
## Environment setup
1. Setup Python environment
- Python v3.10
2. Install NVIDIA Drivers
3. Install CUDA support
4. Install ZED-sdk through official website according to your computer's specs
5. Install zstd
- `sudo apt install zstd`
6. Add execution permission to the install installer using chmod +x and replace the name with the version downloaded
- `chmod +x ZED_SDK_Ubuntu24_cuda13.0_tensorrt10.13_v5.2.0.zstd.run`
- `./ZED_SDK_Ubuntu24_cuda13.0_tensorrt10.13_v5.2.0.zstd.run`
7. Download Python API wrapper requirements
- `python -m pip install cython numpy opencv-python pyopengl`
8. For improved CuPy using pip
- `pip install cupy-cuda11x  # For CUDA 11.x`
- `pip install cupy-cuda12x  # For CUDA 12.x`
- `pip install cupy-cuda12x  # For CUDA 13.x`
9. Install cuda bindings using pip
- `pip install cuda-python`