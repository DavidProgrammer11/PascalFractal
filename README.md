# 🔺 PascalFractal

A Python tool for generating and visualizing **Pascal's Triangle** and the **Sierpiński Triangle** fractal pattern, including diagonal sequence extraction via the hockey stick identity.

No external dependencies — just Python 3 and the built-in `math` module.

---

## Features

- **Pascal's Triangle** — Generate and display any number of rows with centered terminal output
- **Sierpiński Triangle** — Derived from Pascal's triangle using `C(n,k) mod 5`, producing a fractal pattern
- **Diagonal Generator** — Extract diagonal sequences using the identity `C(n+i, i)`

---

## How It Works

### Mode 0 — Pascal's Triangle

Each entry is the binomial coefficient `C(n, k) = n! / (k! × (n−k)!)`. Rows are computed and centered for terminal display.

### Mode 1 — Sierpiński Triangle

Each binomial coefficient is reduced `mod 2`. Values equal to `0` become a space; all other values become `1`. This creates a self-similar fractal pattern:

| `C(n,k) mod 2` | Display |
|:-:|:-:|
| `0` | ` ` (space) |
| `1` | `1` |

### Diagonal Generator

Uses the identity `C(n+i, i)` to extract the diagonal sequence starting at row `n` for `l` elements.

---

## Usage

```python
# Generate a diagonal sequence starting at row 5, length 7
print(generate_diagonal(5, 7))
# [1, 6, 21, 56, 126, 252, 462]

# Display Pascal's Triangle (20 rows)
draw_triangle(create(20, mode=0))

# Display Sierpiński Triangle (10 rows)
draw_triangle(create(10, mode=1))
```

---

## Function Reference

| Function | Description |
|---|---|
| `binomial(n, k, mode)` | Computes `C(n,k)`. `mode=0` returns the integer value; `mode=1` returns display value based on `C(n,k) % 5` |
| `generate_diagonal(n, l)` | Returns `l` binomial coefficients along the diagonal starting at `C(n, 0)` |
| `create(rows, mode)` | Builds the full triangle as a list of rows. `mode=0` = Pascal, `mode=1` = Sierpiński |
| `draw_triangle(row_list)` | Prints the triangle centered in the console and resets internal state |

---

## Example Output

**Pascal's Triangle — `create(20, mode=0)`**

```
                                                                         1
                                                                        1  1
                                                                      1  2  1
                                                                     1  3  3  1
                                                                   1  4  6  4  1
                                                                 1  5  10  10  5  1
                                                               1  6  15  20  15  6  1
                                                             1  7  21  35  35  21  7  1
                                                           1  8  28  56  70  56  28  8  1
                                                        1  9  36  84  126  126  84  36  9  1
                                                   1  10  45  120  210  252  210  120  45  10  1
                                                 1  11  55  165  330  462  462  330  165  55  11  1
                                              1  12  66  220  495  792  924  792  495  220  66  12  1
                                          1  13  78  286  715  1287  1716  1716  1287  715  286  78  13  1
                                      1  14  91  364  1001  2002  3003  3432  3003  2002  1001  364  91  14  1
                                  1  15  105  455  1365  3003  5005  6435  6435  5005  3003  1365  455  105  15  1
                             1  16  120  560  1820  4368  8008  11440  12870  11440  8008  4368  1820  560  120  16  1
                         1  17  136  680  2380  6188  12376  19448  24310  24310  19448  12376  6188  2380  680  136  17  1
                     1  18  153  816  3060  8568  18564  31824  43758  48620  43758  31824  18564  8568  3060  816  153  18  1
                 1  19  171  969  3876  11628  27132  50388  75582  92378  92378  75582  50388  27132  11628  3876  969  171  19  1
```

**Sierpiński Triangle — `create(20, mode=1)`**

```
                                        1
                                      1  1
                                     1     1
                                   1  1  1  1
                                  1           1
                                1  1        1  1
                               1     1     1     1
                             1  1  1  1  1  1  1  1
                            1                       1
                          1  1                    1  1
                         1     1                 1     1
                       1  1  1  1              1  1  1  1
                      1           1           1           1
                    1  1        1  1        1  1        1  1
                   1     1     1     1     1     1     1     1
                 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
                1                                               1
              1  1                                            1  1
             1     1                                         1     1
           1  1  1  1                                      1  1  1  1
```

---

## Requirements

- Python 3.x
- No external dependencies

---

## Notes

- `triangle` is a global list that resets after each `draw_triangle()` call. Always call `draw_triangle()` before calling `create()` again, or the rows will accumulate.
- For large row counts (500+), computation may be slow due to exact factorial arithmetic. Consider adding `@lru_cache` to `binomial()` for better performance.

---

## License

[MIT](LICENSE) — free to use, modify, and distribute.
