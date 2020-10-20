import os
import unittest

from numpy import genfromtxt
import matplotlib.pyplot as plt
from thornpy.signal import manually_clean_sig

TEST_SPIKE_DATA = os.path.join('test', 'files', 'spike.csv')

class Test_ManuallyCleanSig(unittest.TestCase):

    def setUp(self):
        return

    def test_manually_clean_sig_with_y(self):
        data = genfromtxt(TEST_SPIKE_DATA, delimiter=',', names=True)
        
        x = data['time']
        y = data['stress']

        y = manually_clean_sig(x, y, print_debug=True)

        _, ax = plt.subplots()
        
        ax.plot(x, y)
        ax.grid()
        ax.set_title('Cleaned Signal')
        plt.show()

        self.assertEqual(y[1443], -176000.0)

    def test_manually_clean_sig_return_indices(self):
        data = genfromtxt(TEST_SPIKE_DATA, delimiter=',', names=True)
        
        x = data['time']
        y = data['stress']

        y, i = manually_clean_sig(x, y, print_debug=True, indices=True)

        _, ax = plt.subplots()
        
        ax.plot(x, y)
        ax.grid()
        ax.set_title('Cleaned Signal')
        plt.show()

        self.assertListEqual(i, [1443])

    def tearDown(self):
        return