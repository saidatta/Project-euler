# const int gridSize = 20;
# long[,] grid = new long[gridSize+1, gridSize+1];
#
# //Initialise the grid with boundary conditions
# for (int i = 0; i < gridSize; i++) {
#     grid[i, gridSize] = 1; grid[gridSize,i] = 1;
# }
#
# for (int i = gridSize - 1; i >= 0; i--) {
# for (int j = gridSize - 1; j >= 0; j--) {
# grid[i, j] = grid[i+1, j] + grid[i, j+1];
# }
# }

gridSize = 20
inner_grid = [0] * (gridSize+1)
grid = [inner_grid] * (gridSize+1)

# intialize boundaries
for x in range (0, gridSize):
    grid[x][gridSize], grid[gridSize][x] = 1, 1

for i in range(gridSize - 1, -1, -1):
    for j in range(gridSize - 1, -1, -1):
        grid[i][j] = grid[i + 1][j] + grid[i][j+1]

print(grid[0][0])