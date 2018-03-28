import matplotlib.pyplot as plt


def plot_signal(t, y, title):
    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title(title)
    plt.grid(True)
    plt.show()
