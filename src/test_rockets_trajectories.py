from math import *
import rocket_trajectories
import unittest
sputnik_lift_off_mass_negative = ['Sputnik', 1957, 'USSR', 'LEO orbit', 2, 30.0, -280.0, 83.6, 19.6, 3.0, 3890, 250, 168.0, 39.6, 6.4, 2.95, 970, 240, 99, 92]
theta = pi/3
sputnik_s1_m0_negative = ['Sputnik', 1957, 'USSR', 'LEO orbit', 2, 30.0, -280.0, 83.6, 19.6, 3.0, 3890, 250, -168.0, 39.6, 6.4, 2.95, 970, 240, 99, 92]

sputnik_s1_mp_negative = ['Sputnik', 1957, 'USSR', 'LEO orbit', 2, 30.0,280.0, 83.6, 19.6, 3.0, 3890, 250,-168.0, -39.6, 6.4, 2.95, 970, 240, 99, 92]
sputnik_s1_mp_huge = ['Sputnik', 1957,'USSR', 'LEO orbit', 2, 30.0,280.0,83.6, 19.6, 3.0, 3890, 250, 168.0, 239.6, 6.4, 2.95, 970, 240, 99, 92]
sputnik_s2_m0_negative = ['Sputnik', 1957, 'USSR', 'LEO orbit', 2, 30.0, 280.0, 83.6, 19.6, 3.0, 3890, 250, 168.0, 39.6, 6.4, 2.95, 970, 240, -99, 92]
sputnik_s2_mp_negative = ['Sputnik', 1957, 'USSR', 'LEO orbit', 2, 30.0, 280.0, 83.6, 19.6, 3.0, 3890, 250, 168.0, 39.6, 6.4, 2.95, 970, 240, 99, -92]
sputnik_s2_mp_huge = ['Sputnik', 1957, 'USSR', 'LEO orbit', 2, 30.0, 280.0, 83.6, 19.6, 3.0, 3890, 250, 168.0, 39.6, 6.4, 2.95, 970, 240, 99, 192]



class TestTrajectories(unittest.TestCase):
    def test_negative_lift_off_mass(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages,sputnik_lift_off_mass_negative,theta)
    def test_negative_s_1_m0(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages,sputnik_s1_m0_negative,theta)

    def test_negative_s_1_mp(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages,sputnik_s1_mp_negative,theta)

    def test_huge_s_1_mp(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages,sputnik_s1_mp_huge, theta)

    def test_negative_s_2_m0(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages, sputnik_s2_m0_negative, theta)

    def test_negative_s_2_mp(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages, sputnik_s2_mp_negative, theta)

    def test_huge_s_2_mp(self):
        self.assertRaises(rocket_trajectories.Badvalue, rocket_trajectories.trajectoire_2_etages, sputnik_s2_mp_huge, theta)

if __name__ == '__main__' :
    unittest.main()
