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

Each binomial coefficient is reduced `mod 5`. Values equal to `0` become a space; all other values become `1`. This creates a self-similar fractal pattern:

| `C(n,k) mod 2` | Display |
|:-:|:-:|
| `0` | ` ` (space) |
| `0-1` | `1` |

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

**Pascal's Triangle — `create(5, mode=0)`**

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

**Sierpiński Triangle — `create(8, mode=1)`**

```
1
1 1
1   1
1 1 1 1
1       1
1 1     1 1
1   1   1   1
1 1 1 1 1 1 1 1
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
