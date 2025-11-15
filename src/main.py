from typing import Final

NUMBER_OF_ROWS: Final[int] = 5
NUMBER_OF_COLUMNS: Final[int] = 5


def create_grid() -> list[list[int]]:
    listCol = [0 for x in range(NUMBER_OF_COLUMNS)]
    listRow = [listCol for y in range(NUMBER_OF_ROWS)]        

    return listRow
