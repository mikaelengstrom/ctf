# -*- coding: utf-8 -*-
from __future__ import division

from itertools import cycle
from decipher import int_to_letter
from decipher import letter_to_int
from operator import itemgetter


class Analyzer(object):
    def __init__(self, data, cipher_key_length):
        self.data = data
        self.cipher_key_length = cipher_key_length
        self.alphabet_order_by_occurence = "etaoinshrdlcumwfgypbvkjxqz"

    def get_data(self):
        return map(lambda x: x.replace(' ', ''), self.data)

    def count_letters(self):
        result = []
        for data_set in self.get_data():
            counted = self.count_letters_for_file(data_set)
            result = self._merge(result, counted) if result else counted

        return map(self.set_best_guess, result)

    def count_letters_for_file(self, data_set):
        cipher_key = cycle(range(0, self.cipher_key_length))

        results = []
        for c in data_set:
            key = next(cipher_key)
            if key >= len(results):
                results.append({x: {"count": 0} for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"})

            results[key][c]["count"] += 1

        return results

    def _merge(self, stack, results):
        for outer_key, inner_dict in enumerate(results):
            for k, value in inner_dict.items():
                stack[outer_key][k]['count'] += value['count']

        return stack

    def set_best_guess(self, result):
        sorted_by_ocurence = sorted(result, key=lambda x: result[x]['count'], reverse=True)
        for c, best_guess in zip(sorted_by_ocurence, self.alphabet_order_by_occurence):
            result[c]['best_guess'] = best_guess

        return result

class Printer(object):
    def __init__(self, data):
        self.data = data
        self.total_per_char = {}
        self.total_count = 0

    def prnt(self):
        for key, result in enumerate(self.data):
            print("Printing analyzis of key: %s" % key)
            self.print_one_result(result)
            print

        print 'e: %.2f, t: %.2f, q: %.2f, z:%.2f' % (
            self.percent_of_total(self.total_per_char['e']),
            self.percent_of_total(self.total_per_char['t']),
            self.percent_of_total(self.total_per_char['q']),
            self.percent_of_total(self.total_per_char['z'])
        )
        print 'optimal: '
        print 'e: 12.70, t: 9.05, q: 0.09, z: 0.07'
        print 'total count: %s' % self.total_count

    def percent_of_total(self, x):
        return (x / self.total_count) * 100

    def print_one_result(self, result):
        for c in sorted(result, key=lambda x: result[x]['count'], reverse=True):
            total_for_char = self.total_per_char.get(result[c]['best_guess'])
            if not total_for_char:
                total_for_char = 0

            print(u"%s : %02d - Best guess: %s – int: %02d" % (c, result[c]['count'], result[c]['best_guess'], letter_to_int(c)))
            self.total_per_char[result[c]['best_guess']] = total_for_char + result[c]['count']
            self.total_count = self.total_count + result[c]['count']

data_sets = []
for file_name in ['found1', 'found2', 'found3', 'krypton6']:
    with open(file_name, 'r') as file:
        data_sets.append(file.read())


analyzer = Analyzer(data_sets, 9)
data = analyzer.count_letters()
Printer(data).prnt()
