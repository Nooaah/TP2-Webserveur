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

Once the *app.py* API is launched, open a new terminal in the current directory of the project, then thanks to the curl command, send the *input.zip* file and the JSON of the expected SHA-1 checksums for each file:

```bash
curl -X POST -i -F json="{\"photo1\":\"e4bc0da9501b4b23f5d5ebeaf8f0c69b105ce4db\",\"photo2\":\"9d528c080e4b06af37ba8446ff69bdead9c08e6a\",\"photo3\":\"SHA1CODE-FALSE\"}" -F "file=@/Users/noahchatelain/Desktop/app/input.zip" 127.0.0.1:5000/extract
```

## Contributing

- Noah CHATELAIN
- Ambroise GYRE

## License

[MIT](https://choosealicense.com/licenses/mit/)
