from typing import Final
from typing import Callable
from typing import TypeAlias
from math import log


GAMMA: Final[float] = 0.5772156649015328606065120900824
RealFunction: TypeAlias = Callable[[float], float]


class LiIsNotDefinedIn1(Exception):
    pass


class DerivativeOfLiIsNotDefinedIn1(Exception):
    pass


def approximate_li_for_small_input(x: float, precision: int = 30) -> float:
    if x == 1:
        raise LiIsNotDefinedIn1
    u: float = log(x)
    solution: float = GAMMA + log(abs(u))
    factorial = power = 1
    for current_num in range(1, precision):
        factorial *= current_num
        power *= u
        solution += power / (current_num * factorial)
    return solution


def derivative_of_li(x: float) -> float:
    if x == 1:
        raise DerivativeOfLiIsNotDefinedIn1
    return 1 / log(x)


def approximate_rs_constant(
    first_guess: float = 1.5,
    precision: int = 30,
    li: RealFunction = approximate_li_for_small_input,
    d_li: RealFunction = derivative_of_li,
) -> float:
    current_point: float = first_guess
    for _ in range(precision):
        if current_point == 1:
            eg = ExceptionGroup(
                "Both functions are undefined in 1",
                [LiIsNotDefinedIn1(1), DerivativeOfLiIsNotDefinedIn1(2)],
            )
            raise eg
        current_point -= li(current_point) / d_li(current_point)
    return current_point


def main(*args, **kwargs) -> None:
    import logging

    logging.basicConfig(level=logging.INFO)
    logging.info(approximate_rs_constant())


if __name__ == "__main__":
    """Approximating the Ramanujan-Soldner constant via Newton's method using the li function and its derivative."""
    main()
