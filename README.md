# TP Webserver 2

## Installation

If you have a python 3.8.12 version, you can run this program without Docker, otherwise, you will have to use it following the procedures below.

### With Docker
```bash
docker build -t tp2webserver_image .
docker run -itd -p 80:80 --name tp2webserver tp2webserver_image:latest
```

To restart the python container and the program

```bash
docker restart tp2webserver
```

### Without Docker (in python 3.8.12 only)
```bash
pip3 install -r requirements.txt
python3 app.py
```

## Usage

Test the installation in your browser with this URL : [http://127.0.0.1/bonjour](http://127.0.0.1/bonjour)


## Contributing
- Noah CHATELAIN
- Ambroise GYRE

## License
[MIT](https://choosealicense.com/licenses/mit/)
