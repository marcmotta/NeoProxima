# test_neoproxima.py
"""
Tests for NeoProxima module.
"""

import unittest
from neoproxima import NeoProxima

class TestNeoProxima(unittest.TestCase):
    """Test cases for NeoProxima class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoProxima()
        self.assertIsInstance(instance, NeoProxima)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoProxima()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
