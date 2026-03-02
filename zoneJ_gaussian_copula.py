import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

class GaussianCopula:
    def __init__(self, mean, cov):
        self.mean = mean
        self.cov = cov
        self.dim = len(mean)

    def sample(self, n):
        # Draw samples from a multivariate normal distribution
        mvn_samples = np.random.multivariate_normal(self.mean, self.cov, n)
        # Convert to uniform distribution using the CDF
        uniform_samples = np.array([stats.norm.cdf(mvn_samples[:, i]) for i in range(self.dim)]).T
        return uniform_samples

    def plot_samples(self, samples):
        plt.figure(figsize=(8, 6))
        plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)
        plt.title('Scatter Plot of Gaussian Copula Samples')
        plt.xlabel('Variable 1')
        plt.ylabel('Variable 2')
        plt.grid()
        plt.show()

if __name__ == '__main__':
    # Example usage
    mean = [0, 0]
    cov = [[1, 0.5], [0.5, 1]]
    n_samples = 1000

    copula = GaussianCopula(mean, cov)
    samples = copula.sample(n_samples)
    copula.plot_samples(samples)