# Alien Invasion — Book-Based Pygame Demo

This repository contains a small, finished Pygame project inspired by the "Alien Invasion" example (chapters 12–14 style). It implements a playable 2D shooter with a player ship, bullets, an alien fleet, basic collisions, simple level progression, and speed scaling.

This README documents what is implemented, how to run the game, common troubleshooting steps, and suggested next improvements.

## Implemented features (chapters 12–14)
- Player ship with smooth left/right movement.
- Firing bullets from the ship; bullets travel upward and are removed off-screen.
- Alien fleet generation: multiple rows and columns of aliens laid out automatically.
- Fleet movement: aliens move horizontally, drop and reverse when they hit screen edges.
- Bullet–alien collisions (bullets destroy aliens).
- Level progression: when all aliens are destroyed the fleet is recreated and alien speed increases.

Note: This is a compact, book-style implementation — aliens use a simple rectangle sprite to avoid missing external assets.

## Requirements
- Python 3.10+ (the repo was developed with Python 3.12; code is compatible with 3.10+)
- Pygame

Install Pygame with pip (PowerShell example):

```powershell
python -m pip install pygame
```

## Run the game
Open PowerShell in the project root (where `main.py` is) and run:

```powershell
python main.py
```

The game window should open. Use the controls below to play.

## Controls
- Left arrow — move ship left
- Right arrow — move ship right
- Space — fire a bullet
- Close window — exit the game

## Files and responsibilities
- `main.py` — program entry point and main game loop
- `settings.py` — game configuration (screen size, speeds, bullet sizes, fleet settings)
- `shipFile.py` — `Ship` class (image loading, movement, drawing)
- `bullet.py` — `Bullet` sprite (creation, movement, draw)
- `alien.py` — `Alien` sprite (rect-based, movement, draw)
- `game_function.py` — input handling, fleet creation, collision checks, drawing helpers
- `image/ship.png` — ship sprite image (required by `Ship`)

## Architecture & file connections

This section explains how the files connect and how data flows during runtime:

- `main.py` is the orchestrator. It:
  - Creates a `Settings` instance from `settings.py` and initializes the display.
  - Creates the `Ship` (from `shipFile.py`), the `bullets` group (a `pygame.sprite.Group`), and the `aliens` group.
  - Calls `game_function.create_fleet()` to populate the `aliens` group.
  - Runs the main loop which calls the functions in `game_function.py` to handle input, update game objects, and redraw the screen each frame.

- `game_function.py` contains the runtime logic and helpers:
  - Event handling: `check_event()` processes Pygame events and delegates key presses to create `Bullet` objects (from `bullet.py`) or toggle ship movement flags (in `Ship`).
  - Fleet logic: `create_fleet()` computes how many aliens fit horizontally and vertically, creates `Alien` instances (from `alien.py`), and adds them to the `aliens` group.
  - Collisions and updates: `update_aliens()` advances the alien positions and checks for edge collisions; `check_bullet_alien_collisions()` uses `pygame.sprite.groupcollide` to remove bullets and aliens when they overlap.
  - Drawing: `update_screen()` draws bullets, the ship, and aliens and then flips the display.

- `shipFile.py` implements the `Ship` class and exposes `update()` and `blitme()` methods used by `main.py` and `game_function.py`:
  - Movement flags (`moving_left`, `moving_right`) are toggled by event handlers in `game_function.py`.
  - `update()` moves the ship's `rect` using speeds defined in `settings.py`.

- `bullet.py` defines the `Bullet` sprite:
  - Created from `game_function.check_keydown_events()` when SPACE is pressed.
  - `Bullet.update()` moves the bullet up each frame; bullets are managed by the `bullets` group in `main.py`.
  - `game_function.update_screen()` iterates over `bullets.sprites()` and calls `draw_bullet()` for rendering.

- `alien.py` defines a simple `Alien` sprite:
  - `create_fleet()` in `game_function.py` creates rows/columns of `Alien` instances and adds them to the `aliens` group.
  - `update()` moves each alien based on `settings.py` values; `check_edges()` detects when the fleet should drop and reverse direction.

Runtime flow (frame-by-frame):
1. `main.py` calls `game_function.check_event()` to handle input (creating bullets or moving the ship).
2. `ship.update()` moves the ship based on movement flags.
3. `bullets.update()` moves bullets upward; off-screen bullets are removed in `main.py`.
4. `game_function.update_aliens()` moves aliens and checks for collisions with the ship or bottom of the screen.
5. `game_function.check_bullet_alien_collisions()` removes bullets and aliens on collision and recreates the fleet when all aliens are gone.
6. `game_function.update_screen()` draws bullets, ship, aliens, and flips the display.

## Troubleshooting

- Missing `image/ship.png` or image load errors
  - Ensure you run `main.py` from the project root so the relative path `image/ship.png` resolves correctly.

- Bullets invisible or not moving
  - Confirm `bullet.py` places bullets above the ship on spawn (`self.rect.bottom = ship.rect.top`).
  - Confirm `bullets.update()` is called in the main loop (it is in `main.py`).
  - Confirm `game_function.update_screen()` draws bullets before calling `pygame.display.flip()`.

- Performance
  - If the game runs slowly, increase the ship and bullet speed settings in `settings.py`:

```python
# e.g. in settings.py
self.ship_speed_factor = 2
self.bullet_speed_factor = 3
```

## How the main systems work (quick reference)
- Bullets are a `pygame.sprite.Group`; pressing SPACE creates a `Bullet` and adds it to the group.
- Each frame the game calls `bullets.update()` (moves bullets) then removes bullets that moved off-screen.
- The fleet is constructed by calculating how many aliens fit per row and how many rows fit on the screen; when the fleet hits the edge it drops, reverses direction, and continues.
- Collisions use `pygame.sprite.groupcollide(bullets, aliens, True, True)` to remove both bullets and aliens upon collision.

## Next improvements you might want
- Add a score counter and HUD (chapter 13): implement a `Scoreboard` to display score, level, and remaining ships.
- Add lives/ship limit and a start/game-over screen.
- Replace rectangle aliens with sprite images (add `image/alien.png` and load with `pygame.image.load`).
- Add sound effects for firing and collisions.

## Notes for contributors
- Keep relative paths correct (run from project root) or make image loading robust by using `os.path.join` with `__file__`.
- The code is intentionally compact. If you want, I can expand the UI (start screen, play button) and add tests for core logic.

If you'd like, I can now polish visuals (alien images), add scoring and HUD, and implement a start screen and game-over flow. Tell me which feature to add next and I'll implement it.
