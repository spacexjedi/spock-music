@app.route('/register', methods=['GET', 'POST'])
def register():
    db.model()
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['pw']
        query = db(db.user.email == email)
        if query.isempty() is True:
            password = sha256_crypt.encrypt(password)
            db.user.insert(name=name, email=email, password=password)
            db.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')
