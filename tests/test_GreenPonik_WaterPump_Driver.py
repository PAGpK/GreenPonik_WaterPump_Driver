# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest


from GreenPonik_WaterPump_Driver.GreenPonik_WaterPump_Driver import i2c_scanner, pump_run


class TestGreenPonik_WaterPump_Driver(unittest.TestCase):
    def test_i2c_scanner(self):
        self.assertListEqual(i2c_scanner())

    def test_pump_run(self):
        self.assertListEqual(pump_run())


if __name__ == "__main__":
    unittest.main()