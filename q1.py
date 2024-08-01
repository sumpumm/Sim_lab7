import numpy as np

def autocorrelation(x, lag):
    n = len(x)
    mean_x = np.mean(x)
    numerator = 0.0
    denominator = 0.0
    
    for i in range(n - lag):
        numerator += (x[i] - mean_x) * (x[i + lag] - mean_x)
    
    for i in range(n):
        denominator += (x[i] - mean_x) ** 2
    
    return numerator / denominator

def autocorrelation_test(x, max_lag):
    acf = [autocorrelation(x, lag) for lag in range(max_lag + 1)]
    return acf

# Example usage:
if __name__ == "__main__":
    # Generate a sample time series data
    np.random.seed(42)
    time_series_data = np.random.randn(100)
    
    # Set the maximum lag for autocorrelation
    max_lag = 20
    
    # Calculate the autocorrelation function
    acf = autocorrelation_test(time_series_data, max_lag)
    
    # Print the autocorrelation function
    print("Lag | Autocorrelation")
    print("---------------------")
    for lag in range(max_lag + 1):
        print(f"{lag:3d} | {acf[lag]:.4f}")