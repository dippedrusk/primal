# Primal

Quick (one-evening) implementation of Wordle for 5-digit primes in Python, for command-line use.

![Command line run of the program primal.py with the daily flag. I make 6 guesses, prompted by a "Guess the prime" prompt every time. When I make a guess, I get feedback with similar background colours to the original Wordle - green for correct, yellow for it exists in the number but I have the wrong position, and a white background for a digit not in the answer. My guesses are 10009, 23456, 35678, 56337, 55367, and 57367, my winning guess.](./img/daily_game.png "Daily game of Primal")

## Features
- Has a daily version (`--daily` flag) and an ad hoc version (default)
- Has the option to let you only input prime numbers instead of any 5-digit natural numbers (`--only-primes` flag)
- Nonvisual mode for playing without visual cues / with a screenreader (`--nonvisual` flag)
- Generates alt text / image descriptions if you're going to share to Twitter
- Pretty ANSI colours

## How to hack it
Super easy. Read the file with the primes, read the code to see how I'm generating the seed for the daily version, use that and the Python ``random`` module to figure out the target. Et voilà!

## Gallery

![Alt text generated for the daily game above. The text says: PRIMAL 28 6/6. Line 1: All misses. Line 2: 2 misses (positions 1, 3) and 3 in the wrong position. Line 3: 1 miss (position 5) and 4 in the wrong position. Line 4: 3 hits (positions 1, 3, 5), 1 miss (position 4) and 1 in the wrong position. Line 5: 4 hits (positions 1, 3, 4, 5) and 1 miss. Line 6: Won!](./img/daily_alt.png "Alt text generated for the daily game above")

![Grid generated for the daily game above to show how you did without revealing the actual guesses or the answer. The title says PRIMAL 28 6/6. The character - is used to represent a miss, o for a hit and c for a partial match, i.e., in the wrong position. The background of each letter also has coloured backgrounds as in the main game - yellow, green or white.](./img/daily_grid.png "Grid for the daily game above")

![Game, alt text and grid in nonvisual mode. In nonvisual mode, instead of using digits enclosed in square brackets where only the background colour provides cues as to whether the digit was right or wrong or in the wrong place, characters are used instead. The character - represents a miss, o represents a hit and c represents a partial match, i.e., in the wrong position. There is no background colouring for the feedback on each guess. The alt text and grid are generated in the same way as before. Since this is an ad hoc run the title of the alt text and the generated grid both say PRIMAL (ad hoc) 5/6. My 5 guesses were 18402, 35791, 61761, 11761, and 71761, the winning prime.](./img/nonvisual.png "Ad-hoc game in nonvisual mode")

## Credits
- The original [Wordle](https://www.powerlanguage.co.uk/wordle/) by Josh Wardle (the thing that started it all)
- Common Lisp [command-line Wordle](https://twitter.com/curtmackevo/status/1479345428286083078) by Curtis Mackie (inspiration to use square brackets for each digit in visual mode)
- [My friend Ellen](https://twitter.com/Starry1086/) for the precursor to the schema used for nonvisual mode
