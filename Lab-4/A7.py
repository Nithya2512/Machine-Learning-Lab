# =============================================================================
# Lab 04 - A1 (portion for Lab03-A7: Dot Product & Euclidean Norm)
# AI Tool Used: Claude (Anthropic, Claude Sonnet 5) via claude.ai
# Prompt summary: "Regenerate A7.py's dot_product and euclidean_norm
#   functions using numpy vectorization, then compare against numpy.dot
#   and numpy.linalg.norm directly."
# Human review: none needed, straightforward vectorized reimplementation.
# =============================================================================
import pandas as pd
import numpy as np


def dot_product(vector1, vector2):
    """Dot product of two equal-length numeric vectors."""
    a = np.asarray(vector1, dtype=float)
    b = np.asarray(vector2, dtype=float)
    return float(np.sum(a * b))


def euclidean_norm(vector):
    """Euclidean (L2) norm / length of a numeric vector."""
    v = np.asarray(vector, dtype=float)
    return float(np.sqrt(np.sum(v ** 2)))


if __name__ == "__main__":
    df = pd.read_excel(
        "Lab Session Data (1).xlsx",
        sheet_name="marketing_campaign",
    )
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    numeric_df = numeric_df.fillna(numeric_df.mean())

    A = numeric_df.iloc[0].tolist()
    B = numeric_df.iloc[1].tolist()

    my_dot = dot_product(A, B)
    my_norm_A = euclidean_norm(A)
    my_norm_B = euclidean_norm(B)

    numpy_dot = np.dot(A, B)
    numpy_norm_A = np.linalg.norm(A)
    numpy_norm_B = np.linalg.norm(B)

    print("Dot Product (Own Function):", my_dot)
    print("Dot Product (NumPy):", numpy_dot)
    print("\nEuclidean Norm of A (Own Function):", my_norm_A)
    print("Euclidean Norm of A (NumPy):", numpy_norm_A)
    print("\nEuclidean Norm of B (Own Function):", my_norm_B)
    print("Euclidean Norm of B (NumPy):", numpy_norm_B)
