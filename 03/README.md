# Week 03 - Exponentials and Logarithms

1st October 2021

## Reading Material

- [A Level Maths Tutor - Logarithms](https://www.a-levelmathstutor.com/logarithms.php)
- [Maths Genie - Exponentials and Logs](https://www.mathsgenie.co.uk/as-pure-exponentials-and-logs.html)

## Notation

- Log notation; `log_a(b)` is the logarithm of `b` to the base `a`
- Index notation; `a^b` is `a` to the power of `b`
- The following are equivalent; `log_a(b) = c ≡ a^c = b` 

## Log Laws

- `log_a(x) + log_a(y) = log_a(x.y)`
- `log_a(x) - log_a(y) = log_a(x/y)`
- `log_a(x^k) = k.log_a(x)`

## `e` and `ln`

- The gradient of the line `y = e^x` is `e^x` at any point
- The natural log (`ln`) is the inverse of `e` i.e. `ln(e^x) = x`

## Exercises

There is an environment file in the `03` folder that has the required libraries for the exercises below.

### Log Laws

- In python import the `math` module that comes with base python
- Find the logarithm function in the `math` library
- Check a few values for each law to confirm they hold
- By hand, rearrange `2^(4.x) = 3` for `x`, then calculate `x` in python
- By hand, rearrange `7.log_10(x) = 5` for `x`, then calculate `x` in python

### Exponential graphs

- Plot the following;
  - `y = 2^x`
  - `y = 3^x`
  - `y = 4^x`
  - `y = 2.4^x`
  - `y = (1/3)^x`
  - `y = (1/2)^x`
- Look at the [pandas plot method](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)

### Exponential decay

- Radioactivity of a material decays by 15% a year
- Initial level of radioactivity is 1100
- Find how long it takes for radioactivity level to half

### Log scale

- Show that `y = a.b^x` is equivalent to `log(y) = x.log(b) + log(a)`
- Plot `y = 3.2^x`
- Rearrange `y = 3.2^x` to be of the form `log(y) = x.log(b) + log(a)` and plot the rearranged form on the log scale

### Natural log

- Find the exponetial function in the `math` library
- Plot the following;
  - `y = e^x`
  - `y = e^(-x)`
  - `y = ln(x)`
- Manually calculate the values of the above functions for some very small and very large numbers, both positive and negative

### Exponential growth model

- The size of a population of mice is given by `N = 10.e^(0.03t)` where `t` is the number of days since the start point
- Calculate the population size after 10 days
- Calculate the number of days for the population to reach 1000 individuals

