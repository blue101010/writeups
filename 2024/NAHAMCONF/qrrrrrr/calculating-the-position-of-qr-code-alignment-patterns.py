
def get_alignment_positions(version):
    positions = []
    if version > 1:
        n_patterns = version // 7 + 2
        first_pos = 6
        positions.append(first_pos)
        matrix_width = 17 + 4 * version
        last_pos = matrix_width - 1 - first_pos
        second_last_pos = (
            (first_pos + last_pos * (n_patterns - 2)  # Interpolate end points to get point
            + (n_patterns - 1) // 2)                  # Round to nearest int by adding half
                                                      # of divisor before division
            // (n_patterns - 1)                       # Floor-divide by number of intervals
                                                      # to complete interpolation
            ) & -2                                    # Round down to even integer
        pos_step = last_pos - second_last_pos
        second_pos = last_pos - (n_patterns - 2) * pos_step
        positions.extend(range(second_pos, last_pos + 1, pos_step))
    return positions

for version in range(1, 40 + 1): # 1 to 40 inclusive
    print("V%d: %s" % (version, get_alignment_positions(version)))

def get_alignment_tracks(version):
    if version == 1:
        return []
    
    intervals = version // 7 + 1
    distance = 4 * version + 4  # between first and last pattern
    step = (distance // intervals // 2 + 1) * 2
    
    return [6] + [distance + 6 - (intervals - 1 - i) * step for i in range(intervals)]


for version in range(1, 40 + 1): # 1 to 40 inclusive
    print("V%d: %s" % (version, get_alignment_tracks(version)))

