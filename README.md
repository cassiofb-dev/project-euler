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

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

Notes:

- On question 4 the results are strange because I did unholy string manipulation

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.2 | 0.2 | 1.00 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.5 | 1.59 ± 0.27 |
| `java -cp solutions/1 Main` | 16.8 ± 0.2 | 16.4 | 17.5 | 97.28 ± 6.01 |
| `python solutions/1/1.py` | 8.6 ± 1.4 | 7.9 | 16.6 | 49.91 ± 8.43 |
| `node solutions/1/1.js` | 34.1 ± 0.4 | 33.6 | 36.8 | 198.32 ± 12.23 |
| `solutions/2/2.c.bin` | 0.2 ± 0.1 | 0.2 | 0.6 | 1.27 ± 0.37 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.58 ± 0.25 |
| `java -cp solutions/2 Main` | 16.7 ± 0.2 | 16.2 | 17.3 | 97.06 ± 6.02 |
| `python solutions/2/2.py` | 8.4 ± 0.9 | 7.8 | 15.4 | 48.87 ± 5.78 |
| `node solutions/2/2.js` | 34.4 ± 2.0 | 33.4 | 47.5 | 199.99 ± 16.98 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.08 ± 0.13 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.1 | 0.3 | 0.8 | 1.88 ± 0.40 |
| `java -cp solutions/3 Main` | 16.8 ± 0.7 | 16.2 | 21.4 | 97.63 ± 7.06 |
| `python solutions/3/3.py` | 9.1 ± 0.7 | 8.4 | 12.4 | 53.00 ± 5.36 |
| `node solutions/3/3.js` | 35.1 ± 2.3 | 33.8 | 52.4 | 203.84 ± 18.17 |
| `solutions/4/4.c.bin` | 282.3 ± 4.1 | 278.2 | 309.4 | 1639.56 ± 102.15 |
| `solutions/4/4.rs.bin` | 372.7 ± 8.5 | 354.1 | 397.4 | 2164.83 ± 140.19 |
| `java -cp solutions/4 Main` | 56.9 ± 1.7 | 54.6 | 67.6 | 330.47 ± 22.42 |
| `python solutions/4/4.py` | 175.4 ± 3.1 | 172.8 | 202.3 | 1018.45 ± 64.20 |
| `node solutions/4/4.js` | 307.2 ± 4.5 | 299.2 | 339.1 | 1783.99 ± 111.25 |
| `solutions/4/4_optimized.c.bin` | 20.9 ± 0.1 | 20.8 | 21.1 | 121.50 ± 7.37 |
| `solutions/5/5.c.bin` | 0.2 ± 0.0 | 0.2 | 0.4 | 1.02 ± 0.15 |
| `solutions/5/5.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.6 | 1.70 ± 0.31 |
| `java -cp solutions/5 Main` | 16.6 ± 0.3 | 16.2 | 17.7 | 96.67 ± 6.04 |
| `python solutions/5/5.py` | 8.4 ± 0.9 | 7.9 | 16.0 | 49.01 ± 5.89 |
| `node solutions/5/5.js` | 34.1 ± 1.4 | 33.2 | 47.7 | 198.16 ± 14.50 |
| `solutions/6/6.c.bin` | 0.2 ± 0.0 | 0.1 | 0.3 | 1.05 ± 0.17 |
| `solutions/6/6.rs.bin` | 0.3 ± 0.1 | 0.2 | 0.7 | 1.68 ± 0.32 |
| `java -cp solutions/6 Main` | 16.6 ± 0.2 | 16.1 | 17.1 | 96.42 ± 5.98 |
| `python solutions/6/6.py` | 8.0 ± 0.8 | 7.7 | 15.5 | 46.57 ± 5.25 |
| `node solutions/6/6.js` | 34.4 ± 2.4 | 33.6 | 57.4 | 199.98 ± 18.39 |

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
