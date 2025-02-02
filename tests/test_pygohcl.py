import pytest
import pygohcl


def test_basic():
    assert pygohcl.loads('variable "test" {}') == {"variable": {"test": {}}}


def test_parse_error():
    with pytest.raises(pygohcl.HCLParseError):
        pygohcl.loads('variable "test {}')


def test_empty_list():
    out = pygohcl.loads(
        """variable "test" {
    default = []
    }"""
    )
    assert out["variable"]["test"]["default"] == []


def test_null():
    out = pygohcl.loads(
        """variable "test" {
    default = null
    }"""
    )
    assert out["variable"]["test"]["default"] is None


def test_value_is_null():
    with pytest.raises(pygohcl.HCLInternalError):
        pygohcl.loads(
            """resource "datadog_synthetics_test" "status_check_api" {
                message = <<-EOT
                    ${local.is_production_env ? "prod" : null}
                EOT
            }"""
        )
