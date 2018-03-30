import matplotlib.pyplot as plt


def plot_signal(t, y, title):
    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_histogram(y, title):
    plt.xlabel('Value')
    plt.ylabel('Quantity')
    plt.title(title)
    plt.hist(y, alpha=0.5, histtype='bar', ec='black')
    plt.show()
