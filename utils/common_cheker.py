import allure
from deepdiff import DeepDiff


@allure.step('Check the difference between objects')
def check_difference_between_objects(actual_result, expected_result, exclude_paths: str | list[str] = None) -> None:
    comparison_data = (actual_result, expected_result)
    diff = DeepDiff(*comparison_data, ignore_order=True)
    assert not diff