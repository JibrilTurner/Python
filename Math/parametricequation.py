import math

# y is verical 
def parametricEqu(startPos, endPos, angle):
    x0, y0, z0 = startPos
    x1, y1, z1 = endPos
    # calculates the initial velocity and angle(Radiens) Dont feel like converting to degrees 
    vx = math.sqrt((x1 - x0) * 9.81 / (2 * math.sin(math.pi / angle))) 
    vy = vx * math.sin(math.pi / angle)

    # calculate time of flight
    t = (x1 - x0) / vx

    # calculate y coordinates for each time step
    steps = 4  # number of time steps
    dt = t / steps
    y_coords = []
    z_coords = []
    traj_coords = []
    for i in range(steps + 1):
        t_i = i * dt
        y = y0 + vy * t_i - 0.5 * 9.81 * t_i ** 2
        y_coords.append(y)
        z = z0 + (z1 - z0) * t_i / t
        z_coords.append(z)

        # store current (x, y, z) coordinates in traj_coords array
        x = x0 + i * (x1 - x0) / steps
        traj_coords.append((round(x, 2), round(y, 2), round(z, 2)))

    return traj_coords

traj_coords = parametricEqu((0, 0, 0), (5150, 30, 4500), 2.09)
for x in range(0,5,1):
    print(traj_coords[x])