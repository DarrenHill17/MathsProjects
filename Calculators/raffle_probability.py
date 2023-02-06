import itertools as it

class raffle_probability:
    def get_p_win(self, *args: tuple) -> float:
        probability_of_loss = 1
        for i in args:
            probability_of_loss *= (1-i[0] / i[1])
        return (1 - probability_of_loss) * 100

    def test_strategies_equal_entries(self, entries: int, draws: int):
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
                p_win = self.get_p_win(*tuple(test_input))
                if p_win > max_probability:
                    max_probability = p_win
                    max_probability_combination = i
                print ('For case', i, ' P =', p_win)
        print('Max Probability:', max_probability_combination, 'with', max_probability)

    def test_strategies(self, entries: int, *existing_entries: int):
        draws = len(existing_entries)
        l = it.combinations_with_replacement(range(entries+1), draws)
        max_probability = 0
        max_probability_combination = None
        for i in l:
            sum_of_indicies = 0
            for index in range(draws):
                sum_of_indicies += i[index]
            if sum_of_indicies == entries:
                test_input = []
                count = 0
                for element in i:
                    test_input.append((element, element + existing_entries[count]))
                    count += 1
                p_win = self.get_p_win(*tuple(test_input))
                if p_win > max_probability:
                    max_probability = p_win
                    max_probability_combination = i
                print ('For case', i, ' P =', p_win)
        print('Max Probability:', max_probability_combination, 'with', max_probability)