# Kinoko

[![Luke's rMC3 RTA WR](<https://vabold.github.io/Kinoko/Luke rMC3 RTA WR.svg>)](https://www.youtube.com/watch?v=6H6UnSDPPdI)
[![Kasey's LC RTA WR](<https://vabold.github.io/Kinoko/Kasey LC RTA WR.svg>)](https://www.youtube.com/watch?v=HPcvNS8QFVI)
[![Luke's rBC RTA WR](<https://vabold.github.io/Kinoko/Luke rBC RTA WR.svg>)](https://www.youtube.com/watch?v=twZes-RI6Sc)
[![Kasey's rSGB RTA WR](<https://vabold.github.io/Kinoko/Kasey rSGB RTA WR.svg>)](https://www.youtube.com/watch?v=SjXUPXT8n8g)
[![Vincent's rMR RTA WR](<https://vabold.github.io/Kinoko/Vincent rMR RTA WR.svg>)](https://www.youtube.com/watch?v=y7t4_xXuD2A)
[![Sosis's rSL RTA WR](<https://vabold.github.io/Kinoko/Sosis rSL RTA WR.svg>)](https://www.youtube.com/watch?v=ahNGAaUzm6s)
[![Logan's MH RTA WR](<https://vabold.github.io/Kinoko/Logan MH RTA WR.svg>)](https://www.youtube.com/watch?v=CellUlOYgnc)
[![Logan's rBC3 RTA WR](<https://vabold.github.io/Kinoko/Logan rBC3 RTA WR.svg>)](https://www.youtube.com/watch?v=vSbSADDEzEs)

Kinoko is a reimplementation of Mario Kart Wii's physics engine in C++. This project is a spiritual continuation of [stblr/Hanachan](https://github.com/stblr/Hanachan). Like Hanachan, the goal of this reimplementation is to reach perfectly accurate ghost replay.

## Building

### Dependencies

- g++ 13.1 (C++23)
- ninja
- Python 3

### Process

Generate the ninja file:

```bash
./configure.py
```

Execute it:

```bash
ninja
```

## Interfacing

While a GUI is not planned for the project at this time, contributors are welcome to add a graphics frontend under three conditions. The license must not change, it does not interfere with the CLI, and most importantly, it does **not** distribute any in-game assets.

## Contributing

The codebase uses C++ for the engine and Python for any external scripts.

Pull requests resolving an issue or element of a tracking issue should reference the issue or item in the description.

Any commits should be formatted using the project's clang-format file.

## Resources

- [MKW-SP Discord](https://discord.gg/TPSKtyKgqD) - Request Ghidra server access and chat with contributors.
- [Matching Decompilation](https://github.com/riidefi/mkw) - A repository that compiles back into the game's original assembly.
- [Tockdom](http://wiki.tockdom.com/wiki/Main_Page) - A wiki maintained by multiple community members, most notably used for file formats.
