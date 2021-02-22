from mlproject.distance import haversine
import numpy as np

def test_distance_type():
    assert type(haversine(38.865, 2.380, 48.235, 2.393)) == np.dtype('float64')
