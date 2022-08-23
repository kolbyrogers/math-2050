import numpy as np

def counter(fname):
    word_len = []
    f = open(fname,'r')
    for line in f:
        words = line.split()
        for word in words:
            word_len.append(len(word))
    return word_len

def summary_stats(data):
    stats = []
    stats.append(np.mean(data)) # mean
    stats.append(np.median(data)) # median
    stats.append(max(set(data), key=data.count)) # mode
    stats.append(np.std(data)) # std dev
    stats.append(np.var(data)) # variance
    stats.append(np.max(data) - np.min(data)) # range
    stats.append(np.min(data)) # min
    stats.append(np.max(data)) # max
    stats.append(np.sum(data)) # sum
    stats.append(len(data)) # count
    return stats

def main():
    data = counter("letter.txt")
    print("1. Data: ", data, "\n")
    print("2. Summary Stats: ", summary_stats(data))

main()