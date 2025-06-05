def calculate_fibonacci(n):
  """Calculates the nth Fibonacci number.

  Args:
    n: A non-negative integer.

  Returns:
    The nth Fibonacci number.

  Raises:
    ValueError: If n is negative.
  """
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  elif n <= 1:
    return n
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

if __name__ == "__main__":
  import argparse
  import sys

  parser = argparse.ArgumentParser(description="Calculate Fibonacci numbers.")
  parser.add_argument("n", type=int, help="The Fibonacci number to calculate (must be a non-negative integer).")

  args = parser.parse_args()

  try:
    result = calculate_fibonacci(args.n)
    print(result)
  except ValueError as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
