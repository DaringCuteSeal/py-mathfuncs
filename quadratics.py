import math
import colorama
from typing import Callable

# Helpers
class Result:
    """
    Result class for calculation results.
    """
    def __init__(self, value: any, human_readable_str: str):
        self.value = value
        self.readable = human_readable_str

    def __repr__(self):
        return f"{colorama.Fore.CYAN}{self.readable}{colorama.Fore.RESET}"

def format_coefficient(coefficient):
    """
    Turn `5` to `+ 5`, -5 to `- 5`, and `1` to nothing.
    """
    if coefficient == 1:
        return ""
    elif coefficient > 0:
        return f"+ {coefficient}"
    elif coefficient < 0:
        return f"- {abs(coefficient)}"

# Actually useful functions
def discriminant(a, b, c):
    """
    Find discriminant from given a, b, and c.
    """
    return b ** 2 - 4 * a * c

def find_roots(a: float, b: float, c: float) -> Result:
    """
    Get factors from given a, b, and c.
    """
    if discriminant(a, b, c) < 0:
        return Result(None, "No real roots")

    result1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
    result2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
    return Result((result1, result2), f"x = {result1} or x = {result2}")

def crossing_x_axis(a: float, b: float, c: float) -> Result:
    """
    Find x in `f(x) = 0`.
    """
    result = find_roots(a, b, c).value
    if result is not None:
        return Result(result, f"x = {result[0]} or x = {result[1]}")
    else:
        return Result(None, f"no real roots")

def crossing_y_axis(a: float, b: float, c: float) -> Result:
    """
    Find y in `f(0) = y`.
    """
    return Result(c, f"f(0) = {c}")

def symmetry(a: float, b: float, c: float) -> Result:
    """
    Find the symmetry point from given a, b, and c.
    """

    result = (-b) / (2*a)
    return Result(result, f"x = {result}")

def optimum(a: float, b: float, c: float) -> Result:
    """
    Find the optimum (max/min) value from given a, b, and c.

    """
    result = -discriminant(a, b, c) / (4 * a)
    if a < 0:
        optimum_type = "maximum"
    elif a > 0:
        optimum_type = "minimum"
    else:
        optimum_type = "no real roots"

    return Result(result, f"optimum: {result} ({optimum_type})")

def peak_point(a: float, b: float, c: float) -> Result:
    """
    Find the peak point from given a, b, and c.
    """

    result = (symmetry(a, b, c).value, optimum(a, b, c).value)
    return Result(result, f"peak point: ({result[0]}, {result[1]})")


def find_function_from_peak_point(peak_point: tuple[float, float], arb_point: tuple[float, float]) -> Result:
    """
    Find the function from given peak point and an arbitrary point.
    """
    a = float((arb_point[1] - peak_point[1]) / ((arb_point[0] ** 2) - (2 * arb_point[0] * peak_point[0]) + (peak_point[0])**2)) # derived from the f(x) = a(x - xp) + yp thing
    a = int(a) if a.is_integer() else a

    b = float(a * 2 * -peak_point[0])
    b = int(b) if b.is_integer() else b

    c = float((a * (peak_point[0] ** 2)) + peak_point[1])
    c = int(c) if c.is_integer() else c

    a_str = str(a).strip("1") if abs(a) == 1 else a 
    b_str = format_coefficient(b)
    c_str = format_coefficient(c)

    return Result(f"{a_str}x² {b_str}x {c_str}", f"f(x) = {a_str}x² {b_str}x {c_str}")

def find_function_from_crossing_x(crossing_x_points: tuple[float, float], arb_point: tuple[float, float]) -> Result:
    a = float(arb_point[1] / ((arb_point[0] - crossing_x_points[0]) * (arb_point[0] - crossing_x_points[1])))
    a = int(a) if a.is_integer() else a

    b = float((a * -crossing_x_points[1]) + (a * -crossing_x_points[0]))
    b = int(b) if b.is_integer() else b

    c = float(a * -crossing_x_points[0] * -crossing_x_points[1])
    c = int(c) if c.is_integer() else c

    a_str = str(a).strip("1") if abs(a) == 1 else a 
    b_str = format_coefficient(b)
    c_str = format_coefficient(c)

    return Result(f"{a_str}x² {b_str}x {c_str}", f"f(x) = {a_str}x² {b_str}x {c_str}")

__all__ = ["Result", "discriminant", "find_roots", "crossing_x_axis", "crossing_y_axis", "symmetry", "optimum", "peak_point", "find_function_from_peak_point", "find_function_from_crossing_x"]
