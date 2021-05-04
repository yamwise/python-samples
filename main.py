import sys
import subprocess
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Code(BaseModel):
    code: str


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/run", response_model=str)
async def run_code(code_object: Code):
    c_code = code_object.code
    #print("Here is your code:", c_code)
    #print("Here is your response:", "Your output is: " + returnoutput(c_code))
    return "Your output is:\n" + returnoutput(c_code)


def tocleanstring(s):
    return str(s)[2:-1]


def returnoutput(string):
    f = open('foo.c', 'w')
    f.write(string)
    f.close()

    try:
        p_comp = subprocess.run(
            ["gcc", "foo.c", "-ofoo", "-std=c99"], capture_output=True, text=True)
        if (p_comp.returncode == 1):
            raise Exception("Compiler Error")
    except:
        return("Your code failed to compile!\n\n" + p_comp.stderr)

    else:
        p_run = subprocess.check_output(["./foo"], stdin=sys.stdin, text=True)
        return p_run


def linenumber(error):
    counter = 0
    for i in range(len(error)):
        if counter == 2:
            final = ''
            for x in error[i:]:
                if x != ':':
                    final += x
                else:
                    return str(final)
        if error[i] == ':':
            counter += 1


def simpleerror(error):
    errors = []

    linenum = linenumber(error)
    if "expected ';'" in error:
        errors.append("You forgot a semicolon on line " +
                      linenum + "! Keep going champ!")

    final = 'You had ' + str(len(errors)) + ' errors!\n\n'

    for i in range(len(errors)):
        final += 'Here is error number ' + str(i + 1) + ': '
        final += errors[i]
        final += '\n'
    return final

 #   return linenum


# print("Output is:", returnoutput(prog))

# print("Output is:", simpleerror(returnoutput(prog)))
