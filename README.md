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

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 1000 executions:

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `solutions/1/1.c.bin` | 0.2 ± 0.0 | 0.1 | 0.5 | 1.04 ± 0.29 |
| `solutions/1/1.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.7 | 1.82 ± 0.49 |
| `java -cp solutions/1 Main` | 16.5 ± 0.3 | 15.9 | 22.4 | 103.19 ± 24.44 |
| `python solutions/1/1.py` | 8.4 ± 0.9 | 7.9 | 15.9 | 52.88 ± 13.81 |
| `node solutions/1/1.js` | 35.0 ± 1.8 | 33.7 | 52.9 | 219.12 ± 52.98 |
| `solutions/2/2.c.bin` | 0.2 ± 0.0 | 0.1 | 0.7 | 1.00 |
| `solutions/2/2.rs.bin` | 0.3 ± 0.0 | 0.2 | 0.9 | 1.68 ± 0.50 |
| `java -cp solutions/2 Main` | 16.4 ± 0.2 | 15.9 | 17.5 | 102.82 ± 24.31 |
| `python solutions/2/2.py` | 8.1 ± 0.8 | 7.8 | 15.9 | 50.97 ± 12.93 |
| `node solutions/2/2.js` | 34.3 ± 1.8 | 33.3 | 60.9 | 214.60 ± 51.93 |
| `solutions/3/3.c.bin` | 0.2 ± 0.0 | 0.2 | 0.5 | 1.20 ± 0.33 |
| `solutions/3/3.rs.bin` | 0.3 ± 0.1 | 0.3 | 0.8 | 1.86 ± 0.54 |
| `java -cp solutions/3 Main` | 16.5 ± 0.3 | 16.0 | 18.4 | 103.58 ± 24.50 |
| `python solutions/3/3.py` | 8.9 ± 1.5 | 8.4 | 17.2 | 55.71 ± 16.20 |
| `node solutions/3/3.js` | 35.1 ± 2.3 | 33.8 | 59.4 | 219.79 ± 53.86 |

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
