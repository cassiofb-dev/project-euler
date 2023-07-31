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

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

Notes:

- On question 4 the results are strange because I did unholy string manipulation

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.04 ± 0.25 |
| `solutions/1/1.rs.bin` | 0.4 ± 0.0 | 0.3 | 0.6 | 2.25 ± 0.46 |
| `java -cp solutions/1 Main` | 16.7 ± 0.3 | 16.2 | 17.7 | 95.32 ± 16.93 |
| `python solutions/1/1.py` | 8.5 ± 1.0 | 8.0 | 12.1 | 48.33 ± 10.29 |
| `node solutions/1/1.js` | 36.4 ± 4.9 | 34.2 | 61.5 | 207.87 ± 46.06 |
| `solutions/2/2.c.bin` | 0.2 ± 0.0 | 0.1 | 0.3 | 1.00 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.4 | 1.58 ± 0.31 |
| `java -cp solutions/2 Main` | 16.5 ± 0.2 | 16.1 | 17.4 | 94.42 ± 16.74 |
| `python solutions/2/2.py` | 8.3 ± 1.1 | 7.9 | 15.6 | 47.58 ± 10.54 |
| `node solutions/2/2.js` | 34.9 ± 2.1 | 33.8 | 47.8 | 199.31 ± 37.22 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.3 | 1.02 ± 0.20 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.0 | 0.3 | 0.4 | 1.61 ± 0.31 |
| `java -cp solutions/3 Main` | 16.8 ± 0.3 | 16.3 | 18.8 | 95.84 ± 17.02 |
| `python solutions/3/3.py` | 8.8 ± 0.9 | 8.4 | 16.2 | 50.09 ± 10.17 |
| `node solutions/3/3.js` | 35.0 ± 2.3 | 33.9 | 49.6 | 200.01 ± 37.69 |
| `solutions/4/4.c.bin` | 281.9 ± 1.7 | 278.3 | 286.2 | 1609.14 ± 284.52 |
| `solutions/4/4.rs.bin` | 376.0 ± 9.2 | 354.7 | 400.0 | 2145.88 ± 382.79 |
| `java -cp solutions/4 Main` | 56.5 ± 0.7 | 54.5 | 59.2 | 322.44 ± 57.12 |
| `python solutions/4/4.py` | 175.4 ± 1.7 | 172.3 | 182.2 | 1001.25 ± 177.20 |
| `node solutions/4/4.js` | 308.9 ± 4.5 | 303.3 | 346.5 | 1763.28 ± 312.64 |
| `solutions/4/4_optimized.c.bin` | 21.1 ± 0.7 | 20.8 | 25.8 | 120.52 ± 21.66 |

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
