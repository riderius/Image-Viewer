# Picture-reader

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Hi! **Picture-reader** is a Windows picture reader based on Python 3.8.

## Using:

You must download "Picture-reader.exe" from the root of the repository. Then you have to open the image with "Picture reader.exe".

![OpenFile](https://image.prntscr.com/image/EmCtDUhDTH_HHxAgBFwLag.png)

Then you will see a window like this:

![Picture](https://image.prntscr.com/image/mfNX2USsREu--i70QjsyYA.png)

## Modules Used:

1. pillow

Python 3.8 or higher is recommended for using this program. You need to install the pillow module. You can do this with the following command:

> pip install -r requirements.txt

**Pillow** is the friendly PIL fork by Alex Clark and Contributors. **PIL** is the Python Imaging Library by Fredrik Lundh and Contributors.

## Compilation

Picture-reader is compiled with pyinstaller. This command is used for this.

> pyinstaller -F -i icon.ico -w -n Picture-reader main.py

You can see what these parameters mean in the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#options).

## Versioning

**Picture-reader** uses [Semantic Versioning](https://semver.org/).

## License

This project is licensed under the MIT License, see the [LICENSE](https://github.com/RIDERIUS/Picture-reader/blob/main/LICENSE) file for details.