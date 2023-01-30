# PyFlit
Pyflit is a Python Package with many helpful features for [FLASK](https://pypi.org/project/Flask/) developers. It helps you to add components, pages, send Python variables to JavaScript and many other features like, you can add same navbar for every pages while writing it only once. And if you would like to change the code you need to change the code only for once.

# Links

- **Source - [GitHub](https://jerit.ml/github)**
- **My WebSite - [Jerit Baiju](https://jerit.ml)**
- **Contact Me - [WhatsApp](https://jerit.ml/whatsapp)**

## Installation

PyFlit is available on PyPi:

```bash
python3 -m pip install pyflit
```

```bash
pip3 install pyflit
```

PyFlit officially supports Python 3.8+.

## Cloning the Repository

```bash
git clone https://github.com/Jerit-Baiju/PyFlit.git
```

## Features

- Add components in pages
- Render single line HTML
- Adding CSS
- Adding JS
- Send Python variables to JavaScript
- Easy to Use
- Install and Use

## Usage

```py
from flask import Flask
from pyflit import Page

app = Flask(__name__)

@app.route('/')
def index():
    # INITIALIZING PAGE
    index = Page('index')
    # ADD PAGE TITLE
    index.title('Jerit Baiju')
    # ADD CSS
    index.add_css('index')
    # ADD COMPONENT
    index.add_component('navbar')
    # ADD PAGE
    index.add_page('index')
    index.add_component('footer')
    # EXPORTING
    return index.export()

app.run()

```

## License

MIT.
For more information see [LICENSE](https://github.com/Jerit-Baiju/PyFlit/blob/master/LICENSE)
