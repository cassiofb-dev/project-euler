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

Run in your terminal ``docker compose up -d``. You can check the results on the file ``run_solutions.txt`` created on root directory or inside the programs directory with a txt file created for each program.

To use it without docker make sure you have installed the programs in the section [credits](#credits) and run ``python run_solutions.py``.

A benchmark can be produced with ``python run_solutions.py benchmark`` the result file will be ``run_solutions.md`` in root directory.

## Problems

1. Find the sum of all the multiples of $3$ or $5$ below $1000$.
2. By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
3. What is the largest prime factor of the number $600851475143$?
4. Find the largest palindrome made from the product of two $3$-digit numbers.
5. What is the smallest positive number that is evenly divisible by all of the numbers from $1$ to $20$?
6. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
7. What is the $10\,001$st prime number?

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

Notes:

- On question 4 the results are strange because I did unholy string manipulation

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.16 ± 0.14 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.6 | 1.79 ± 0.27 |
| `java -cp solutions/1 Main` | 16.9 ± 0.2 | 16.4 | 17.5 | 113.53 ± 10.43 |
| `python solutions/1/1.py` | 8.6 ± 1.4 | 8.0 | 16.4 | 58.06 ± 10.82 |
| `node solutions/1/1.js` | 34.5 ± 1.9 | 33.7 | 51.0 | 231.80 ± 24.79 |
| `solutions/2/2.c.bin` | 0.2 ± 0.0 | 0.2 | 0.2 | 1.16 ± 0.14 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.1 | 0.2 | 0.6 | 2.01 ± 0.48 |
| `java -cp solutions/2 Main` | 16.8 ± 0.2 | 16.5 | 17.3 | 113.31 ± 10.38 |
| `python solutions/2/2.py` | 8.5 ± 0.6 | 7.9 | 11.0 | 57.16 ± 6.40 |
| `node solutions/2/2.js` | 34.6 ± 1.9 | 33.7 | 48.5 | 232.95 ± 24.84 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.4 | 1.20 ± 0.17 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.6 | 1.98 ± 0.38 |
| `java -cp solutions/3 Main` | 16.8 ± 0.2 | 16.3 | 17.6 | 113.25 ± 10.41 |
| `python solutions/3/3.py` | 8.8 ± 0.4 | 8.5 | 11.1 | 59.06 ± 5.93 |
| `node solutions/3/3.js` | 34.4 ± 1.4 | 33.6 | 47.7 | 231.58 ± 23.14 |
| `solutions/4/4.c.bin` | 281.5 ± 1.4 | 277.9 | 284.7 | 1893.35 ± 172.23 |
| `solutions/4/4.rs.bin` | 374.4 ± 9.3 | 352.5 | 393.7 | 2518.09 ± 237.12 |
| `java -cp solutions/4 Main` | 56.7 ± 0.8 | 55.2 | 60.2 | 381.50 ± 35.04 |
| `python solutions/4/4.py` | 174.1 ± 1.4 | 172.3 | 178.1 | 1171.27 ± 106.82 |
| `node solutions/4/4.js` | 307.2 ± 3.7 | 303.5 | 338.6 | 2066.53 ± 189.32 |
| `solutions/4/4_optimized.c.bin` | 21.3 ± 1.2 | 20.9 | 32.8 | 143.49 ± 15.33 |
| `solutions/5/5.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.20 ± 0.22 |
| `solutions/5/5.rs.bin` | 0.3 ± 0.1 | 0.2 | 0.5 | 2.10 ± 0.44 |
| `java -cp solutions/5 Main` | 16.8 ± 0.3 | 16.2 | 18.0 | 113.00 ± 10.43 |
| `python solutions/5/5.py` | 8.8 ± 1.0 | 8.0 | 14.8 | 59.41 ± 8.82 |
| `node solutions/5/5.js` | 34.2 ± 0.4 | 33.6 | 37.0 | 230.21 ± 21.06 |
| `solutions/6/6.c.bin` | 0.1 ± 0.0 | 0.1 | 0.2 | 1.00 |
| `solutions/6/6.rs.bin` | 0.3 ± 0.1 | 0.2 | 0.7 | 1.85 ± 0.41 |
| `java -cp solutions/6 Main` | 16.7 ± 0.2 | 16.4 | 17.6 | 112.59 ± 10.34 |
| `python solutions/6/6.py` | 8.1 ± 0.4 | 7.9 | 11.3 | 54.81 ± 5.64 |
| `node solutions/6/6.js` | 34.6 ± 1.8 | 33.5 | 47.0 | 232.94 ± 24.43 |
| `solutions/7/7.c.bin` | 13.3 ± 1.7 | 10.2 | 17.6 | 89.19 ± 13.74 |
| `solutions/7/7.rs.bin` | 35.9 ± 2.9 | 34.5 | 55.7 | 241.80 ± 29.47 |
| `java -cp solutions/7 Main` | 26.0 ± 0.4 | 25.3 | 27.1 | 174.78 ± 16.14 |
| `python solutions/7/7.py` | 67.4 ± 1.1 | 66.7 | 77.3 | 453.49 ± 41.91 |
| `node solutions/7/7.js` | 43.5 ± 1.8 | 42.4 | 57.9 | 292.79 ± 29.09 |

## Credits

Thanks for these awesome open source projects bellow:

- [Hyperfine](https://github.com/sharkdp/hyperfine)
- [Docker](https://github.com/docker)
- [NodeJS](https://github.com/nodejs)
- [Python](https://github.com/python)
- [Java](https://github.com/openjdk/jdk)
- [Rust](https://github.com/rust-lang/rust)
- [GCC](https://github.com/gcc-mirror/gcc)

## License

MIT

---

> [Website](https://cassio-souza.pages.dev/) &nbsp;&middot;&nbsp;
> GitHub [@cassiofb-dev](https://github.com/cassiofb-dev) &nbsp;&middot;&nbsp;
> Twitter [@cassiofb_dev](https://twitter.com/cassiofb_dev)
