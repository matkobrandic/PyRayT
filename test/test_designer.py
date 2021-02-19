import unittest
import pyrayt.designer as designer
import pyrayt.simple_cg as cg

class TestAnalyticSystem(unittest.TestCase):
    def setUp(self):
        self.system = designer.AnalyticSystem()

    def test_calling_dict_fields(self):
        # the three default fields should be created with the object
        default_keys = ("sources", "components", "detectors")
        system_keys = self.system.keys()
        for key in default_keys:
            self.assertTrue(key in system_keys)
            self.assertTrue(isinstance(self.system[key], cg.ObjectGroup))

    def test_adding_to_system_fields(self):
        # we should be able to add to the dictionary field
        my_object = cg.WorldObject()
        my_object.move(3, 0, 0)

        self.system["components"].append(my_object)
        self.assertEqual(self.system["components"][0], my_object)

    def test_flatten_system(self):
        self.system["sources"].append(0)
        self.system["sources"].append((1, (2, 3)))
        self.system["components"].append((4, 5, 6))
        self.system["detectors"].append(7)
        flattened = self.system.flatten()
        for n,field in enumerate(flattened):
            self.assertEqual(n,field)


if __name__ == '__main__':
    unittest.main()
