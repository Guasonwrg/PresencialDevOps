from flask import Flask, request, jsonify

app = Flask(__name__)

def palindromo (cadena):

    return cadena == cadena[::-1]

print(palindromo("ana")) 
print(palindromo("hola")) 

