#!/usr/bin/env python3

import pytest
from ament_pep257.main import main


@pytest.mark.linter
@pytest.mark.pep257
def test_pep257():
    rc = main(argv=[])
    assert rc == 0, 'Found code style errors / warnings'
