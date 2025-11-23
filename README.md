# 2048 PyGame

## Description
This is a Python implementation of the popular **2048 game** using PyGame. Slide numbered tiles on a 4×4 grid to combine matching tiles (2+2 → 4, etc.) until you reach 2048. The game continues beyond 2048 for higher scores.

## Features
- 4×4 grid, single-player
- Moves in four directions (Up, Down, Left, Right)
- Tiles with equal values merge on collision
- New tile (2 or 4) spawns randomly after each valid move
- Win condition: reaching the 2048 tile
- Lose condition: no legal moves remain
- Board display with colors
- Score tracking and high score persistence
- Restart option after game over

## How to Run
1. Make sure Python 3.x is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the game:
   python main.py

## Controls
- Arrow Keys: Move tiles (Up, Down, Left, Right)
- Enter: Restart the game after game over
- Close Window: Quit the game

## Files
- main.py — Entry point, handles game loop and events
- board.py — Board display and piece rendering
- game_logic.py — Tile movement and merging logic
- icon.png.png — Window icon
- data/high_score.txt — High score storage
