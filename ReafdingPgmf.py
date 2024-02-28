def read_pgm(pgm):
    header = pgm.readline().decode().strip()
    assert header == "P5"
    (width, height) = [int(i) for i in pgm.readline().split()]
    depth = int(pgm.readline())
    assert depth <= 255

    data = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(ord(pgm.read(1)))
        data.append(row)
    return data


with open('F:\\pattern\\data\\s1\\1.pgm', 'rb') as pgm_file:
    raster_data = read_pgm(pgm_file)
flatten_vector = [pixel for row in raster_data for pixel in row]
