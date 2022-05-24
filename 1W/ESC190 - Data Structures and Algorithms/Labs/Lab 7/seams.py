#%%
energies = [[24,      22,      30,      15,      18,      19],
            [12,      23,      15,      23,      10,      15],
            [11,      13,      22,      13,      21,      14],
            [13,      15,      17,      28,      19,      21],
            [17,      17,      7,       27,      20,      19]]


def min_energy_seam(energies):
    height = len(energies)
    width = len(energies[0])
    cost = [[0] * width for i in range(height)]

    # initialize first row of cost
    for i in range(width):
        cost[0][i] = energies[0][i]
    
    for i in range(1, height):
        for j in range(width):
            min_prev_cost = 10000000000
            for x in [-1, 0, 1]:
                if (j+x) < 0 or (j+x) > (width-1):
                    continue
                if cost[i-1][j+x] < min_prev_cost:
                    min_prev_cost = cost[i-1][j+x]
            cost[i][j] = energies[i][j] + min_prev_cost
    
    print(cost)
    return min(cost[height-1])



# %%
