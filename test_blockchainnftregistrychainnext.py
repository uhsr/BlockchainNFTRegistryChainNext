# test_blockchainnftregistrychainnext.py
"""
Tests for BlockchainNFTRegistryChainNext module.
"""

import unittest
from blockchainnftregistrychainnext import BlockchainNFTRegistryChainNext

class TestBlockchainNFTRegistryChainNext(unittest.TestCase):
    """Test cases for BlockchainNFTRegistryChainNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTRegistryChainNext()
        self.assertIsInstance(instance, BlockchainNFTRegistryChainNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTRegistryChainNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
