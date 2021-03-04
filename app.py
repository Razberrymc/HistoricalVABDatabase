from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
app.secret_key = "OhManIHopeThisFlaskAppWorks"
app.debug = True

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'MClark'
app.config['MYSQL_DATABASE_PASSWORD'] = 'EmporiaBounty98'
app.config['MYSQL_DATABASE_DB'] = 'MClark$default'
app.config['MYSQL_DATABASE_HOST'] = 'MClark.mysql.pythonanywhere-services.com'
mysql.init_app(app)

@app.route('/')
def Index():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM employee')
    data = cur.fetchall()

    cur.close()
    return render_template('index.html', employee = data)

@app.route('/add_contact', methods=['POST'])
def add_employee():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        parcel = request.form['parcel']
        roll = request.form['roll']
        petition = request.form['petition']
        pacs = request.form['pacs']
        zoning = request.form['zoning']
        tang = request.form['tang']
        cost = request.form['cost']
        sale = request.form['sale']
        income = request.form['income']
        occupancy = request.form['occupancy']
        build = request.form['build']
        quality = request.form['quality']
        age = request.form['age']
        condition = request.form['condition']
        priceSquare = request.form['priceSquare']
        buildImpr = request.form['buildImpr']
        extraFeature = request.form['extraFeature']
        estLandVal = request.form['estLandVal']
        totalCostAppr = request.form['totalCostAppr']
        propApprMarketVal = request.form['propApprMarketVal']
        potentialGrossIncome = request.form['potentialGrossIncome']
        lessVacanciesAndCollections = request.form['lessVacanciesAndCollections']
        effectiveGrossIncome = request.form['effectiveGrossIncome']
        lessOperatingExpenses = request.form['lessOperatingExpenses']
        netOperatingIncome = request.form['netOperatingIncome']
        capRate = request.form['capRate']
        plusEffectiveTaxRate = request.form['plusEffectiveTaxRate']
        overallRate = request.form['overallRate']
        estimatedMarketVal = request.form['estimatedMarketVal']
        cost_comp1_parcel = request.form['cost_comp1_parcel']
        cost_comp1_sale_price = request.form['cost_comp1_sale_price']
        cost_comp1_size = request.form['cost_comp1_size']
        cost_comp1_price_per_square = request.form['cost_comp1_price_per_square']
        cost_comp2_parcel = request.form['cost_comp2_parcel']
        cost_comp2_sale_price = request.form['cost_comp2_sale_price']
        cost_comp2_size = request.form['cost_comp2_size']
        cost_comp2_price_per_square = request.form['cost_comp2_price_per_square']
        cost_comp3_parcel = request.form['cost_comp3_parcel']
        cost_comp3_sale_price = request.form['cost_comp3_sale_price']
        cost_comp3_size = request.form['cost_comp3_size']
        cost_comp3_price_per_square = request.form['cost_comp3_price_per_square']
        cur.execute("INSERT INTO employee (parcel, roll, petition, pacs, zoning, tang, cost, sale, income, occupancy, build, quality, age, `condition`, priceSquare, buildImpr, extraFeature, estLandVal, totalCostAppr, propApprMarketVal, potentialGrossIncome, lessVacanciesAndCollections, effectiveGrossIncome, lessOperatingExpenses, netOperatingIncome, capRate, plusEffectiveTaxRate, overallRate, estimatedMarketVal, cost_comp1_parcel, cost_comp1_sale_price, cost_comp1_size, cost_comp1_price_per_square, cost_comp2_parcel, cost_comp2_sale_price, cost_comp2_size, cost_comp2_price_per_square, cost_comp3_parcel, cost_comp3_sale_price, cost_comp3_size, cost_comp3_price_per_square) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (parcel, roll, petition, pacs, zoning, tang, cost, sale, income, occupancy, build, quality, age, condition, priceSquare, buildImpr, extraFeature, estLandVal, totalCostAppr, propApprMarketVal, potentialGrossIncome, lessVacanciesAndCollections, effectiveGrossIncome, lessOperatingExpenses, netOperatingIncome, capRate, plusEffectiveTaxRate, overallRate, estimatedMarketVal, cost_comp1_parcel, cost_comp1_sale_price, cost_comp1_size, cost_comp1_price_per_square, cost_comp2_parcel, cost_comp2_sale_price, cost_comp2_size, cost_comp2_price_per_square, cost_comp3_parcel, cost_comp3_sale_price, cost_comp3_size, cost_comp3_price_per_square))
        conn.commit()
        flash('Entry Added Successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', employee = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_employee(id):
    if request.method == 'POST':
        parcel = request.form['parcel']
        roll = request.form['roll']
        petition = request.form['petition']
        pacs = request.form['pacs']
        zoning = request.form['zoning']
        tang = request.form['tang']
        cost = request.form['cost']
        sale = request.form['sale']
        income = request.form['income']
        occupancy = request.form['occupancy']
        build = request.form['build']
        quality = request.form['quality']
        age = request.form['age']
        condition = request.form['condition']
        priceSquare = request.form['priceSquare']
        buildImpr = request.form['buildImpr']
        extraFeature = request.form['extraFeature']
        estLandVal = request.form['estLandVal']
        totalCostAppr = request.form['totalCostAppr']
        propApprMarketVal = request.form['propApprMarketVal']
        potentialGrossIncome = request.form['potentialGrossIncome']
        lessVacanciesAndCollections = request.form['lessVacanciesAndCollections']
        effectiveGrossIncome = request.form['effectiveGrossIncome']
        lessOperatingExpenses = request.form['lessOperatingExpenses']
        netOperatingIncome = request.form['netOperatingIncome']
        capRate = request.form['capRate']
        plusEffectiveTaxRate = request.form['plusEffectiveTaxRate']
        overallRate = request.form['overallRate']
        estimatedMarketVal = request.form['estimatedMarketVal']
        cost_comp1_parcel = request.form['cost_comp1_parcel']
        cost_comp1_sale_price = request.form['cost_comp1_sale_price']
        cost_comp1_size = request.form['cost_comp1_size']
        cost_comp1_price_per_square = request.form['cost_comp1_price_per_square']
        cost_comp2_parcel = request.form['cost_comp2_parcel']
        cost_comp2_sale_price = request.form['cost_comp2_sale_price']
        cost_comp2_size = request.form['cost_comp2_size']
        cost_comp2_price_per_square = request.form['cost_comp2_price_per_square']
        cost_comp3_parcel = request.form['cost_comp3_parcel']
        cost_comp3_sale_price = request.form['cost_comp3_sale_price']
        cost_comp3_size = request.form['cost_comp3_size']
        cost_comp3_price_per_square = request.form['cost_comp3_price_per_square']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE employee
            SET parcel = %s,
                roll = %s,
                petition = %s,
                pacs = %s,
                zoning = %s,
                tang = %s,
                cost = %s,
                sale = %s,
                income = %s,
                occupancy = %s,
                build = %s,
                quality = %s,
                age = %s,
                `condition` = %s,
                priceSquare = %s,
                buildImpr = %s,
                extraFeature = %s,
                estLandVal = %s,
                totalCostAppr = %s,
                propApprMarketVal = %s,
                potentialGrossIncome = %s,
                lessVacanciesAndCollections = %s,
                effectiveGrossIncome = %s,
                lessOperatingExpenses = %s,
                netOperatingIncome = %s,
                capRate = %s,
                plusEffectiveTaxRate = %s,
                overallRate = %s,
                estimatedMarketVal = %s,
                cost_comp1_parcel = %s,
                cost_comp1_sale_price = %s,
                cost_comp1_size = %s,
                cost_comp1_price_per_square = %s,
                cost_comp2_parcel = %s,
                cost_comp2_sale_price = %s,
                cost_comp2_size = %s,
                cost_comp2_price_per_square = %s,
                cost_comp3_parcel = %s,
                cost_comp3_sale_price = %s,
                cost_comp3_size = %s,
                cost_comp3_price_per_square = %s
            WHERE id = %s
        """, (parcel, roll, petition, pacs, zoning, tang, cost, sale, income, occupancy, build, quality, age, condition, priceSquare, buildImpr, extraFeature, estLandVal, totalCostAppr, propApprMarketVal, potentialGrossIncome, lessVacanciesAndCollections, effectiveGrossIncome, lessOperatingExpenses, netOperatingIncome, capRate, plusEffectiveTaxRate, overallRate, estimatedMarketVal, cost_comp1_parcel, cost_comp1_sale_price, cost_comp1_size, cost_comp1_price_per_square, cost_comp2_parcel, cost_comp2_sale_price, cost_comp2_size, cost_comp2_price_per_square, cost_comp3_parcel, cost_comp3_sale_price, cost_comp3_size, cost_comp3_price_per_square, id))
        flash('Entry Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_employee(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('DELETE FROM employee WHERE id = {0}'.format(id))
    conn.commit()
    flash('Entry Removed Successfully')
    return redirect(url_for('Index'))

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
