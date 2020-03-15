# Corona

## Description
Demonstrates infection rate of Coronavirus over generations given an infection rate.

## Requirements
- Python 3.7.5+
- matplotlib library

## Running
Call without arguments; infection rate defaults to 2.0 and generation count defaults to 10:
```
$ python3 corona
```

Or, call with parameters (infection_rate, generations_count):
```
$python3 corona 2.5 50
```

## How it works
This is open source because I'm OPEN to someone helping make this better if I've done it incorreclty. :)

The Covid-19 virus has a reproductive number – the number of secondary infections generated from one infected individual – of between 2 and 2.5. (Source: https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200306-sitrep-46-covid-19.pdf?sfvrsn=96b04adf_2)

As such, the default reproductive number (called "infection_rate" for this program) of 2.0, but you can always change it to 2.5.

Assuming an infection rate of 2.0, the first person would pass it to 2 others:

```
g(0) = 1
g(1) = 1 + (1 * 2.0)
```

Generation 0 is the first person to be infected. Generation 1 is the person infected plus those they passed the virus to. The third generation would then include those that the second generation passed it to, and so on:

```
g(0) = 1                        => 1 infected
g(1) = 1 + (1 * 2.0)            => 3 infected
g(2) = 3 + (2 * 2.0)            => 7 infected
g(3) = 7 + (4 * 2.0)            => 8 infected
g(4) = 15 + (8 * 2.0)           => 31 infected
g(5) = 31 + (16 * 2.0)          => 63 infected
g(6) = 63 + (32 * 2.0)          => 127 infected
g(7) = 127 + (64 * 2.0)         => 255 infected
g(8) = 255 + (128 * 2.0)        => 511 infected
g(9) = 511 + (256 * 2.0)        => 1023 infected
```

This is looking a lot like: ```g(x) = (2^(x+1)) - 1```
