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
| `solutions/1/1.c.bin` | 0.3 ± 0.1 | 0.3 | 0.7 | 1.04 ± 0.28 |
| `solutions/1/1.rs.bin` | 0.5 ± 0.0 | 0.4 | 0.7 | 1.60 ± 0.35 |
| `java -cp solutions/1 Main` | 23.6 ± 0.3 | 23.1 | 25.4 | 77.59 ± 14.92 |
| `python solutions/1/1.py` | 11.2 ± 1.7 | 10.0 | 19.3 | 36.74 ± 8.99 |
| `node solutions/1/1.js` | 45.5 ± 0.9 | 44.5 | 48.1 | 149.77 ± 28.86 |
| `solutions/2/2.c.bin` | 0.3 ± 0.1 | 0.3 | 0.7 | 1.00 |
| `solutions/2/2.rs.bin` | 0.5 ± 0.1 | 0.4 | 1.1 | 1.74 ± 0.51 |
| `java -cp solutions/2 Main` | 23.7 ± 0.7 | 23.0 | 28.8 | 77.81 ± 15.09 |
| `python solutions/2/2.py` | 10.6 ± 0.8 | 9.9 | 13.6 | 34.79 ± 7.18 |
| `node solutions/2/2.js` | 45.8 ± 1.3 | 44.7 | 54.4 | 150.60 ± 29.21 |
| `solutions/3/3.c.bin` | 0.3 ± 0.0 | 0.3 | 0.5 | 1.14 ± 0.24 |
| `solutions/3/3.rs.bin` | 0.5 ± 0.0 | 0.4 | 0.7 | 1.64 ± 0.34 |
| `java -cp solutions/3 Main` | 23.9 ± 0.5 | 23.3 | 26.1 | 78.55 ± 15.16 |
| `python solutions/3/3.py` | 11.0 ± 0.6 | 10.6 | 13.9 | 36.30 ± 7.22 |
| `node solutions/3/3.js` | 45.8 ± 0.7 | 44.9 | 48.3 | 150.56 ± 28.96 |
| `solutions/4/4.c.bin` | 284.6 ± 3.3 | 281.0 | 313.4 | 935.94 ± 179.82 |
| `solutions/4/4.rs.bin` | 375.8 ± 9.3 | 353.6 | 412.0 | 1236.04 ± 239.00 |
| `java -cp solutions/4 Main` | 67.2 ± 1.7 | 65.0 | 79.4 | 221.07 ± 42.77 |
| `python solutions/4/4.py` | 178.3 ± 1.6 | 174.9 | 182.3 | 586.40 ± 112.58 |
| `node solutions/4/4.js` | 331.7 ± 2.3 | 323.6 | 337.6 | 1090.87 ± 209.34 |
| `solutions/4/4_optimized.c.bin` | 23.5 ± 4.6 | 21.0 | 36.9 | 77.24 ± 21.14 |
| `solutions/5/5.c.bin` | 0.3 ± 0.1 | 0.3 | 0.6 | 1.00 ± 0.27 |
| `solutions/5/5.rs.bin` | 0.5 ± 0.1 | 0.4 | 0.7 | 1.63 ± 0.36 |
| `java -cp solutions/5 Main` | 23.8 ± 0.5 | 23.2 | 26.7 | 78.38 ± 15.13 |
| `python solutions/5/5.py` | 10.7 ± 1.4 | 10.1 | 21.3 | 35.22 ± 8.26 |
| `node solutions/5/5.js` | 46.4 ± 1.9 | 44.6 | 59.7 | 152.56 ± 29.94 |
| `solutions/6/6.c.bin` | 0.4 ± 0.1 | 0.3 | 0.7 | 1.31 ± 0.31 |
| `solutions/6/6.rs.bin` | 0.5 ± 0.0 | 0.4 | 0.7 | 1.54 ± 0.33 |
| `java -cp solutions/6 Main` | 23.7 ± 0.4 | 23.1 | 26.5 | 77.96 ± 15.02 |
| `python solutions/6/6.py` | 10.6 ± 1.2 | 9.9 | 19.6 | 34.75 ± 7.79 |
| `node solutions/6/6.js` | 47.1 ± 4.0 | 44.7 | 74.4 | 154.82 ± 32.46 |
| `solutions/7/7.c.bin` | 14.4 ± 2.1 | 10.0 | 19.0 | 47.26 ± 11.38 |
| `solutions/7/7.rs.bin` | 40.7 ± 1.2 | 39.5 | 48.2 | 133.69 ± 25.97 |
| `java -cp solutions/7 Main` | 35.4 ± 3.9 | 32.6 | 45.8 | 116.54 ± 25.72 |
| `python solutions/7/7.py` | 70.7 ± 2.5 | 69.5 | 93.2 | 232.36 ± 45.32 |
| `node solutions/7/7.js` | 57.2 ± 2.8 | 55.1 | 75.7 | 188.25 ± 37.28 |
| `solutions/8/8.c.bin` | 0.3 ± 0.1 | 0.3 | 0.7 | 1.14 ± 0.32 |
| `solutions/8/8.rs.bin` | 76.4 ± 1.9 | 75.7 | 93.7 | 251.17 ± 48.58 |
| `java -cp solutions/8 Main` | 28.3 ± 0.5 | 27.7 | 30.3 | 93.21 ± 17.96 |
| `python solutions/8/8.py` | 12.1 ± 0.6 | 11.7 | 14.8 | 39.74 ± 7.84 |
| `node solutions/8/8.js` | 48.7 ± 3.5 | 46.3 | 63.0 | 160.31 ± 32.86 |
| `solutions/9/9.c.bin` | 1.8 ± 0.1 | 1.7 | 2.0 | 5.80 ± 1.12 |
| `solutions/9/9.rs.bin` | 3.0 ± 0.5 | 2.5 | 4.9 | 9.71 ± 2.44 |
| `java -cp solutions/9 Main` | 28.3 ± 0.8 | 27.4 | 32.4 | 93.04 ± 18.04 |
| `python solutions/9/9.py` | 27.4 ± 3.6 | 26.0 | 50.4 | 90.07 ± 20.91 |
| `node solutions/9/9.js` | 49.6 ± 1.7 | 48.0 | 58.9 | 163.25 ± 31.81 |
| `solutions/10/10.c.bin` | 26.9 ± 2.7 | 23.6 | 37.0 | 88.46 ± 19.14 |
| `solutions/10/10.rs.bin` | 107.7 ± 1.6 | 104.2 | 118.6 | 354.21 ± 68.15 |
| `java -cp solutions/10 Main` | 40.1 ± 1.8 | 38.5 | 54.4 | 131.84 ± 25.98 |
| `python solutions/10/10.py` | 199.5 ± 3.0 | 192.6 | 210.4 | 656.06 ± 126.21 |
| `node solutions/10/10.js` | 77.4 ± 2.8 | 74.4 | 93.6 | 254.53 ± 49.67 |

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
