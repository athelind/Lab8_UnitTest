import unittest
import Lab8 as prog

class TestMyProgram(unittest.TestCase):

    def test_EngineType(self):
        print("Testing Begins..")
        vios = prog.Vehicle("4", "petrol", 5, 180)
        self.assertEqual(vios.type_of_tank, "xxxx")

if __name__ == "__main__":
    unittest.main()