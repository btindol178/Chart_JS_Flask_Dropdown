# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, render_template,request
import pandas as pd

app = Flask(__name__)

df_scatter = pd.DataFrame({
      'sales':  [2115, 1562, 1584, 1892, 1487, 2223, 2966, 2448, 2905, 3838, 2917, 3327],
      'orders':[958, 724, 629, 883, 915, 1214, 1476, 1212, 1554, 2128, 1466, 1827],
      'months': ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
   })
@app.route('/')
@app.route('/apexdropdown',methods=['GET','POST'])
def apextutorialdropdown():
    # Bring in csv... print it.. pd.read_csv for example 
    print(type(df_scatter['sales'])) # series 
    print(df_scatter.dtypes)
    #############################################
    # Change columns to list.. 
    #values = [10, 41, 35, 51, 49, 62, 69, 91, 148]
    #months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    sales = df_scatter['sales'].to_list()
    orders = df_scatter['orders'].to_list()
    months = df_scatter['months'].to_list()

    #print(values2)
    dataObject = {
        "sales":sales,
        "orders":orders,
        "months":months
    }
    if request.method == 'POST':
        
        var1 = int(request.form['id']) # Need to make the column same type as eachother int is values column in df
        print(type(var1))
        print(var1)

        df2 = df_scatter[df_scatter['sales'] != var1]#.astype(str) # was used to make the int column string to match types
        print(df_scatter)
        print(df2)
        
        sales = df2['sales'].to_list()
        orders = df2['orders'].to_list()
        months = df2['months'].to_list()

        dataObject = {
        "sales":sales,
        "orders":orders,
        "months":months
    }

        return render_template('home/apex-chart-tutorial2.html',dataObject=dataObject)
    return render_template('home/apex-chart-tutorial2.html',dataObject=dataObject)
if __name__=="__main__":
    app.run(debug=True)
