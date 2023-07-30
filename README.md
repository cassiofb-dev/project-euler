<h1 align="center">
  Project Euler
</h1>

<h4 align="center">Solutions for Project Euler</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#usage">Usage</a> •
  <a href="#problems">Problems</a> •
  <a href="#benchmarks">Benchmarks</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## About

This repository contains my solutions for [Project Euler](https://projecteuler.net/). I'll try to solve them on more than one programming language to improve and keep my problem solving and programming skills.

## Usage

Run in your terminal ``docker compose up -d``. You can check the results on the file ``results.txt`` created on root directory or inside the programs directory with a txt file created for each program.

To use it without docker make sure you have installed the programs in the section [credits](#credits) and run ``python run_solutions.py``.

A benchmark can be produced with ``python run_solutions.py benchmark`` the result file will be ``run_solutions.md`` in root directory.

## Problems

1. Find the sum of all the multiples of $3$ or $5$ below $1000$.
2. By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
3. What is the largest prime factor of the number $600851475143$?

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 10 warmups and 100 executions:

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `src/1/1.c.bin` | 0.2 ± 0.0 | 0.1 | 0.2 | 1.00 |
| `python src/1/1.py` | 8.6 ± 0.5 | 8.1 | 10.8 | 56.45 ± 4.06 |
| `node src/1/1.js` | 34.9 ± 1.9 | 33.4 | 45.2 | 230.54 ± 16.28 |
| `src/2/2.c.bin` | 0.2 ± 0.0 | 0.1 | 0.3 | 1.16 ± 0.25 |
| `python src/2/2.py` | 8.3 ± 0.6 | 7.8 | 10.7 | 54.82 ± 4.59 |
| `node src/2/2.js` | 34.0 ± 0.8 | 33.2 | 38.3 | 224.34 ± 11.47 |
| `src/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.2 | 1.14 ± 0.07 |
| `python src/3/3.py` | 9.0 ± 0.5 | 8.6 | 12.0 | 59.44 ± 4.30 |
| `node src/3/3.js` | 35.2 ± 2.6 | 33.6 | 50.7 | 232.57 ± 20.48 |

## Credits

Thanks for these awesome open source projects bellow:

- [Docker](https://github.com/docker)
- [NodeJS](https://github.com/nodejs)
- [Python](https://github.com/python)
- [GCC](https://github.com/gcc-mirror/gcc)
- [Hyperfine](https://github.com/sharkdp/hyperfine)

## License

MIT
