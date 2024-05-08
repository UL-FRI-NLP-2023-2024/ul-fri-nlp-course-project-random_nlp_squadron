# Import necessary modules
import pycuda.driver as cuda
import pycuda.autoinit  # Automatically initializes CUDA
from pycuda.compiler import SourceModule

def test_cuda_device():
    # Define a simple kernel that computes the square of numbers
    mod = SourceModule("""
    __global__ void compute_square(float *d_result, float *d_data)
    {
        int idx = threadIdx.x + blockIdx.x * blockDim.x;
        float f = d_data[idx];
        d_result[idx] = f * f;
    }
    """)

    # Allocate input data and output arrays on GPU
    import numpy as np
    data = np.random.randn(256).astype(np.float32)
    data_gpu = cuda.mem_alloc(data.nbytes)
    result_gpu = cuda.mem_alloc(data.nbytes)
    cuda.memcpy_htod(data_gpu, data)

    # Get the kernel function from the compiled module
    kernel = mod.get_function("compute_square")

    # Launch the kernel on the data
    kernel(result_gpu, data_gpu, block=(256,1,1), grid=(1,1))

    # Copy the result back to host
    result = np.empty_like(data)
    cuda.memcpy_dtoh(result, result_gpu)

    print("Original data:", data)
    print("Computed squares:", result)

if __name__ == "__main__":
    test_cuda_device()

