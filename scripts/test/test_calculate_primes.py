import pytest

import scripts.calculate_primes


@pytest.mark.parametrize(
    "number,is_prime", [(1, True), (2, True), (3, True), (4, False)]
)
def test_calculate_primes(number, is_prime):
    assert scripts.calculate_primes.checking_primes(number) == is_prime

