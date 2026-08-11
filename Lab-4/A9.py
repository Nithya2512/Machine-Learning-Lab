# =============================================================================
# Lab 04 - A1 (portion for Lab03-A9: Compare mean/std vs NumPy)
# AI Tool Used: Claude (Anthropic, Claude Sonnet 5) via claude.ai
# Prompt summary: "Regenerate A9.py to reuse A8_AI's dataset_statistics and
#   build a comparison table against numpy.mean / numpy.std as a pandas
#   DataFrame for cleaner display."
# Human review: kept ddof=0 for numpy.std to match the population-std
#   convention used in calculate_std.
# =============================================================================
import pandas as pd
from A8_AI import dataset_statistics


def build_comparison_table(numeric_df):
    """
    Build a side-by-side comparison of own vs NumPy mean/std for every
    column in numeric_df.

    Returns
    -------
    pandas.DataFrame with columns:
        Own_Mean, NumPy_Mean, Own_Std, NumPy_Std
    """
    own_means, _, own_stds = dataset_statistics(numeric_df)
    numpy_means = numeric_df.mean(axis=0)
    numpy_stds = numeric_df.std(axis=0, ddof=0)

    comparison = pd.DataFrame({
        "Own_Mean": pd.Series(own_means),
        "NumPy_Mean": numpy_means,
        "Own_Std": pd.Series(own_stds),
        "NumPy_Std": numpy_stds,
    })
    return comparison


if __name__ == "__main__":
    df = pd.read_excel(
        "Lab Session Data (1).xlsx",
        sheet_name="marketing_campaign",
    )
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    numeric_df = numeric_df.fillna(numeric_df.mean())

    comparison_table = build_comparison_table(numeric_df)
    pd.set_option("display.float_format", lambda x: f"{x:.2f}")
    print("Mean & Standard Deviation Comparison (Own vs NumPy)")
    print("-" * 60)
    print(comparison_table)
