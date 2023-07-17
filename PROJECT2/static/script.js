document.addEventListener('DOMContentLoaded', () => {
  const cells = document.querySelectorAll('.cell');
  const resetButton = document.getElementById('reset');
  const quitButton = document.getElementById('quit');
  const player1Input = document.getElementById('player1');
  const player2Input = document.getElementById('player2');
  let currentPlayer = 'X';
  let gameEnded = false;

  // Add event listeners to cells
  cells.forEach(cell => {
    cell.addEventListener('click', () => {
      if (!cell.textContent && !gameEnded) {
        makeMove(cell.dataset.position);
      }
    });
  });

  // Add event listener to reset button
  resetButton.addEventListener('click', resetGame);

  // Add event listener to quit button
  quitButton.addEventListener('click', quitGame);

  // Function to make a move
  function makeMove(position) {
    // Send a POST request to the /play endpoint with the chosen position
    fetch('/play', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ position })
    })
      .then(response => response.json())
      .then(data => {
        if (data.validMove) {
          // Update the game board on the frontend
          cells[position].textContent = currentPlayer;
          currentPlayer = currentPlayer === 'X' ? 'O' : 'X';

          if (data.winner) {
            // Handle win
            handleWin(data.winner);
          } else if (data.tie) {
            // Handle tie
            handleTie();
          }
        } else {
          // Handle invalid move
          console.log('Invalid move. Try again.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  // Function to handle win
  function handleWin(winner) {
    gameEnded = true;
    cells.forEach(cell => {
      cell.removeEventListener('click', () => {
        if (!cell.textContent && !gameEnded) {
          makeMove(cell.dataset.position);
        }
      });
    });

    alert(`Player ${winner} wins!`);
  }

  // Function to handle tie
  function handleTie() {
    gameEnded = true;
    alert('It\'s a tie!');
  }

  // Function to resetthe game
  function resetGame() {
    cells.forEach(cell => {
      cell.textContent = '';
    });
    currentPlayer = 'X';
    gameEnded = false;
  }

  // Function to quit the game
  function quitGame() {
    gameEnded = true;
    alert('Game has been quit.');
  }
});




  