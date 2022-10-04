import os, subprocess, random

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        data_url = request.form["data_url"]
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=generate_prompt(data_url),
            temperature=0,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        code = response.choices[0].text
        generate_python_file(code)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(data_url):
    return "\"\"\"\nfetch csv file at url '{}' and read into DataFrame\n\"\"\"".format(
        data_url
    )


def generate_python_file(code):
    file_name = 'notebook_code' + str(random.randint(0,1000))
    notebook_name = file_name + '.ipynb'
    file_name = file_name + '.py'
    with open(file_name,'w') as f:
        f.write(code)
        subprocess.run(["ipynb-py-convert",file_name,'output_notebooks/'+notebook_name])


