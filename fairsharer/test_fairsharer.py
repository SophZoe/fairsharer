import pytest

from fair_sharer import fair_sharer

@pytest.mark.parametrize("values, num_iterations, share, expected_result",
                         [([0, 1000, 800, 0], 1, 0.1, [100, 800, 900, 0]),
                          ([0, 1000, 800, 0], 2, 0.1, [100, 890, 720, 90]),
                          ([0, 1000, 800, 0], 3, 0,1, [189, 712, 809, 90])
                          ])

def test_fair_sharer(values, num_iterations, share, expected_result):
    result = fair_sharer(values, num_iteration, share)
    assert result == expected_result