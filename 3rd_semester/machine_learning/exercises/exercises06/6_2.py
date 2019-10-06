import matplotlib.pyplot as plt
import numpy as np

def N(x_1, x_2, m_1, m_2, std_1, std_2, rho):
    x_vector = np.array([[x_1],[x_2]])
    m_vector = np.array([[m_1], [m_2]])
    cov_matrix = np.array([[std_1**2, rho * std_1 * std_2], [rho * std_1 * std_2, std_2**2]])
    return 1 / np.sqrt((2 * np.pi)**2 * np.linalg.det(cov_matrix)) * np.e **( -1/2 * np.matmul(np.matmul(np.transpose(x_vector - m_vector), np.linalg.inv(cov_matrix)), x_vector - m_vector))

def plot_N(m_1, m_2, std_1, std_2, rho):
    X1, X2 = np.meshgrid(np.linspace(-3, 3, 30), np.linspace(-3,3, 100))
    f = np.vectorize(lambda x1, x2: N(x1, x2, m_1, m_2, std_1, std_2, rho))
    Z = f(X1, X2)
    fig, ax = plt.subplots()
    plt.style.use("seaborn")
    ax.axis('equal')
    ax.contour(X1, X2, Z)
    fig.savefig("0_0_1_1_minus075.png")

if __name__ == "__main__":
    plot_N(0,0,1,1,-0.75)
