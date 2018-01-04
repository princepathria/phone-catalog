from flask import render_template, request, url_for, redirect, flash, jsonify
from settings import app, db
from database_setup import Company, Phone

@app.route('/company/<int:comp_id>/JSON')
def restaurantMenuJSON(comp_id):
    comp = Company.query.filter_by(
        id=comp_id
    ).one()
    items = Phone.query.filter_by(company_id=comp.id).all()
    return jsonify(allPhones=[i.serialize for i in items])


# ADD JSON ENDPOINT HERE
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    a = Company.query.all()
    output = ''
    for item in a:
        output = output + item.name
        output = output + '<br>'
    return output


@app.route('/company/<int:var>/')
@app.route('/company/<string:var>/')
def products(var):
    dbC = Company
    dbCq = dbC.query
    dbPq = Phone.query
    if type(var) is str:
        brand = dbCq.filter(db.func.lower(dbC.name) == var.lower()).first()
        phones = dbPq.filter_by(company_id=brand.id)
        return render_template('phone.html', company=brand, products=phones)
    if type(var) is int:
        brand = dbCq.filter_by(id=var).first()
        phones = dbPq.filter_by(company_id=brand.id)
        return render_template('phone.html', company=brand, products=phones)


@app.route('/company/<int:var>/new/', methods=['GET', 'POST'])
def newPhone(var):
    if request.method == 'POST':
        newphone = Phone(
            name=request.form['name'], company_id=var)
        db.session.add(newphone)
        db.session.commit()
        flash("new phone created!")
        return redirect(url_for('products', var=var))
    else:
        return render_template('newphone.html', company_id=var)


@app.route('/company/<int:var>/<int:phone_id>/edit/', methods=['GET', 'POST'])
def editPhone(var, phone_id):
    editphone = Phone.query.filter_by(
        id=phone_id
    ).one()
    ph_name = editphone.name
    if request.method == 'POST':
        if request.form['name']:
            editphone.name = request.form['name']
        redirect(url_for('products', var=var))
        db.object_session(editphone).add(editphone)
        db.object_session(editphone).commit()
        flash("Phone has been edited")
        return redirect(url_for('products', var=var))
    else:
        return render_template('editphone.html', company_id=var, phone=phone_id, phonename=ph_name)


@app.route('/company/<int:var>/<int:phone_id>/delete/', methods=['GET', 'POST'])
def deletePhone(var, phone_id):
    itemToDelete = Phone.query.filter_by(id=phone_id).one()
    if request.method == 'POST':
        db.object_session(itemToDelete).delete(itemToDelete)
        db.object_session(itemToDelete).commit()
        flash("Phone has been deleted")
        return redirect(url_for('products', var=var))
    else:
        return render_template('deletephone.html', phone=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000, debug=True)
