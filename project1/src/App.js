import React from 'react'
import { useState } from 'react';

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

function Board({ xIsNext, squares, onPlay }) {
    function handleClick(i) {
        if(calculateWinner(squares) || squares[i]) return;

        function xCount() {
            let count = 0;
            for (let s = 0; s < squares.length; s++)
                if(squares[s] == 'X') count++;
            return count;
        }

        if(xIsNext) {
            //move 1: corner
            if(squares[0] == null && squares[1] == null && squares[2] == null && squares[3] == null && squares[4] == null && squares[5] == null && squares[6] == null && squares[7] == null && squares[8] == null) {
                if (![0, 2, 6, 8].includes(i)) {
                    alert("Not a good choice!");
                    return;
                } else {
                    alert("Good choice!");
                }
            } else if(xCount() == 1) {
                if (squares[4] === 'O') { //if O is in center
                    if(squares[0] == 'X') {
                        if(i == 8) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                    else if(squares[2] == 'X') {
                        if(i == 6) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                    else if(squares[6] == 'X') {
                        if(i == 2) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                    else if(squares[8] == 'X') {
                        if(i == 0) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                } else if (squares[4] !== 'O' && squares[4] !== 'X') { //If O is not in center
                    // X's second move to win if O is not in the center
                    if(squares[0] == 'X') {
                        if(i == 2 && squares[1] == null) {
                            alert("Good choice!");
                        } else if(i == 6 && squares[3] == null) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                    else if(squares[2] == 'X') {
                        if(i == 0 && squares[1] == null) {
                            alert("Good choice!");
                        } else if(i == 8 && squares[5] == null) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                    else if(squares[6] == 'X') {
                        if(i == 0 && squares[3] == null) {
                            alert("Good choice!");
                        } else if(i == 8 && squares[7] == null) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                    else if(squares[8] == 'X') {
                        if(i == 2 && squares[5] == null) {
                            alert("Good choice!");
                        } else if(i == 6 && squares[7] == null) {
                            alert("Good choice!");
                        } else {
                            alert("Not a good choice!");
                            return;
                        }
                    }
                }

                //if (i === 4) {
                //    alert("Not a good choice!");
                //    return;
                //} else if (![1, 3, 5, 7].includes(i)) {
                //    alert("Not a good choice!");
                //    return;
                //} else {
                //    alert("Good choice!");
               // }
            }
        }

    const nextSquares = squares.slice();
    if (xIsNext) {
      nextSquares[i] = 'X';
    } else {
      nextSquares[i] = 'O';
    }
    onPlay(nextSquares);
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = 'Winner: ' + winner;
  } else {
    status = 'Next player: ' + (xIsNext ? 'X' : 'O');
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square value={squares[0]} onSquareClick={() => handleClick(0)} />
        <Square value={squares[1]} onSquareClick={() => handleClick(1)} />
        <Square value={squares[2]} onSquareClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} onSquareClick={() => handleClick(3)} />
        <Square value={squares[4]} onSquareClick={() => handleClick(4)} />
        <Square value={squares[5]} onSquareClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} onSquareClick={() => handleClick(6)} />
        <Square value={squares[7]} onSquareClick={() => handleClick(7)} />
        <Square value={squares[8]} onSquareClick={() => handleClick(8)} />
      </div>
    </>
  );
}

export default function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares = history[currentMove];

  function handlePlay(nextSquares) {
    const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMove(nextHistory.length - 1);
  }

  function jumpTo(nextMove) {
    setCurrentMove(nextMove);
  }

  const moves = history.map((squares, move) => {
    let description;
    if (move > 0) {
      description = 'Go to move #' + move;
    } else {
      description = 'Go to game start';
    }
    return (
      <li key={move}>
        <button onClick={() => jumpTo(move)}>{description}</button>
      </li>
    );
  });

  return (
    <div className="game">
      <div className="game-board">
        <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
      </div>
      <div className="game-info">
        <ol>{moves}</ol>
      </div>
    </div>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

