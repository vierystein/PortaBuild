# test_portabuild.py
"""
Tests for PortaBuild module.
"""

import unittest
from portabuild import PortaBuild

class TestPortaBuild(unittest.TestCase):
    """Test cases for PortaBuild class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortaBuild()
        self.assertIsInstance(instance, PortaBuild)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortaBuild()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
