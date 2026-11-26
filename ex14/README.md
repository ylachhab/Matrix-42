# Exercise 14: projection display

Keep both display folders at the project root:

- `display_macos/`: macOS display executable and assets.
- `matrix_display/`: Linux display executable and assets.

If you need to extract the supplied archives, run these commands from the
project root with the archives there:

```sh
mkdir -p display_macos matrix_display
tar -xzf display_macos.tar.gz -C display_macos
tar -xzf display_linux.tar.gz -C matrix_display
```

Generate the projection from the project root:

```sh
python3 -m ex14.main
```

This writes the same `proj` file into both folders. Run the display from its
own folder so it can find `proj` and its assets.

On macOS:

```sh
cd display_macos
./display
```

On Linux:

```sh
cd matrix_display
./display
```

The supplied executables are for x86-64. The macOS executable may require
Rosetta on Apple Silicon.
