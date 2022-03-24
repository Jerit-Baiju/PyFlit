class Page:
    __index__ = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <!-- ADD YOUR CSS & CDN HERE WHICH IS APPLICABLE TO ALL PAGES -->
    <style>
        /* {{style}} */
    </style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
</head>

<body onload=''>
    {{root}}
    <script>
        // {{script}}
    </script>
    <!-- ADD YOUR JS & CDN HERE WHICH IS APPLICABLE TO ALL PAGES -->
</body>
</html>"""

    def __write_index__(self):
        open('index.html', 'w').write(self.__index__)

    def __init__(self, name):
        self.name = name.capitalize()
        self.__errs__ = []
        self.title = 'Document'
        self.__welcome__ = f"<center><h1 class='fw-light'>PyFlit</h1></center><h2 class='fw-light'>Template : {self.name} <br> Running Successful</h2>"
        self.__content__ = ""
        try:
            self.__op__ = open(f"index.html").read()
            if "<title>{{title}}</title>" not in self.__op__:
                self.write_index()
            if "/* {{style}} */" not in self.__op__:
                self.write_index()
            if "{{root}}" not in self.__op__:
                self.write_index()
            if "// {{script}}" not in self.__op__:
                self.write_index()
        except:
            self.__op__ = self.__index__
            open('index.html', 'w').write(self.__op__)

    def __add_err__(self, err):
        __err__ = err.capitalize()
        self.__errs__.append(__err__)
    
    def __add__(self, content):
        try:
            self.__content__ = self.__content__ + content
        except:
            self.__add_err__('root adding error')

    def add_html(self,html):
        self.__add__(html)

    def add_component(self, component):
        if ".html" in component:
            component = component.replace('.html', '')
        try:
            self.__add__(open(f"components/{component}.html", 'r').read())
        except:
            self.__errs__.append(f'Create {component}.html in components folder')

    def add_page(self, page):
        if ".html" in page:
            page = page.replace('.html', '')
        try:
            self.__add__(open(f"pages/{page}.html", 'r').read())
        except:
            self.__errs__.append(
                f"Your page not found ({page}.html). Please create your pages in pages folder")

    def add_css(self, css_file):
        if ".css" in css_file:
            css_file = css_file.replace('.css', '')
        try:
            self.__op__ = self.__op__.replace(
                '/* {{style}} */', open(f'static/css/{css_file}.css', 'r').read() + "\n" + "/* {{style}} */")
        except:
            self.__errs__.append(
                f"Your css file is not found ({css_file}.css). Please create your css file in this path => /static/css/{css_file}.css")

    def add_js(self, js_file):
        if ".js" in js_file:
            js_file = js_file.replace('.js', '')
        try:
            self.__op__ = self.__op__.replace(
                '// {{script}}', open(f'static/js/{js_file}.js', 'r').read() + "\n" + "// {{script}}")
        except:
            self.__errs__.append(f"Your JS file is not found ({js_file}.js). Please create your JS file in this path => /static/js/{js_file}.js")

    def add_body_onload(self, func):
        self.__op__ = self.__op__.replace("body onload=''", f"body onload='{func}()'")

    def add_var(self, var, content):
        if f"const {var} = ''" in self.__op__:
            content = f"const {var} = '{content}'"
            self.__op__ = self.op.replace(f"const {var} = ''", content)
        elif f'const {var} = ""' in self.__op__:
            content = f'const {var} = "{content}"'
            self.__op__ = self.__op__.replace(f'const {var} = ""', content)
        else:
            self.__errs__.append(f'please add an empty var like this : const {var} = "" ')

    def check_err(self):
        if self.__errs__ == []:
            return self.__op__
        else:
            return "<h2>" + str(self.__errs__).replace(',', '<br>').replace('[', '').replace(']', '').replace("'", "") + "</h2>"


    def __clear__(self):
        if self.__content__ == "":
            self.__content__ = self.__welcome__
        self.__op__ = self.__op__.replace('{{root}}', self.__content__)
        self.__op__ = self.__op__.replace('/* {{style}} */', '')
        self.__op__ = self.__op__.replace('// {{script}}', '')

    def export(self):
        self.__op__ = self.__op__.replace('{{title}}',self.title)
        self.__clear__()
        return self.check_err()
