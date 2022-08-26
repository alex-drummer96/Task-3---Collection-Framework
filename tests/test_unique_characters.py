import pytest
from counter_app import number_of_unique_characters as module


def test_cache() -> None:
    cases = [
        '',
        'asdf',
        '@#$;$@',
        '@#$;$@',
        "abbbccdf",
        "abbbccdf",
        'aawwccddd',
        '114jsdksjq wk1'
    ]
    number_of_calls_cache = 2
    for case in cases:
        module.count_unique_characters(string=case)
    assert module.count_unique_characters.cache_info().hits == number_of_calls_cache


@pytest.mark.parametrize('test_input, expected', [
    ('', 0), ('asdf', 4), ('@#$;$@', 2), ("abbbccdf", 3),
    ('aawwccddd', 0), ('114jsdksjq wk1', 5)
])
def test_typical_count_unique_characters(test_input: str, expected: int) -> None:
    assert module.count_unique_characters(test_input) == expected


@pytest.mark.parametrize('test_input', [111, [111, 'dfvjndvj'], {1: 'xcvdfvdf'}])
def test_check_type(test_input: object) -> None:
    with pytest.raises(module.CustomTypeError) as excinfo:
        module.check_type(string=test_input)
    assert f'{type(test_input)} is not allowed. Only string' in str(excinfo.value)
