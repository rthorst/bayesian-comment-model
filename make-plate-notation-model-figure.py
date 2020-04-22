import daft
from matplotlib import rc 

# Instantiate probablistic graphical model (PGM)
pgm = daft.PGM()

# params.
top_y = 1.75
bottom_y = 0.5
left_x = 0.5
right_x = 2


# Nodes.
pgm.add_node("lambda", r"$\lambda_k$", left_x, top_y)
pgm.add_node("p", r"P", right_x, top_y)
pgm.add_node("d", r"$D_i$", left_x, bottom_y)
pgm.add_node("z", r"$z_i$", right_x, bottom_y)

# Edges.
pgm.add_edge("lambda", "d")
pgm.add_edge("p", "z")
pgm.add_edge("z", "d")

# Plates. [x-start, y-start, x-length, y-length]
pgm.add_plate(plate=[left_x - 0.35, top_y - 0.6, 1.05, 1], label="K=1,2", label_offset=(25, 0))
pgm.add_plate(plate=[left_x - 0.35, bottom_y - 0.5, 2.5, 1], label=r"$M = 1, \cdots, N$", label_offset = (75,0))

# Show.
pgm.render()
pgm.savefig("model-plate-diagram.png")

