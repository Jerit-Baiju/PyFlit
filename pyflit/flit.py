class page:

    def __init__(self, name):
        self.name = name
        self.errs = []
        try:
            self.op = open(f"index.html").read()
        except:
            open('index.html', 'w').write("""<!DOCTYPE html>
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


</head>

<body onload='' class="bg-light">

    {{root}}

    <script>
        // {{script}}
    </script>

    <!-- ADD YOUR JS & CDN HERE WHICH IS APPLICABLE TO ALL PAGES -->
</body>

</html>""")

    def add_err(self, err):
        err = err.capitalize()
        self.errs.append(err)

    def check_err(self):
        if self.errs == []:
            return self.op
        else:
            return "<h2>" + str(self.errs).replace(',', '<br>').replace('[', '').replace(']', '').replace("'", "") + "</h2>"

    def title(self, title):
        self.op = self.op.replace('{{title}}', title)

    def add(self, content):
        try:
            self.op = self.op.replace(
                '{{root}}', content + "\n" + "{{root}}" + "\n")
        except:
            self.add_err('root error adding error')

    def add_component(self, component):
        try:
            self.add(open(f"components/{component}.html", 'r').read())
        except:
            self.errs.append(f'Create {component}.html in components folder')

    def add_page(self, page):
        try:
            self.add(open(f"pages/{page}.html", 'r').read())
        except:
            self.errs.append(
                f"Your page not found ({page}.html). Please create your pages in pages folder")

    def add_css(self, css):
        try:
            self.op = self.op.replace(
                '/* {{style}} */', open(f'static/css/{css}.css', 'r').read() + "\n" + "/* {{style}} */")
        except:
            self.errs.append(
                f"Your css not found ({css}.css). Please create your css file in css folder")

    def add_js(self, js):
        try:
            self.op = self.op.replace(
                '// {{script}}', open(f'static/js/{js}.js').read() + "\n" + "// {{script}}")
        except:
            self.errs.append(
                f"Your js not found ({js}.js). Please create your js file in js folder")

    def add_body_onload(self, func):
        self.op = self.op.replace("onload=''", f"onload='{func}()'")

    def add_var(self, var, content):
        text = f"const {var} = ''"
        content = f"const {var} = '{content}'"
        self.op = self.op.replace(text, content)

    def clear(self):
        self.op = self.op.replace('{{root}}', '\n')
        self.op = self.op.replace('/* {{style}} */', '')
        self.op = self.op.replace('// {{script}}', '\n')
        if "{{title}}" in self.op:
            self.errs.append('Title not added')
        # open('last.html','w').write(self.op)

    def export(self):
        self.clear()
        return self.check_err()
