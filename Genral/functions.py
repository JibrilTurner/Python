
import unittest

from Nuke import player_One_Choice, launch_Nuke,player_Picker,projectile

def test_player_One_Choice():
    # Test scenario 1
    expected_output = 1
    actual_output = player_One_Choice()
    assert actual_output == expected_output, f"Expected {expected_output} but got {actual_output}"

