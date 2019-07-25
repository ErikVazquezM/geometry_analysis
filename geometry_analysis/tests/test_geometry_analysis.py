"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys

import numpy as np
import math

@pytest.fixture()
def water_molecule():
    name = "water"
    symbols = ["H", "O", "H"]
    coordinates = np.array([[2,0,0], [0,0,0], [-2,0,0]])

    water = geometry_analysis.Molecule(name, symbols, coordinates)
    
    return water

def test_molecules_set_coordinates(water_molecule):
    """Test bond list is rebuilt when we reset coordinates """

    num_bonds = len(water_molecule.bonds)

    assert num_bonds == 2

    new_coordinates = np.array([[5,0,0], [0,0,0], [-2,0,0]])

    water_molecule.coordinates = new_coordinates

    new_bonds = len(water_molecule.bonds)

    assert new_bonds == 1
    assert np.array_equal(new_coordinates, water_molecule.coordinates)

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

def test_calculate_distance():
    """Test the calculate_distance function"""

    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])

    expected_distance = np.sqrt(2)

    calculated_distance = geometry_analysis.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle_180():
    """Test the calculate_distance function"""

    r1 = np.array([-1,0,0])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])

    expected_theta = math.pi

    calculated_theta = geometry_analysis.calculate_angle(r1, r2, r3)

    assert expected_theta == calculated_theta

def test_calculate_angle_90():
    """Test the calculate_distance function"""

    r1 = np.array([1,0,0])
    r2 = np.array([0,0,0])
    r3 = np.array([0,1,0])

    expected_theta = (math.pi) / 2

    calculated_theta = geometry_analysis.calculate_angle(r1, r2, r3)

    assert expected_theta == calculated_theta

@pytest.mark.parametrize('p1, p2, p3, expected_angle', [
    (np.array([-1,0,0]), np.array([0,0,0]), np.array([1,0,0]), 180),
    (np.array([1,0,0]), np.array([0,0,0]), np.array([0,1,0]), 90),
    ])
def test_calculate_angle(p1, p2, p3, expected_angle):
    calculated_theta = geometry_analysis.calculate_angle(p1, p2, p3, expected_angle)
    assert expected_angle == calculated_theta

