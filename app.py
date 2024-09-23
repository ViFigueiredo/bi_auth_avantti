from flask import Flask, render_template, request, redirect, url_for, flash, abort, get_flashed_messages
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import pandas as pd
import os

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'dlçsakjdjawlermwaçdopwjeqwk4o329482039i12-*/+d1239830ir'
app.config['UPLOAD_FOLDER'] = './'

df = pd.read_excel('planilha.xlsx')


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in list(df['usuario']) and username != 'admin':
        return
    user = User()
    user.id = username
    return user


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    user = User()
    if username == 'admin' and password == 'admin':
        user.id = username
        login_user(user)
        return redirect(url_for('upload_file'))
    else:
        if username in list(df['usuario']) and password == df.loc[df['usuario'] == username, 'senha'].values[0]:
            user.id = username
            login_user(user)
            return redirect(url_for('protected'))
        else:
            flash('Acesso inválido!', 'error')
            return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/protected')
@login_required
def protected():
    user_content = df.loc[df['usuario'] == current_user.id, [
        'conteudo', 'iframe']].values.tolist()
    return render_template('protected.html', user_content=user_content)


@app.route('/reload_data', methods=['GET'])
@login_required
def reload_data():
    global df
    df = pd.read_excel('planilha.xlsx')
    flash('Dados recarregados com sucesso!', 'success')
    return redirect(url_for('upload_file'))


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if current_user.is_anonymous or current_user.id != 'admin':
        abort(403)
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and file.filename.endswith('.xlsx'):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Upload realizado com sucesso!', 'success')
            return redirect(url_for('reload_data'))

    messages = get_flashed_messages(with_categories=True)
    return render_template('upload.html', messages=messages)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
