from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objects as go

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = int(request.form['year'])  # Read the year input
    country = request.form['country']  # Read the country input
    
    print(f"Received year: {year}, country: {country}")  # Debug print

    # Filter the dataset for the given year and country
    data = df[(df['Year'] == year) & (df['Country'] == country)]
    
    print(f"Filtered data: {data}")  # Debug print
    
    if data.empty:
        return render_template('index.html', error="No data available for the specified year and country.")

    # Customizing the plot for Sea Level
    fig_sea_level = go.Figure(data=go.Scatter(
        x=data['Country'], 
        y=data['SeaLevel'], 
        mode='lines+markers+text', 
        line=dict(color='red', width=2),
        marker=dict(color='cyan', size=8),
        text=data['SeaLevel'],
        textposition='top center'
    ))
    fig_sea_level.update_layout(
        title=f'Sea Level in {year} for {country}',
        xaxis=dict(title='Country', showgrid=True, gridcolor='black', tickmode='array'),
        yaxis=dict(title='SeaLevel', showgrid=True, gridcolor='black'),
        plot_bgcolor='white'
    )
    graph_sea_level = fig_sea_level.to_html(full_html=False)

    # Customizing the plot for Agricultural Yield
    fig_agri_yield = go.Figure(data=go.Scatter(
        x=data['Country'], 
        y=data['AgriculturalYield'], 
        mode='lines+markers+text', 
        line=dict(color='red', width=2),
        marker=dict(color='cyan', size=8),
        text=data['AgriculturalYield'],
        textposition='top center'
    ))
    fig_agri_yield.update_layout(
        title=f'Agricultural Yield in {year} for {country}',
        xaxis=dict(title='Country', showgrid=True, gridcolor='black', tickmode='array'),
        yaxis=dict(title='AgriculturalYield', showgrid=True, gridcolor='black'),
        plot_bgcolor='white'
    )

    graph_agri_yield = fig_agri_yield.to_html(full_html=False)

    return render_template('index.html', graph_sea_level=graph_sea_level, graph_agri_yield=graph_agri_yield)

if __name__ == '__main__':
    app.run(debug=True)
