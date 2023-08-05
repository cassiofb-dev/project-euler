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
7. What is the 10,001st prime number?
8. Find the thirteen adjacent digits in the $1000$-digit number that have the greatest product. What is the value of this product?

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

Notes:

- On question 4 the results are strange because I did unholy string manipulation

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.1 | 0.2 | 1.10 ± 0.18 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.5 | 1.84 ± 0.30 |
| `java -cp solutions/1 Main` | 17.0 ± 0.2 | 16.6 | 18.0 | 112.07 ± 10.53 |
| `python solutions/1/1.py` | 8.5 ± 1.1 | 8.0 | 15.6 | 56.18 ± 8.88 |
| `node solutions/1/1.js` | 34.7 ± 2.1 | 33.7 | 52.3 | 229.57 ± 25.41 |
| `solutions/2/2.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.14 ± 0.17 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.1 | 0.2 | 0.6 | 2.12 ± 0.40 |
| `java -cp solutions/2 Main` | 16.9 ± 0.3 | 16.2 | 18.1 | 111.54 ± 10.60 |
| `python solutions/2/2.py` | 8.6 ± 1.0 | 7.8 | 15.5 | 57.03 ± 8.56 |
| `node solutions/2/2.js` | 35.3 ± 2.7 | 33.5 | 48.6 | 233.34 ± 28.28 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.19 ± 0.16 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.5 | 1.92 ± 0.30 |
| `java -cp solutions/3 Main` | 17.0 ± 0.2 | 16.3 | 17.6 | 112.10 ± 10.53 |
| `python solutions/3/3.py` | 9.1 ± 1.2 | 8.5 | 18.0 | 60.25 ± 9.64 |
| `node solutions/3/3.js` | 34.5 ± 0.5 | 33.9 | 37.9 | 228.30 ± 21.48 |
| `solutions/4/4.c.bin` | 282.4 ± 2.1 | 279.2 | 291.3 | 1867.05 ± 173.89 |
| `solutions/4/4.rs.bin` | 373.3 ± 8.4 | 354.0 | 394.0 | 2468.21 ± 235.82 |
| `java -cp solutions/4 Main` | 56.9 ± 1.1 | 55.4 | 64.0 | 376.29 ± 35.73 |
| `python solutions/4/4.py` | 176.6 ± 2.0 | 172.9 | 182.0 | 1167.41 ± 109.20 |
| `node solutions/4/4.js` | 309.6 ± 5.1 | 304.0 | 343.4 | 2047.19 ± 193.10 |
| `solutions/4/4_optimized.c.bin` | 21.9 ± 2.7 | 20.8 | 40.5 | 144.93 ± 22.21 |
| `solutions/5/5.c.bin` | 0.2 ± 0.0 | 0.1 | 0.3 | 1.08 ± 0.19 |
| `solutions/5/5.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.79 ± 0.22 |
| `java -cp solutions/5 Main` | 17.0 ± 0.4 | 16.5 | 19.9 | 112.56 ± 10.79 |
| `python solutions/5/5.py` | 8.2 ± 0.5 | 8.0 | 11.4 | 54.31 ± 6.05 |
| `node solutions/5/5.js` | 34.5 ± 1.2 | 33.7 | 42.9 | 228.23 ± 22.53 |
| `solutions/6/6.c.bin` | 0.2 ± 0.0 | 0.1 | 0.2 | 1.00 |
| `solutions/6/6.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.81 ± 0.30 |
| `java -cp solutions/6 Main` | 16.9 ± 0.3 | 16.3 | 17.8 | 111.64 ± 10.53 |
| `python solutions/6/6.py` | 9.6 ± 2.9 | 7.9 | 15.8 | 63.68 ± 20.19 |
| `node solutions/6/6.js` | 34.5 ± 0.8 | 33.7 | 39.3 | 227.89 ± 21.89 |
| `solutions/7/7.c.bin` | 12.7 ± 1.4 | 10.2 | 16.6 | 84.17 ± 12.14 |
| `solutions/7/7.rs.bin` | 36.2 ± 2.5 | 34.8 | 54.3 | 239.51 ± 27.64 |
| `java -cp solutions/7 Main` | 26.2 ± 0.7 | 25.5 | 30.7 | 173.27 ± 16.78 |
| `python solutions/7/7.py` | 67.7 ± 2.5 | 66.6 | 91.2 | 447.90 ± 44.81 |
| `node solutions/7/7.js` | 43.7 ± 1.2 | 42.7 | 51.3 | 289.11 ± 27.98 |
| `solutions/8/8.c.bin` | 0.2 ± 0.0 | 0.2 | 0.5 | 1.26 ± 0.27 |
| `solutions/8/8.rs.bin` | 76.3 ± 1.5 | 75.0 | 83.1 | 504.70 ± 47.89 |
| `java -cp solutions/8 Main` | 21.0 ± 0.3 | 20.3 | 21.9 | 138.62 ± 13.05 |
| `python solutions/8/8.py` | 10.4 ± 1.8 | 9.6 | 20.4 | 68.62 ± 13.26 |
| `node solutions/8/8.js` | 36.2 ± 1.6 | 35.1 | 50.7 | 239.12 ± 24.60 |

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
