from flask import Flask




app = Flask(__name__)


@app.route('/')
def world():
    return "Hello World"

@app.route('/about')
def about():
    return "This is About page"

@app.route('/product')
def product():
    return "This is Product page"

print(__name__)


# We can also add same url to  different url name
# Example: We need to access same information of existing url name=('/') in a new url name called ('/Home').

#        new url name, End point, existing url information(def world():)
#                   ^      ^       ^
app.add_url_rule('/home','home',world)


print('====================DYNAMIC================')


# Lets make a dynamic website, suppose the clint wants to show hello+ whatever name which clint put in the urls ('/)

@app.route('/welcome/<name>') # Here whatever add in the url path and its consist as Str, Tuple, Dict Therefor if we need to add int or float we must add its data type, '/<int:number>' or '/<float:number>'
def welcome(name):
    return "Welcome"+" "+name  

# Lets some task in number, Here we show age 

@app.route('/age/<int:num>')
def age(num):
    return(f'I am {num} Years old')

@app.route('/Table/<int:num>')
def table(num):
    num=int(input("Enter your Number"))
    for i in range(1,11):
        tab= num,"x",i,"=",num*i
    return tab
    
# Let Add HTML Template in this urls





if __name__ == '__main__':
    app.run(debug=True)