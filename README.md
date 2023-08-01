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

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

Notes:

- On question 4 the results are strange because I did unholy string manipulation

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.1 | 0.3 | 1.30 ± 0.26 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.5 | 1.79 ± 0.32 |
| `java -cp solutions/1 Main` | 16.7 ± 0.2 | 16.2 | 17.3 | 108.46 ± 16.43 |
| `python solutions/1/1.py` | 8.5 ± 1.1 | 7.9 | 15.3 | 55.37 ± 10.96 |
| `node solutions/1/1.js` | 35.9 ± 2.3 | 34.1 | 46.3 | 233.62 ± 38.21 |
| `solutions/2/2.c.bin` | 0.2 ± 0.0 | 0.1 | 0.3 | 1.07 ± 0.21 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.5 | 1.73 ± 0.36 |
| `java -cp solutions/2 Main` | 16.7 ± 0.2 | 16.2 | 17.4 | 108.46 ± 16.42 |
| `python solutions/2/2.py` | 8.2 ± 0.6 | 7.8 | 11.1 | 53.09 ± 8.87 |
| `node solutions/2/2.js` | 34.5 ± 1.7 | 33.8 | 50.8 | 224.90 ± 35.69 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.2 | 1.16 ± 0.19 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.6 | 1.87 ± 0.36 |
| `java -cp solutions/3 Main` | 16.7 ± 0.3 | 16.3 | 18.2 | 108.84 ± 16.54 |
| `python solutions/3/3.py` | 8.8 ± 0.5 | 8.4 | 11.7 | 57.49 ± 9.28 |
| `node solutions/3/3.js` | 36.0 ± 2.5 | 34.5 | 48.5 | 234.36 ± 39.04 |
| `solutions/4/4.c.bin` | 281.2 ± 1.6 | 278.2 | 287.7 | 1831.53 ± 276.34 |
| `solutions/4/4.rs.bin` | 376.9 ± 9.6 | 354.3 | 403.3 | 2454.82 ± 375.40 |
| `java -cp solutions/4 Main` | 56.6 ± 1.0 | 54.9 | 61.3 | 368.34 ± 55.94 |
| `python solutions/4/4.py` | 176.0 ± 1.7 | 172.1 | 180.7 | 1146.20 ± 173.19 |
| `node solutions/4/4.js` | 308.1 ± 3.0 | 303.6 | 328.9 | 2006.93 ± 303.24 |
| `solutions/4/4_optimized.c.bin` | 21.1 ± 0.4 | 20.9 | 24.9 | 137.65 ± 20.91 |
| `solutions/5/5.c.bin` | 0.2 ± 0.0 | 0.1 | 0.4 | 1.00 |
| `solutions/5/5.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.3 | 1.70 ± 0.27 |
| `java -cp solutions/5 Main` | 16.6 ± 0.2 | 16.2 | 17.3 | 107.99 ± 16.35 |
| `python solutions/5/5.py` | 8.3 ± 0.7 | 8.0 | 11.6 | 54.22 ± 9.33 |
| `node solutions/5/5.js` | 35.9 ± 3.7 | 34.3 | 59.9 | 233.51 ± 42.74 |

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
