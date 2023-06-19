# ImageStickyNote

## Overview

ImageStickyNote is a Python tool that allows you to display any image as a sticky note on your desktop. It's simple, lightweight, and customizable.

## Installation

Before installing ImageStickyNote, make sure you have the following dependencies installed: Python 3.x, GdkPixbuf, Gtk, Gdk. Then, use pip to install:

```bash
pip install ImageStickyNote
```

## Usage
You can use ImageStickyNote from your command line:

```bash
ImageStickyNote /path/to/image [x_position] [y_position] [width] [height]
```

By default, the image is displayed at (0,0) with a size of 400x400 pixels.

Example:

```bash
ImageStickyNote /home/user/pictures/note.png 200 200 800 600
```
This displays note.png at (200, 200) with a width of 800 and a height of 600 pixels.

## Contributing

Contributions are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

ImageStickyNote is licensed under the MIT License. See the [License](URL) file for more details.

