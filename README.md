# TP Webserver 2

## Installation

If you have a python 3.8.12 version, you can run this program without Docker, otherwise, you will have to use it following the procedures below.

### With Docker

```bash
docker build -t tp2webserver_image .
docker run -itd --name tp2webserver -p 5000:5000 -v $PWD:/app --hostname noah tp2webserver_image:latest
docker exec -it tp2webserver bash
python -V #Tester l'installation de python 3.8.12
python app.py #Lancer le script python
```

### Without Docker (in python 3.8.12 only)

```bash
pip3 install -r requirements.txt
python3 app.py
```

## Usage

Test the installation in your browser with this URL : [http://127.0.0.1:5000/bonjour](http://127.0.0.1/bonjour)

## Contributing

- Noah CHATELAIN
- Ambroise GYRE

## License

[MIT](https://choosealicense.com/licenses/mit/)
