import math

import numpy as np
import pytest

from import_monster import methods_importer


class TestImportMonster:
    @pytest.mark.parametrize(
        "test_case,expected_result",
        [
            (("pi", [np, math]), []),
            (("e", [np, math]), []),
        ],
    )
    def test_not_return_not_callable(self, test_case, expected_result):
        assert list(methods_importer(*test_case)) == expected_result

    @pytest.mark.parametrize(
        "test_case,expected_result",
        [
            (("sum", [np, math]), 1),
            (("exp", [np, math]), 2),
        ],
    )
    def test_return_callable(self, test_case, expected_result):
        assert len(methods_importer(*test_case)) == expected_result

    @pytest.mark.parametrize(
        "test_case,expected_result",
        [
            (("some_strange_name", [np, math]), []),
            (("exp_", [np, math]), []),
        ],
    )
    def test_not_found(self, test_case, expected_result):
        assert list(methods_importer(*test_case)) == expected_result

    @pytest.mark.parametrize(
        "test_case,expected_result",
        [
            (("sum", [np.sum]), TypeError),
            (("exp", [np.exp, math.exp]), TypeError),
        ],
    )
    def test_not_module_or_string(self, test_case, expected_result):
        with pytest.raises(TypeError):
            methods_importer(*test_case)
