import unittest
from Nuke import launch_Nuke, player_Picker

class TestLaunchNuke(unittest.TestCase):
    def test_launch_nuke(self):
        owner = "Player1"
        nuke = object()
        nuke.totalMoves = 5
        nuke.name = "Nuke"
        nuke.eta = 0
        nuke.xCords = 0
        nuke.yCords = 0
        nuke.numberOfProjectile = 1
        nuke.blastRadius = 5
        nuke.owner = owner

        # Call the function to be tested
        launch_Nuke(nuke, owner)

        # Assert that the nuke object has been updated as expected
        self.assertEqual(nuke.totalMoves, 5)
        self.assertEqual(nuke.name, "Nuke")
        self.assertEqual(nuke.eta, 5)
        # Add more asserts for the rest of the attributes as needed

if __name__ == '__main__':
    unittest.main()