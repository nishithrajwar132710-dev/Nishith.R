import pandas as pd
import plotly.express as px
# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}
df = pd.DataFrame(data)
# Bar chart for Sales
fig = px.bar(df, x='Product', y='Sales', title='Sales by Product')
fig.show()

fig = px.scatter(df, x='Sales', y='Profit', color='Product', title='Sales vs. Profit')
fig.show()

# Enhanced Bar chart
fig = px.bar(df, x='Product', y='Sales', 
             title='Sales by Product',
             color='Profit',  # Color by Profit
             text='Sales')    # Show sales value on bars

# Customize layout
fig.update_layout(xaxis_title='Product',
                  yaxis_title='Sales',
                  legend_title='Profit',
                  template='plotly_dark')  # Change template
fig.show()

# Save the figure as an HTML file
fig.write_html('sales_by_product.html')

# Save the figure as a PNG file (you may need to install kaleido)
fig.write_image('sales_by_product.png')

    
