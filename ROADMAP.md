# Textsmith Roadmap

Welcome to the development roadmap for **Textsmith**, a lightweight, modular engine for building text-based adventure games in Python.

This roadmap outlines planned features and goals leading up to the **v1.0** release. Contributions, ideas, and feedback are always welcome!

---

## Version 0.1 – Initial Release (Complete)
- [x] `Game`, `Player`, and `Room` classes implemented
- [x] Room connections (N/S/E/W)
- [x] Basic command handling: `LOOK`, `MOVE`
- [x] Example usage in README
- [x] Modular and extensible structure

---

## Version 0.2 – Game Loop & CLI Input
>  Goal: Make the engine interactive from the command line

- [ ] Implement a game loop that takes user input
- [ ] Parse raw input strings (e.g., `"move north"` → `"MOVE", 0`)
- [ ] Map direction words to direction indexes
- [ ] Add `EXIT` or `QUIT` command
- [ ] Optional: Add `HELP` command
- [ ] Update README with instructions for interactive play

---

## Version 0.3 – Engine Extensibility
> Goal: Make it easier to build custom mechanics

- [ ] Add room event hooks (`on_enter`, `on_exit`)
- [ ] Allow custom actions on rooms or players
- [ ] Enable easier subclassing of core classes
- [ ] Define constants/enums for directions (e.g., `Direction.NORTH`)
- [ ] Refactor command handling for custom commands

---

## Version 0.4 – Items and Inventory
> Goal: Introduce a simple item system

- [ ] `Item` class with name/description
- [ ] Add player inventory
- [ ] Add item support in rooms
- [ ] Commands: `TAKE`, `DROP`, `INVENTORY`
- [ ] Enhance `LOOK` to show visible items

---

## Version 0.5 – External Game Data
> Goal: Enable loading game data from files

- [ ] Load rooms and connections from JSON or YAML
- [ ] Define player spawn room in config
- [ ] Optional: Add support for hot-reloading room definitions
- [ ] Create sample map file

---

## Version 0.6 – Testing & Stability
> Goal: Make the engine stable and testable

- [ ] Unit tests for `Game`, `Room`, `Player`
- [ ] Tests for command parsing and movement
- [ ] Setup linter (e.g., `flake8`, `black`)
- [ ] Improve validation and error messages

---

## Version 0.7 – Quality of Life Enhancements
> Goal: Improve developer and player experience

- [ ] Option for auto bi-directional room connections
- [ ] Handle bad input more gracefully
- [ ] Add optional room ID or UUID
- [ ] Support flexible direction input (`"north"`, `"n"`, `"NORTH"`)

---

##  Version 0.8 – Packaging and Installability
>  Goal: Make it installable as a Python package

- [ ] Add `setup.py` or `pyproject.toml`
- [ ] Include `__init__.py` for module structure
- [ ] Create installable pip package
- [ ] Publish to PyPI (optional)
- [ ] Include a sample game in `/examples/`

---

##  Version 0.9 – Documentation and Community
> Goal: Improve onboarding and contributions

- [ ] Polish README with full usage
- [ ] Add full documentation (Sphinx or MkDocs)
- [ ] Add `CONTRIBUTING.md`, `LICENSE`, and `CODE_OF_CONDUCT.md`
- [ ] Add GitHub Issues/PR templates
- [ ] Add README badges

---

## Version 1.0 – Full Stable Release
> Goal: Deliver a polished, tested, and extensible engine

- [ ] All core features complete
- [ ] Fully tested
- [ ] Fully documented
- [ ] Packaged and published
- [ ] Includes playable demo game

---

## 📌 Milestone Tags
- `v0.2`: Interactive CLI
- `v0.4`: Inventory system
- `v0.5`: File-based map loading
- `v0.8`: PyPI-ready package
- `v1.0`: Stable public release

---

Feel free to fork, contribute, and submit suggestions!  
Let’s build something cool. 🚀
