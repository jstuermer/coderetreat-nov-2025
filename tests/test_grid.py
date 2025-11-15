from src.main import NUMBER_OF_COLUMNS, NUMBER_OF_ROWS, create_grid


def test_create_grid() -> None:
    # ACT
    grid = create_grid()

    # ASSERT
    assert len(grid) == NUMBER_OF_ROWS
    for column in grid:
        assert len(column) == NUMBER_OF_COLUMNS
