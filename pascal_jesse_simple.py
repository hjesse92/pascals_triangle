from scipy.special import comb
import time

start_time = time.time()
line = []
lookup_line = 500

if lookup_line % 2 == 0:
    for iteration in range(int(lookup_line / 2)):
        line = line + [comb(lookup_line - 1, iteration, exact=True)]
    line = line + [i for i in list(reversed(line))]
else:
    for iteration in range(int(lookup_line / 2) + 1):
        line = line + [comb(lookup_line - 1, iteration, exact=True)]
    line = line + [i for i in list(reversed(line))[1::]]

print(line)
print("--- %s seconds ---" % (time.time() - start_time))
