#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb, sys, os
from parser.parser import parser, yacc, quad_helper, error_helper, parser_helper, memory
from virtual_machine.virtual_machine import run_code, vmh


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from text area field
if form.getvalue("textcontent"):
    text_content = form.getvalue("textcontent")
else:
    text_content = "Nein!"
# Get data from radio button fields
if form.getvalue("type"):
    # html or plain
    type = form.getvalue("type")
else:
    type = "html"

print(f"Content-type:text/{type}\n")
print("""
<html>
<head>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title> Trendlit - Cloud Based Programming Language</title>
</head>

<body>
    <div class="container">
""")

data = text_content

try:
    yacc.parse(data, tracking=True)

    if error_helper.error_cont is 0:
        run_code(quad_helper.queue_quad, memory.constant_values)
        for result in vmh.queue_results:
            print(result)
    else:
        print(f"Your code doesn't compile. Please try harder \n")
        print(f"# of Errors: {error_helper.error_cont}\n")
        error_helper.print_errors()

except:
    error = f"Error. We couldn't compile successfully.\n"
    print(error)


print("""
    </div>
""")

print("""
<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
""")

print("""
</body>
</html>
""")
