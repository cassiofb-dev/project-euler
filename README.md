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

> [!WARNING]
> This repository will only cover the first 100 problems implementations and the others in benchmarks only. Please try to solve them yourself before searching for solutions. Also keep in mind that most of my solutions are the first thing I thought and they can be highly inefficient and be solved in another ways.

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
9. There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

Notes:

- On question 4 the results are strange because I did unholy string manipulation

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.1 | 0.2 | 1.00 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.7 | 1.83 ± 0.33 |
| `java -cp solutions/1 Main` | 16.7 ± 0.2 | 16.2 | 17.6 | 105.66 ± 7.86 |
| `python solutions/1/1.py` | 8.4 ± 0.5 | 7.9 | 11.2 | 52.87 ± 5.01 |
| `node solutions/1/1.js` | 35.2 ± 2.0 | 33.9 | 52.4 | 222.27 ± 20.51 |
| `solutions/2/2.c.bin` | 0.2 ± 0.1 | 0.1 | 0.7 | 1.24 ± 0.41 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.67 ± 0.23 |
| `java -cp solutions/2 Main` | 16.7 ± 0.3 | 16.1 | 18.4 | 105.79 ± 7.97 |
| `python solutions/2/2.py` | 8.3 ± 0.8 | 7.7 | 15.0 | 52.20 ± 6.48 |
| `node solutions/2/2.js` | 34.2 ± 0.7 | 33.5 | 37.3 | 216.26 ± 16.36 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.4 | 1.27 ± 0.23 |
| `solutions/3/3.rs.bin` | 0.4 ± 0.1 | 0.3 | 0.7 | 2.27 ± 0.55 |
| `java -cp solutions/3 Main` | 16.9 ± 0.4 | 16.2 | 18.3 | 106.66 ± 8.28 |
| `python solutions/3/3.py` | 9.1 ± 1.1 | 8.4 | 17.4 | 57.61 ± 8.36 |
| `node solutions/3/3.js` | 35.2 ± 3.0 | 33.8 | 56.7 | 222.23 ± 24.82 |
| `solutions/4/4.c.bin` | 281.8 ± 4.9 | 278.0 | 316.5 | 1781.25 ± 133.66 |
| `solutions/4/4.rs.bin` | 372.2 ± 9.7 | 348.5 | 393.8 | 2352.71 ± 182.31 |
| `java -cp solutions/4 Main` | 57.1 ± 1.5 | 55.0 | 67.2 | 360.81 ± 27.89 |
| `python solutions/4/4.py` | 175.7 ± 1.8 | 172.4 | 182.0 | 1110.49 ± 81.81 |
| `node solutions/4/4.js` | 308.1 ± 2.5 | 304.2 | 321.1 | 1947.35 ± 142.98 |
| `solutions/4/4_optimized.c.bin` | 20.9 ± 0.1 | 20.7 | 21.1 | 132.15 ± 9.65 |
| `solutions/5/5.c.bin` | 0.2 ± 0.0 | 0.2 | 0.4 | 1.12 ± 0.23 |
| `solutions/5/5.rs.bin` | 0.3 ± 0.1 | 0.2 | 0.4 | 1.86 ± 0.38 |
| `java -cp solutions/5 Main` | 16.9 ± 0.5 | 16.2 | 18.8 | 106.79 ± 8.32 |
| `python solutions/5/5.py` | 8.5 ± 0.6 | 8.0 | 11.2 | 53.64 ± 5.59 |
| `node solutions/5/5.js` | 34.1 ± 0.5 | 33.5 | 37.8 | 215.68 ± 16.04 |
| `solutions/6/6.c.bin` | 0.2 ± 0.0 | 0.1 | 0.6 | 1.04 ± 0.32 |
| `solutions/6/6.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.5 | 1.98 ± 0.33 |
| `java -cp solutions/6 Main` | 16.6 ± 0.2 | 16.2 | 17.2 | 105.06 ± 7.80 |
| `python solutions/6/6.py` | 8.3 ± 0.5 | 7.8 | 10.7 | 52.16 ± 4.78 |
| `node solutions/6/6.js` | 34.5 ± 0.9 | 33.5 | 38.6 | 218.12 ± 16.90 |
| `solutions/7/7.c.bin` | 12.7 ± 1.4 | 9.6 | 16.2 | 80.12 ± 10.83 |
| `solutions/7/7.rs.bin` | 35.5 ± 1.1 | 34.3 | 40.2 | 224.57 ± 17.81 |
| `java -cp solutions/7 Main` | 25.9 ± 0.8 | 25.2 | 32.1 | 163.49 ± 12.92 |
| `python solutions/7/7.py` | 67.5 ± 0.7 | 66.8 | 70.9 | 426.83 ± 31.45 |
| `node solutions/7/7.js` | 43.9 ± 2.5 | 42.3 | 65.9 | 277.29 ± 25.53 |
| `solutions/8/8.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.24 ± 0.18 |
| `solutions/8/8.rs.bin` | 76.2 ± 3.6 | 74.9 | 100.1 | 481.72 ± 41.72 |
| `java -cp solutions/8 Main` | 20.7 ± 0.5 | 20.0 | 24.3 | 130.58 ± 10.02 |
| `python solutions/8/8.py` | 10.1 ± 0.9 | 9.6 | 17.1 | 63.83 ± 7.56 |
| `node solutions/8/8.js` | 35.9 ± 1.2 | 34.8 | 43.9 | 226.69 ± 18.21 |
| `solutions/9/9.c.bin` | 1.6 ± 0.0 | 1.6 | 1.8 | 10.34 ± 0.79 |
| `solutions/9/9.rs.bin` | 2.6 ± 0.5 | 2.3 | 4.3 | 16.74 ± 3.50 |
| `java -cp solutions/9 Main` | 21.0 ± 0.4 | 20.3 | 22.9 | 132.60 ± 9.93 |
| `python solutions/9/9.py` | 24.4 ± 0.7 | 23.8 | 27.7 | 154.36 ± 11.99 |
| `node solutions/9/9.js` | 37.6 ± 1.6 | 36.6 | 50.1 | 237.44 ± 20.19 |

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
