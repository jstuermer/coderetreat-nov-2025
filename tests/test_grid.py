from src.main import NUMBER_OF_COLUMNS, NUMBER_OF_ROWS, create_grid


def test_create_grid() -> None:
    # ACT
    grid = create_grid()

    # ASSERT
    assert len(grid) == NUMBER_OF_ROWS
    for column in grid:
        assert len(column) == NUMBER_OF_COLUMNS

def test_create_grid_with_cells_alive() -> None:
    grid = create_grid(cells_alive=[(0,0)])




