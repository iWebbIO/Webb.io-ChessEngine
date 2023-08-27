# Chess API Documentation (For JavaScript/Node.js)

Welcome to the documentation for Moreweb's Chess API! This API allows you to interact with a chess game using HTTP requests. It provides endpoints to make moves, get the current state of the chessboard, and reset the game. This documentation will guide you on how to use the Chess API specifically with JavaScript and Node.js.

## Base URL

The base URL for the Chess API is `https://chessengine-io.moreweblearn.repl.co/`.

## Installation

To use the Chess API in your JavaScript/Node.js project, you need to install the `axios` library. You can do this by running the following command in your terminal:

```bash
npm install axios
```

## Make Move

Endpoint: `/api/make-move`

This endpoint allows you to make a move in the chess game.

### Request

- Method: POST
- Content-Type: application/json
- Body:

| Field     | Type   | Description                                  |
| --------- | ------ | -------------------------------------------- |
| start_row | number | The starting row of the piece to be moved    |
| start_col | number | The starting column of the piece to be moved |
| end_row   | number | The target row for the move                  |
| end_col   | number | The target column for the move               |

Example:

```javascript
const axios = require('axios');

const makeMove = async (startRow, startCol, endRow, endCol) => {
  try {
    const response = await axios.post('https://chessengine-io.moreweblearn.repl.co/api/make-move', {
      start_row: startRow,
      start_col: startCol,
      end_row: endRow,
      end_col: endCol
    });

    console.log(response.data.message);
  } catch (error) {
    console.error(error);
  }
};

makeMove(1, 2, 3, 2);
```

### Response

- Content-Type: application/json

| Field   | Type    | Description                                      |
| ------- | ------- | ------------------------------------------------ |
| success | boolean | Indicates whether the move was successful or not |
| message | string  | A message describing the result of the move      |

Example:

```json
{
  "success": true,
  "message": "Move successful!"
}
```

## Get Board

Endpoint: `/api/get-board`

This endpoint allows you to get the current state of the chessboard.

### Request

- Method: GET

Example:

```javascript
const axios = require('axios');

const getBoard = async () => {
  try {
    const response = await axios.get('https://chessengine-io.moreweblearn.repl.co/api/get-board');

    console.log(response.data.board);
    console.log(response.data.current_player);
  } catch (error) {
    console.error(error);
  }
};

getBoard();
```

### Response

- Content-Type: application/json

| Field          | Type   | Description                         |
| -------------- | ------ | ----------------------------------- |
| board          | array  | The current state of the chessboard |
| current_player | string | The player who is currently playing |

Example:

```json
{
  "board": [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
  ],
  "current_player": "white"
}
```

## Reset Game

Endpoint: `/api/reset-game`

This endpoint allows you to reset the chess game to its initial state.

### Request

- Method: POST

Example:

```javascript
const axios = require('axios');

const resetGame = async () => {
  try {
    const response = await axios.post('https://chessengine-io.moreweblearn.repl.co/api/reset-game');

    console.log(response.data.message);
  } catch (error) {
    console.error(error);
  }
};

resetGame();
```

### Response

- Content-Type: application/json

| Field   | Type   | Description                    |
| ------- | ------ | ------------------------------ |
| message | string | A message confirming the reset |

Example:

```json
{
  "message": "Game reset successfully!"
}
```

That's it! You now have the necessary information to use Moreweb's Chess API with JavaScript and Node.js. Don't forget to install the `axios` library and make the HTTP requests to the respective endpoints.
