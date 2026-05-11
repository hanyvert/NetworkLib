# test_networklib.py
"""
Tests for NetworkLib module.
"""

import unittest
from networklib import NetworkLib

class TestNetworkLib(unittest.TestCase):
    """Test cases for NetworkLib class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NetworkLib()
        self.assertIsInstance(instance, NetworkLib)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NetworkLib()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
