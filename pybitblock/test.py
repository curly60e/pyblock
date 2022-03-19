import unittest
from btcsupply import btcSupplyAtBlock


class Test(unittest.TestCase):

    def testBeginning(self):
        self.assertEqual(btcSupplyAtBlock(0), 50)
        self.assertEqual(btcSupplyAtBlock(1), 100)
        self.assertEqual(btcSupplyAtBlock(2), 150)
        self.assertEqual(btcSupplyAtBlock(3), 200)
        self.assertEqual(btcSupplyAtBlock(4), 250)

    def test1stHalving(self):
        self.assertEqual(btcSupplyAtBlock(209998), 10499950)
        self.assertEqual(btcSupplyAtBlock(209999), 10500000)
        self.assertEqual(btcSupplyAtBlock(210000), 10500025)
        self.assertEqual(btcSupplyAtBlock(210001), 10500050)
        self.assertEqual(btcSupplyAtBlock(210002), 10500075)

    def test2ndHalving(self):
        self.assertEqual(btcSupplyAtBlock(419998), 15749975)
        self.assertEqual(btcSupplyAtBlock(419999), 15750000)
        self.assertEqual(btcSupplyAtBlock(420000), 15750012.5)
        self.assertEqual(btcSupplyAtBlock(420001), 15750025.0)
        self.assertEqual(btcSupplyAtBlock(420002), 15750037.5)

    def test3rdHalving(self):
        self.assertEqual(btcSupplyAtBlock(419998), 15749975)
        self.assertEqual(btcSupplyAtBlock(419999), 15750000)
        self.assertEqual(btcSupplyAtBlock(420000), 15750012.5)
        self.assertEqual(btcSupplyAtBlock(420001), 15750025.0)
        self.assertEqual(btcSupplyAtBlock(420002), 15750037.5)

    def test4thHalving(self):
        self.assertEqual(btcSupplyAtBlock(629998), 18374987.5)
        self.assertEqual(btcSupplyAtBlock(629999), 18375000.0)
        self.assertEqual(btcSupplyAtBlock(630000), 18375006.25)
        self.assertEqual(btcSupplyAtBlock(630001), 18375012.5)
        self.assertEqual(btcSupplyAtBlock(630002), 18375018.75)

    def test5thHalving(self):
        self.assertEqual(btcSupplyAtBlock(839998), 19687493.75)
        self.assertEqual(btcSupplyAtBlock(839999), 19687500.0)
        self.assertEqual(btcSupplyAtBlock(840000), 19687503.125)
        self.assertEqual(btcSupplyAtBlock(840001), 19687506.25)
        self.assertEqual(btcSupplyAtBlock(840002), 19687509.375)

    def testOverTime(self):
        self.assertEqual(btcSupplyAtBlock(10), 550)
        self.assertEqual(btcSupplyAtBlock(100), 5050)
        self.assertEqual(btcSupplyAtBlock(1000), 50050)
        self.assertEqual(btcSupplyAtBlock(10000), 500050)
        self.assertEqual(btcSupplyAtBlock(100000), 5000050)
        self.assertEqual(btcSupplyAtBlock(250000), 11500025.0)
        self.assertEqual(btcSupplyAtBlock(500000), 16750012.5)
        self.assertEqual(btcSupplyAtBlock(750000), 19125006.25)
        self.assertEqual(btcSupplyAtBlock(1000000), 20187503.125)
        self.assertEqual(btcSupplyAtBlock(2500000), 20994384.78851406)

    def testEndOfHalvings(self):
        self.assertEqual(btcSupplyAtBlock(33 * 210000 - 5), 20999999.97689996)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 - 4), 20999999.97689997)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 - 3), 20999999.97689998)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 - 2), 20999999.97689999)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 - 1), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(33 * 210000), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 + 1), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 + 2), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(33 * 210000 + 3), 20999999.9769)

    def testFarInTheFuture(self):
        self.assertEqual(btcSupplyAtBlock(1e7), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(1e10), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(1e25), 20999999.9769)
        self.assertEqual(btcSupplyAtBlock(1e100), 20999999.9769)


if __name__ == "__main__":
    unittest.main()
