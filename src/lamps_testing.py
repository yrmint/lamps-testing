import numpy as np
import scipy
import matplotlib.pyplot as plt
import parsing

n = parsing.n
ms = parsing.m
ss = parsing.s
experiments = parsing.nexp

if __name__ == '__main__':
    """
        Lamps testing
        
        Among N light bulbs, part r is faulty. Each time, m light bulbs are randomly selected and checked to see how 
        many of them are working. This program guesses the number of faulty light bulbs. 
        
        Part 1a: After each test, a series of posterior probability distributions of hypotheses about the number of
        faulty light bulbs is calculated. The corresponding results are presented visually on a graph in the form of
        changes in probability distribution diagrams of hypotheses over the course of experiments.
        
        Part 1b: After each attempt, it is determined which hypotheses have the highest probability. The evolution of
        changes in the most probable hypotheses is visualized.
        
        Part 1c: The dependence of the number of prevailing hypotheses on the number of experiments performed is 
        constructed.
    """

    threshold = 0.05
    r = n
    hypotheses = np.arange(r + 1)
    exp = np.arange(experiments)
    preval_hypotheses = np.zeros(experiments)
    prior = np.ones(r + 1) / (r + 1)
    prob_dist = np.zeros((experiments, r + 1))
    most_likely_number = np.zeros((experiments, 4))
    for i in range(experiments):
        m = ms[i]
        s = ss[i]
        print(i)
        likelihood = np.zeros(r + 1)
        for j in range(r + 1):
            likelihood[j] = scipy.stats.binom.pmf(s, m, j / r)
        posterior = prior * likelihood
        posterior /= np.sum(posterior)
        prob_dist[i] = posterior
        prior = posterior
        most_likely_number[i] = np.argsort(posterior)[-1::-1][:4]

    # Plot the probability distribution for each experiment (part 1a)
    columns = np.zeros((r + 1, experiments))
    most_likely_list = np.zeros(experiments)
    most_likely = 0
    for i in range(r + 1):
        plt.plot(prob_dist[:, i])
        columns[i] = prob_dist[:, i]
        if columns[i][experiments - 1] > most_likely_list[experiments - 1]:
            most_likely_list = columns[i]
            most_likely = i
    plt.xlabel('Experiment')
    plt.ylabel('Probability')
    plt.show()

    # Guess the number of faulty bulbs based on the most likely hypothesis
    title = 'The most likely number of faulty bulbs is: ' + str(most_likely)
    plt.title(title)
    plt.xlabel('Experiment')
    plt.ylabel('Probability')
    plt.plot(most_likely_list)
    plt.show()

    # Plot top 4 hypotheses for each experiment (part 1b)
    for i in range(4):
        plt.plot(most_likely_number[:, i], label=f'Top {i + 1}')
    plt.xlabel('Experiment')
    plt.ylabel('Number of faulty bulbs')
    plt.legend()
    plt.show()

    # Plot number of prevailing hypotheses (part 1c)
    for i in range(experiments):
        for j in range(r):
            if prob_dist[i][j] > threshold:
                preval_hypotheses[i] += 1
    plt.plot(preval_hypotheses)
    plt.xlabel('Experiment')
    plt.ylabel('Number of prevailing hypotheses')
    plt.show()
