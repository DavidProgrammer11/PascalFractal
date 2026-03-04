# PascalFractal
# 🔺 Pascal's Triangle & Sierpiński Triangle Generator

A Python implementation for generating and visualizing **Pascal's Triangle** and the **Sierpiński Triangle** fractal pattern, with support for diagonal sequence generation.

---

## Features

- **Pascal's Triangle** — Generate and display any number of rows
- **Sierpiński Triangle** — Derived from Pascal's triangle using modular arithmetic (mod 5), with custom symbol mapping
- **Diagonal Generator** — Extract diagonal sequences from Pascal's triangle using the hockey stick identity
- Configurable display modes for both numeric and symbolic output

---

## How It Works

### Pascal's Triangle
Each entry is a binomial coefficient `C(n, k) = n! / (k! * (n-k)!)`. Rows are computed and centered for display.

### Sierpiński Triangle (mode 1)
Each binomial coefficient is taken `mod 5` and mapped to a symbol:

| Value (mod 5) | Symbol |
|:-:|:-:|
| 0 | ` ` (space) |
| 1 | `+` |
| 2 | `Ç` |
| 3 | `´´` |
| 4 | `1` |

This produces a fractal-like pattern reminiscent of the classic Sierpiński triangle.

### Diagonal Generator
Uses the identity `C(n+i, i)` to produce the diagonal sequence starting at row `n`, for `l` elements.

---

## Usage

```python
from math import factorial

# Generate a diagonal sequence starting at row 5, length 6
print(generate_diagonal(5, 6))

# Display Pascal's Triangle with 30 rows
draw_triangle(create(30, mode=0))

# Display Sierpiński Triangle with 70 rows
draw_triangle(create(70, mode=1))
```

### Function Reference

| Function | Description |
|---|---|
| `binomio(n, k, mode)` | Computes `C(n,k)`. `mode=0` returns the integer; `mode=1` returns a symbol based on `C(n,k) % 5` |
| `generate_diagonal(n, l)` | Returns a list of `l` binomial coefficients along the diagonal starting at `C(n,0)` |
| `create(rows, mode)` | Builds the triangle as a list of rows up to `rows`. `mode=0` = Pascal, `mode=1` = Sierpiński |
| `draw_triangle(row_list)` | Prints the triangle centered in the console |

---

## Requirements

- Python 3.x
- No external dependencies — only the built-in `math` module is used

---

## Example Output

**Pascal's Triangle (5 rows):**
```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
```

**Sierpiński Triangle (symbolic, 10 rows):**
```
+
+ +
+ Ç +
+ ++ ++
+    +    +
...
```

---

## Notes

- `triangle` is used as a global list that gets reset after each `draw_triangle()` call. If you plan to generate multiple triangles in sequence, make sure to call `draw_triangle()` between each `create()` call.
- For very large row counts (e.g. 1000+), computation may be slow due to exact factorial arithmetic.

---

## License

MIT License — feel free to use, modify, and distribute.
