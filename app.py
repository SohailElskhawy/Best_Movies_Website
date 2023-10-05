import pandas as pd
from flask import Flask,render_template


df = pd.read_csv(r'data\sample_output.csv')

my_data = df.to_dict(orient='records')

print(my_data[0])


app = Flask(__name__)

@app.route("/")
def page_one():
    return render_template('index.html',contents = my_data)



if __name__ == '__main__':
    app.run()