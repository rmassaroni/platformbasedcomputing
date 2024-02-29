var sol =
   [[0, 7, 0, 2, 3, 8, 0, 0, 0],
    [0, 0, 0, 7, 4, 0, 8, 0, 9],
    [0, 6, 8, 1, 0, 9, 0, 0, 2],
    [0, 3, 5, 4, 0, 0, 0, 0, 8],
    [6, 0, 7, 8, 0, 2, 5, 0, 1],
    [8, 0, 0, 0, 0, 5, 7, 6, 0],
    [2, 0, 0, 6, 0, 3, 1, 9, 0],
    [7, 0, 9, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 9, 7, 4, 0, 8, 0]];

/* printBoard is the only function you need to implement.
  The values of the sudoku puzzle above should be displayed in the table in index.html
  Modify the DOM using JavaScript. Notice each <td> has an id. 
  The value at sol[0][0] should go in <td id="r11">. 
  The value at sol[0][1] should go in <td id="r12"> and so on...
  Loop through the two-dimensional array sol above and place each value in a <td> 
  element.
  */

var printBoard = function () {
   
    
};

//Check if value is in the row
var isInRow = function(row, number) {    
    for (var col = 0; col < 9; col++) {
        if (sol[row][col] == number) {
            return true;
        }
    }
    return false;
};

//Check if value is in the column
var isInCol = function(col, number) {    
    for (var row = 0; row < 9; row++) {
        if (sol[row][col] == number) {
            return true;
        }
    }     
    return false;
};

// Check if value is in its 3x3 box
var isInBox = function(row, col, number) {
    r = row - row % 3;
    c = col - col % 3;

    for (i = r; i < r + 3; i++) {
        for (j = c; j < c + 3; j++) {            
            if (sol[i][j] == number) {
                return true;
            }
        }
    }
    return false;
};

var isOk = function(row, col, number) {
    return !isInRow(row,number) && !isInCol(col,number) && !isInBox(row, col, number);
}

var solve = function () {
    for (var row = 0; row < 9; row++) {
        for (var col = 0; col < 9; col++) {
         // we search an empty cell
            if (sol[row][col] == 0) {
           // we try possible numbers
                for (var number = 1; number <= 9; number++) {
                    if (isOk(row, col, number)) {
                    // number ok. it respects sudoku constraints
                        sol[row][col] = number;
                        if (solve()) { // we continue to the next empty cell
                            return true;
                        } else { // if not a solution, we empty the cell and we continue
                            sol[row][col] = 0;
                        }
                    }
                }
                return false; //backtrack and try the next possible number
            }
        }
    }
    printBoard();
    return true;
};
// function will get called when page loads
printBoard();