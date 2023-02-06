import itertools as it

def get_p_win(*args: tuple) -> float:
    probability_of_loss = 1
    for i in args:
        probability_of_loss *= (1-i[0] / i[1])
    return (1 - probability_of_loss) * 100

def test_strategies(entries: int, draws: int):
    l = it.combinations_with_replacement(range(entries+1), draws)
    max_probability = 0
    max_probability_combination = None
    for i in l:
        sum_of_indicies = 0
        for index in range(draws):
            sum_of_indicies += i[index]
        if sum_of_indicies == entries:
            test_input = []
            for element in i:
                test_input.append((element, 217))
            p_win = get_p_win(*tuple(test_input))
            if p_win > max_probability:
                max_probability = p_win
                max_probability_combination = i
            print ('For case', i, ' P =', p_win)
    print('Max Probability:', max_probability_combination, 'with', max_probability)

#print(get_p_win((4, 217), (0, 217), (0, 217)))
test_strategies(150, 3)
