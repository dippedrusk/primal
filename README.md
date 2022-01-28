# Primal

Quick (one-evening) implementation of Wordle for 5-digit primes in Python, for command-line use.

## Features
- Has a daily version (`--daily` flag) and an ad hoc version (default)
- Has the option to let you only input prime numbers instead of any 5-digit natural numbers (`--only-primes` flag)
- Nonvisual mode for playing without visual cues / with a screenreader (`--nonvisual` flag)
- Generates alt text / image descriptions if you're going to share to Twitter
- Pretty ANSI colours

## How to hack it
Super easy. Read the file with the primes, read the code to see how I'm generating the seed for the daily version, use that and the Python ``random`` module to figure out the target. Et voilà!

## Credits
- The original [Wordle](https://www.powerlanguage.co.uk/wordle/) by Josh Wardle (the thing that started it all)
- Common Lisp [command-line Wordle](https://twitter.com/curtmackevo/status/1479345428286083078) by Curtis Mackie (inspiration to use square brackets for each digit in visual mode)
- [My friend Ellen](https://twitter.com/Starry1086/) for the precursor to the schema used for nonvisual mode
