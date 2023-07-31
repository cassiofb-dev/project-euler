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
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.2 | 0.4 | 1.22 ± 0.30 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.78 ± 0.24 |
| `java -cp solutions/1 Main` | 16.9 ± 0.3 | 16.3 | 18.0 | 112.00 ± 8.36 |
| `python solutions/1/1.py` | 8.2 ± 0.4 | 8.0 | 10.6 | 54.42 ± 4.60 |
| `node solutions/1/1.js` | 34.5 ± 0.5 | 33.9 | 38.0 | 228.63 ± 16.93 |
| `solutions/2/2.c.bin` | 0.2 ± 0.0 | 0.1 | 0.2 | 1.00 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.70 ± 0.20 |
| `java -cp solutions/2 Main` | 16.7 ± 0.3 | 16.2 | 17.5 | 110.86 ± 8.21 |
| `python solutions/2/2.py` | 8.5 ± 0.6 | 7.9 | 12.0 | 56.32 ± 5.55 |
| `node solutions/2/2.js` | 34.5 ± 1.5 | 33.7 | 48.1 | 228.84 ± 19.23 |
| `solutions/3/3.c.bin` | 0.3 ± 0.0 | 0.2 | 0.4 | 1.69 ± 0.21 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.1 | 0.3 | 0.6 | 2.15 ± 0.42 |
| `java -cp solutions/3 Main` | 16.9 ± 0.3 | 16.4 | 17.7 | 111.96 ± 8.32 |
| `python solutions/3/3.py` | 9.1 ± 0.7 | 8.5 | 12.0 | 60.06 ± 6.31 |
| `node solutions/3/3.js` | 35.8 ± 3.0 | 34.2 | 59.1 | 237.04 ± 26.29 |
| `solutions/4/4.c.bin` | 284.2 ± 4.4 | 278.2 | 312.1 | 1882.77 ± 139.61 |
| `solutions/4/4.rs.bin` | 375.0 ± 9.0 | 352.6 | 395.3 | 2484.19 ± 189.72 |
| `java -cp solutions/4 Main` | 58.1 ± 2.7 | 55.8 | 70.6 | 385.17 ± 33.21 |
| `python solutions/4/4.py` | 174.6 ± 3.2 | 171.8 | 203.5 | 1156.93 ± 86.57 |
| `node solutions/4/4.js` | 311.1 ± 6.2 | 303.9 | 347.1 | 2061.04 ± 155.03 |

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
