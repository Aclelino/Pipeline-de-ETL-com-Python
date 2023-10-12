from flask import Flask,jsonify,request

vagas =[
{
        "id":1,
        "Vaga":"Dev Python",
        "Senioridade":"Sr",
        "Local":"Remoto",
        "Descricao":"new"
},
{
        "id":2,
        "Vaga":"Dev Java",
        "Senioridade":"Sr",
        "Local":"Remoto",
        "Descricao":"new"
},
    
{
        "id":3,
        "Vaga":"Analista de Dados",
        "Senioridade":"Sr",
        "Local":"Remoto",
        "Descricao":"new"
},
{
        "id":4,
        "Vaga":"Cientista de Dados",
        "Senioridade":"Jr",
        "Local":"Remoto",
        "Descricao":"new"
},

]


app = Flask(__name__)

@app.route('/',methods=["PUT"])

def vaga_ti():
    return "Home Pagina"

@app.route('/vaga',methods=["GET"])
def allJobs():
    
    return jsonify(vagas)

@app.route('/vaga/<int:id>',methods=['GET'])

def vaga_id(id):
    
    for vaga in vagas:
        if vaga.get('id') == id:
            return jsonify(vaga)
        
        
if __name__ == "__main__":
    app.run(debug=True)
