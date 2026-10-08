import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "tools" / "duct_sizing.py"
SPEC = importlib.util.spec_from_file_location("duct_sizing", MODULE_PATH)
duct_sizing = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(duct_sizing)


class DuctSizingTests(unittest.TestCase):
    def test_reference_case(self):
        diameter, friction, velocity, over = duct_sizing.size_duct(1000)
        self.assertEqual(diameter, 16)
        self.assertAlmostEqual(friction, 0.046, places=3)
        self.assertAlmostEqual(velocity, 716.2, places=1)
        self.assertFalse(over)

    def test_fittings_are_parsed(self):
        self.assertEqual(
            duct_sizing.parse_fittings("elbow_90=2,diffuser=1"),
            [("elbow_90", 2), ("diffuser", 1)],
        )

    def test_invalid_physical_inputs_are_rejected(self):
        for airflow in (0, -1):
            with self.subTest(airflow=airflow):
                with self.assertRaises(ValueError):
                    duct_sizing.size_duct(airflow)
        with self.assertRaises(ValueError):
            duct_sizing.size_duct(1000, target_fr=0)
        with self.assertRaises(ValueError):
            duct_sizing.size_segment("bad", 1000, -1, [])

    def test_invalid_fitting_counts_are_rejected(self):
        for value in ("elbow_90", "elbow_90=x", "elbow_90=-1"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    duct_sizing.parse_fittings(value)


if __name__ == "__main__":
    unittest.main()
