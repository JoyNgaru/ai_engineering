import numpy as np
#we are importing numpy library to perform the SVD operation on the matrix A. 
# The function perform_svd takes a matrix A as input and returns the matrices U, Σ (Sigma), and VT that result from the SVD decomposition. 
# The code also includes a test case to verify that the original matrix A can be reconstructed from U, Σ, and VT.

def perform_svd(A):
   
    U, Sigma, VT = np.linalg.svd(A)
    
    # Convert Sigma (1D array) into a diagonal matrix
    Sigma_matrix = np.zeros((U.shape[0], VT.shape[0]))
    np.fill_diagonal(Sigma_matrix, Sigma)
    
    return U, Sigma_matrix, VT

# Test the implementation
if __name__ == "__main__":
    # Define the matrix A
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])

    # Perform SVD
    U, Sigma, VT = perform_svd(A)

    # Reconstruct A using U, Σ, and VT
    A_reconstructed = U @ Sigma @ VT

    # Print results
    print("Original Matrix A:")
    print(A)
    print("\nMatrix U:")
    print(U)
    print("\nMatrix Σ (Sigma):")
    print(Sigma)
    print("\nMatrix VT:")
    print(VT)
    print("\nReconstructed Matrix A:")
    print(A_reconstructed)

    # Verify the reconstruction
    if np.allclose(A, A_reconstructed):
        print("\nReconstruction successful: A matches the product UΣVT.")
    else:
        print("\nReconstruction failed: A does not match the product UΣVT.")
