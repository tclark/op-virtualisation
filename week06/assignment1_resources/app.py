from flask import Flask

app = Flask(__name__)
frontend_ip = '10.25.2.61' #ip address of host that will run frontend

@app.route('/')
def kittens():
    return """ \
<!doctype html>
<html lang="en">
 <head>
  <title>IN720 Assignment 1</title>
 </head>
 <body>
  <div>
   <img src="http://{}/kitten.jpg" />
  </div>
 </body>
</html>""".format(frontend_ip) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')

