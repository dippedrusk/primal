import argparse
import datetime
import random
import sys
from enum import Enum

parser = argparse.ArgumentParser(description='Wordle but with prime numbers')
parser.add_argument('--only-primes', action='store_true')
parser.add_argument('--daily', action='store_true')
parser.add_argument('--nonvisual', action='store_true')

class Stat(Enum):
    MISS = '-'
    PARTIAL = 'c'
    HIT = 'o'

with open('primes.txt', 'r', encoding='utf-8') as f:
    primes = list(map(int, list(f)))
GREEN = '\x1b[42m\x1b[30m'
YELLOW = '\x1b[43m\x1b[30m'
WHITE = '\x1b[47m\x1b[30m'
END = '\x1b[0m'


def compute_stats(guess, target):
    guess = str(guess)
    target = str(target)
    stats = [None] * 5
    unseen = []
    # probably faster with some fancy bit blitzing but eh
    for i, digit in enumerate(guess):
        if digit == target[i]:
            stats[i] = Stat.HIT
        else:
            unseen.append(target[i])
    for i, digit in enumerate(guess):
        if digit == target[i]:
            continue
        if digit in unseen:
            unseen.remove(digit)
            stats[i] = Stat.PARTIAL
        else:
            stats[i] = Stat.MISS
    return stats

def stringify(singular, plural, indices):
    count = len(indices)
    if count == 0:
        return ''
    stat_noun = singular if count == 1 else plural
    position_noun = 'position' if count == 1 else 'positions'
    return f"{count} {stat_noun} ({position_noun} {', '.join(map(str, indices))}), "

def find_last(string, substring):
    try:
        res = string.index(substring)
    except ValueError:
        sys.exit('Oops, a dev fucked up. Please screenshot and report this bug!')
    try:
        while True:
            res = string.index(substring, res+1)
    except ValueError:
        return res

def shorten(description):
    description = description[:-2]
    last_paren = find_last(description, '(')
    description = description[:last_paren].strip()
    last_comma = find_last(description, ',')
    description = description[:last_comma] + ' and' + description[last_comma+1:]
    return description

def describe_line(line):
    hit_indices, miss_indices, partial_indices = [], [], []
    for i, stat in enumerate(line):
        if stat == Stat.HIT:
            hit_indices.append(i+1)
        elif stat == Stat.MISS:
            miss_indices.append(i+1)
        else:
            partial_indices.append(i+1)
    if len(hit_indices) == 5:
        return 'Won!'
    if len(miss_indices) == 5:
        return 'All misses'
    if len(partial_indices) == 5:
        return 'All right but in the wrong places'
    hits = stringify('hit', 'hits', hit_indices)
    misses = stringify('miss', 'misses', miss_indices)
    partials = stringify('in the wrong position', 'in the wrong position', partial_indices)
    together = hits + misses + partials
    return shorten(together)

def colourize(stat, text):
    if stat == Stat.HIT:
        return f'{GREEN}{text}{END}'
    if stat == Stat.PARTIAL:
        return f'{YELLOW}{text}{END}'
    return f'{WHITE}{text}{END}'

def print_total_stats(total_stats, date):
    print(f'PRIMAL {date} {len(total_stats)}/6')
    for i, line in enumerate(total_stats):
        print(f'Line {i}:', describe_line(line))
    print()
    print(f'PRIMAL {date} {len(total_stats)}/6')
    for line in total_stats:
        print(''.join([colourize(stat, f' {stat.value} ') for stat in line]))
    print()

def print_guess(guess, stats, nonvisual):
    if nonvisual:
        print(''.join([stat.value for stat in stats]))
        return
    string = ''
    for digit, stat in zip(str(guess), stats):
        string += colourize(stat, f'[{digit}]') + ' '
    print(string.strip())

def get_guess(only_primes):
    while True:
        try:
            guess = int(input('Guess the prime: '))
            assert guess > 0, 'Your number is not positive!'
            assert len(str(guess)) == 5, 'You did not type a 5-digit natural number!'
            if only_primes:
                assert guess in primes, 'You did not guess a prime!'
            return guess
        except ValueError:
            print('You did not type a natural number!')
        except AssertionError as err:
            print(err)

def game(target, only_primes, nonvisual):
    total_stats = []
    for _ in range(6):
        guess = get_guess(only_primes)
        stats = compute_stats(guess, target)
        total_stats.append(stats)
        print_guess(guess, stats, nonvisual)
        if guess == target:
            print('You win!')
            break
    print()
    return total_stats

def main():
    args = parser.parse_args()

    game_type = '(ad hoc)'
    if args.daily:
        date = datetime.datetime.now()
        game_type = int(f"{int(date.strftime('%Y')) - 2022}{date.strftime('%j')}")
        random.seed(game_type)

    target = random.choice(primes)

    total_stats = game(target, args.only_primes, args.nonvisual)
    print_total_stats(total_stats, game_type)

if __name__ == "__main__":
    main()
