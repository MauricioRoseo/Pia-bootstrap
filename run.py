from flask import render_template, request, redirect
from markupsafe import escape
from app import app, db # importa as config do app e banco
from py.models import Contato # importa o model

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = escape(request.form['nome'])
        estado = escape(request.form['estado'])
        email = escape(request.form['email'])
        cidade = escape(request.form['cidade'])
        comentarios = escape(request.form['comentarios'])
        novo_contato = Contato(nome=nome, estado=estado, email=email, cidade=cidade, comentarios=comentarios)
        try:
            db.session.add(novo_contato)
            db.session.commit()
            return redirect('/contato')
        except:
            return 'Ocorreu um erro ao cadastrar o contato'
    else:
        return render_template('/contato.html', contato=contato)

@app.route('/admim', methods=['GET'])
def admim():
    contatos=Contato.query.all()
    return render_template('admim.html', contatos=contatos)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)

