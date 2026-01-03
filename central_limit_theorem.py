"""
Central Limit Theorem for Process Improvement

This script demonstrates how to use the Central Limit Theorem to estimate
workload probabilities for returns management processes.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm


def calculate_probability(mean, std, threshold, sample_size=1):
    """
    Calculate probability of sample mean being below threshold.

    Using CLT: sample mean ~ N(mu, sigma/sqrt(n))
    """
    # Standard error of the mean
    std_error = std / np.sqrt(sample_size)

    # Z-score
    z_score = (threshold - mean) / std_error

    # Probability
    probability = norm.cdf(z_score)

    return probability, z_score


def visualize_distribution(mean, std, threshold, sample_size=1):
    """Visualize the normal distribution with threshold."""
    std_error = std / np.sqrt(sample_size)

    # Generate x values
    x = np.linspace(mean - 4*std_error, mean + 4*std_error, 1000)
    y = norm.pdf(x, mean, std_error)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot distribution
    ax.plot(x, y, 'b-', linewidth=2, label='Distribution')

    # Fill area below threshold
    x_fill = x[x <= threshold]
    y_fill = norm.pdf(x_fill, mean, std_error)
    ax.fill_between(x_fill, y_fill, alpha=0.3, color='green',
                    label=f'P(X ≤ {threshold})')

    # Add vertical lines
    ax.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean}')
    ax.axvline(threshold, color='green', linestyle='-',
               label=f'Threshold = {threshold}')

    ax.set_xlabel('Items per Carton')
    ax.set_ylabel('Probability Density')
    ax.set_title('Central Limit Theorem - Returns Management Workload')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('clt_distribution.png', dpi=150)
    plt.close()

    print("Visualization saved to: clt_distribution.png")


def returns_workload_analysis():
    """
    Analyze returns management workload using Central Limit Theorem.

    Scenario:
    - Average items per carton: 23
    - Standard deviation: 7 items
    - Team capacity threshold: 30 items per carton
    """
    # Parameters from historical data
    mean_items = 23  # Average items per carton
    std_items = 7    # Standard deviation
    threshold = 30   # Team capacity threshold

    print("=" * 60)
    print("RETURNS MANAGEMENT WORKLOAD ANALYSIS")
    print("=" * 60)
    print(f"\nHistorical Data:")
    print(f"  Average items per carton: {mean_items}")
    print(f"  Standard deviation: {std_items}")
    print(f"  Team capacity threshold: {threshold} items/carton")

    # Single carton probability
    prob_single, z_single = calculate_probability(mean_items, std_items, threshold)
    print(f"\n--- Single Carton Analysis ---")
    print(f"Z-score: {z_single:.4f}")
    print(f"P(items ≤ {threshold}): {prob_single:.4f} ({prob_single*100:.2f}%)")
    print(f"P(items > {threshold}): {1-prob_single:.4f} ({(1-prob_single)*100:.2f}%)")

    # Weekly analysis (assuming 50 cartons per week)
    sample_sizes = [1, 10, 25, 50, 100]

    print(f"\n--- Sample Size Effect (CLT) ---")
    print(f"{'Sample Size':<15} {'Std Error':<15} {'P(mean ≤ {})'.format(threshold):<20}")
    print("-" * 50)

    for n in sample_sizes:
        prob_n, _ = calculate_probability(mean_items, std_items, threshold, n)
        std_error = std_items / np.sqrt(n)
        print(f"{n:<15} {std_error:<15.4f} {prob_n*100:<20.4f}%")

    # Create visualization
    visualize_distribution(mean_items, std_items, threshold)

    return prob_single


def confidence_interval_analysis():
    """Calculate confidence intervals for mean items per carton."""
    mean_items = 23
    std_items = 7
    sample_sizes = [10, 30, 50, 100]
    confidence_level = 0.95

    print("\n" + "=" * 60)
    print("CONFIDENCE INTERVAL ANALYSIS")
    print("=" * 60)
    print(f"\nConfidence Level: {confidence_level*100}%")

    z_critical = norm.ppf((1 + confidence_level) / 2)

    print(f"\n{'Sample Size':<15} {'Margin of Error':<20} {'95% CI':<25}")
    print("-" * 60)

    for n in sample_sizes:
        margin = z_critical * (std_items / np.sqrt(n))
        ci_lower = mean_items - margin
        ci_upper = mean_items + margin
        print(f"{n:<15} {margin:<20.2f} [{ci_lower:.2f}, {ci_upper:.2f}]")


def main():
    """Main function demonstrating Central Limit Theorem applications."""
    returns_workload_analysis()
    confidence_interval_analysis()

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
