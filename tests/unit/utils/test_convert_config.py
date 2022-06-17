import os
import pytest
import unittest

from gcp_airflow_foundations.common.utils.convert_config import (
    convert_template_extra_options
)
from gcp_airflow_foundations.base_class.source_template_config import SourceTemplateConfig

class TestConvertConfig(unittest.TestCase):
    def setUp(self):
        mock_template_config = SourceTemplateConfig()
        mock_template_config.extra_options = {"test_config_1": {"test_param_1": ["TEST_VAL_1", "TEST_VAL_2"], "test_param_2": "TEST"}}
        mock_template_config.iterable_options = []
        self.convert_config = convert_template_extra_options

    def test_convert_config(self):
        assert (
            self.convert_config(self.mock_template_config, 0)
            == {"test_param_1": "TEST_VAL_1", "test_param_2": "TEST"}
        )
        assert (
            self.convert_config(self.mock_template_config, 1)
            == {"test_param_1": "TEST_VAL_2", "test_param_2": "TEST"}
        )