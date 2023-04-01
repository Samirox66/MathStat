import numpy as np
from scipy.stats import norminvgauss, poisson, cauchy, uniform
import matplotlib.pyplot as plt
import math

sizes = [10, 100, 1000]
NORMAL, CAUCHY, POISSON, UNIFORM = "Normal distribution", "Cauchy distribution", "Poisson distribution", "Uniform distribution"
DENSITY, SIZE = "Плотность распределения", "Размер: "
LINE_TYPE = 'k--'
HISTOGRAM_TYPE = 'stepfilled'
COLORS = ["mediumslateblue", "mediumspringgreen", "sandybrown", "salmon"]

def normal_distribution():
    for size in sizes:
        density = norminvgauss(1, 0)
        histogram = norminvgauss.rvs(1, 0, size=size)
        fig, ax = plt.subplots(1, 1)
        ax.hist(histogram, bins = 20, density = True, histtype = HISTOGRAM_TYPE, color = COLORS[0])
        x = np.linspace(density.ppf(0.01), density.ppf(0.99), 100)
        ax.plot(x, density.pdf(x), LINE_TYPE, lw=0.7)
        ax.set_xlabel(NORMAL)
        ax.set_ylabel(DENSITY)
        ax.set_title(SIZE + str(size))
        plt.grid()
        plt.show()
        fig.savefig('c:/Users/bsam/Documents/web/sem6/mathStat/MathStat/Lab1-4/res/lab1/' +'Normal distribution ' + str(size) +".png")

normal_distribution()

def cauchy_distribution():
    for size in sizes:
        density = cauchy()
        histogram = cauchy.rvs(size=size)
        fig, ax = plt.subplots(1, 1)
        ax.hist(histogram, bins = 20, density=True, histtype=HISTOGRAM_TYPE, color=COLORS[1])
        x = np.linspace(density.ppf(0.01), density.ppf(0.99), 100)
        ax.plot(x, density.pdf(x), LINE_TYPE, lw=0.7)
        ax.set_xlabel(CAUCHY)
        ax.set_ylabel(DENSITY)
        ax.set_title(SIZE + str(size))
        plt.grid()
        plt.show()
        fig.savefig('c:/Users/bsam/Documents/web/sem6/mathStat/MathStat/Lab1-4/res/lab1/' +'Cauchy distribution ' + str(size) +".png")
    return

cauchy_distribution()

def poisson_distribution():
    for size in sizes:
        density = poisson(10)
        histogram = poisson.rvs(10, size=size)
        fig, ax = plt.subplots(1, 1)
        ax.hist(histogram, bins = 20, density=True, histtype=HISTOGRAM_TYPE, color=COLORS[2])
        x = np.arange(poisson.ppf(0.01, 10), poisson.ppf(0.99, 10))

        ax.plot(x, density.pmf(x), LINE_TYPE, lw=0.7)
        ax.set_xlabel(POISSON)
        ax.set_ylabel(DENSITY)
        ax.set_title(SIZE + str(size))
        plt.grid()

        plt.show()
        fig.savefig('c:/Users/bsam/Documents/web/sem6/mathStat/MathStat/Lab1-4/res/lab1/' +'Poisson distribution ' + str(size) +".png")
    return

poisson_distribution()

def uniform_distribution():
    for size in sizes:
        density = uniform(loc=-math.sqrt(3), scale=2 * math.sqrt(3))
        histogram = uniform.rvs(size=size, loc=-math.sqrt(3), scale=2 * math.sqrt(3))
        fig, ax = plt.subplots(1, 1)
        ax.hist(histogram, bins = 20, density=True, histtype=HISTOGRAM_TYPE, color=COLORS[3])
        x = np.linspace(density.ppf(0.01), density.ppf(0.99), 100)
        ax.plot(x, density.pdf(x), LINE_TYPE, lw=0.7)
        ax.set_xlabel(UNIFORM)
        ax.set_ylabel(DENSITY)
        ax.set_title(SIZE + str(size))
        plt.grid()
        plt.show()
        fig.savefig('c:/Users/bsam/Documents/web/sem6/mathStat/MathStat/Lab1-4/res/lab1/' +'Uniform distribution ' + str(size) +".png")
    return

uniform_distribution()