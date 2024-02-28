import numpy as np

from ReafdingPgmf import read_pgm

all_flatten_vectors = []
for i in range(1, 41):
    for j in range(1, 11):
        file_path = f'F:\\pattern\\data\\s{i}\\{j}.pgm'
        with open(file_path, 'rb') as pgm_file:
            raster_data = read_pgm(pgm_file)
        flatten_vector = [pixel for row in raster_data for pixel in row]
        all_flatten_vectors.append(flatten_vector)

D = np.array(all_flatten_vectors)
y = np.array([i for i in range(1, 41) for _ in range(10)])
print("Shape of D:", D.shape)
print("Shape of y:", y.shape)
