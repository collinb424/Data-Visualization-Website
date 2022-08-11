import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Reads in Alcohol Consumption File
fh = open('alcohol_consumption.csv')
alcohol_reader = csv.reader(fh)
alcohol_table = []
for row in alcohol_reader:
  alcohol_table.append(row)
fh.close()
country_list = []
alcohol_list = []
age_list = []
first_row = True
for row in alcohol_table:
  if first_row:
    first_row = False
    continue
  country_list.append(row[0])
  alcohol_list.append(row[1])
  age_list.append(row[4])

# Reads in Happiness Index File
fh = open('happiness_data.csv')
happiness_reader = csv.reader(fh)
happiness_table = []
for row in happiness_reader:
  happiness_table.append(row)
fh.close()
country_list2 = []
score_list = []
gdp_list = []
first_row = True
for row in happiness_table:
  if first_row:
    first_row = False
    continue
  country_list2.append(row[1])
  score_list.append(row[2])
  gdp_list.append(row[3])

countries = []
alcohol = []
happiness = []
gdp = []
age = []

for i in range(len(country_list)):
  for j in range(len(country_list2)):
    if (country_list[i] == country_list2[j]):
      countries.append(country_list[i])
      alcohol.append(float(alcohol_list[i]))
      age.append(int(age_list[i]))
      happiness.append(float(score_list[j]))
      gdp.append(float(gdp_list[j]))

iso = ['LVA', 'MDA', 'DEU', 'LTU', 'IRL', 'ESP', 'UGA', 'BGR', 'LUX', 'ROU', 'MNE', 'FRA', 'SVN', 'PRT', 'LAO', 'TZA', 'AUT', 'POL', 'GBR', 'CHE', 'HUN', 'SVK', 'BFA', 'BLR', 'CYP', 'BEL', 'EST', 'NZL', 'FIN', 'GRC', 'RUS', 'AUS', 'DNK', 'JPN', 'USA', 'NLD', 'GEO', 'ARG', 'ZAF', 'ISL', 'SWE', 'CHL', 'SRB', 'CAN', 'HRV', 'THA', 'KOR', 'UKR', 'MLT', 'GAB', 'ITA', 'RWA', 'VNM', 'KHM', 'BIH', 'PAN', 'BDI', 'BRA', 'NOR', 'PHL', 'PRY', 'URY', 'ALB', 'PER', 'DMA', 'BWA', 'MKD', 'NGA', 'CHN', 'MNG', 'IND', 'CMR', 'COL', 'LBR', 'SLE', 'LSO', 'NIC', 'MEX', 'KAZ', 'KGZ', 'MUS', 'ARM', 'ZWE', 'ZMB', 'ISR', 'JAM', 'SLV', 'MWI', 'CRI', 'HND', 'BOL', 'ARE', 'VEN', 'GMB', 'ECU', 'NAM', 'TKM', 'CIV', 'HTI', 'LKA', 'GHA', 'MOZ', 'TGO', 'UZB', 'BEN', 'ETH', 'KEN', 'MMR', 'TUN', 'SGP', 'MDG', 'TUR', 'CAF', 'GTM', 'LBN', 'QAT', 'MLI', 'TCD', 'COM', 'BHR', 'GIN', 'AZE', 'MYS', 'TJK', 'SEN', 'DZA', 'NPL', 'JOR', 'NER', 'MAR', 'IRQ', 'IDN', 'BTN', 'SYR', 'EGY', 'MRT', 'BGD']

# Makes a Data Frame
zipped_list = list(zip(happiness, alcohol, countries, gdp, iso, age))
df = pd.DataFrame(zipped_list, columns=['Happiness', 'Alcohol', 'Country', 'GDP Per Capita', 'Iso', 'Legal Drinking Age'])
fig = px.scatter(df, x='Happiness', y='Alcohol', labels={'Happiness':'Happiness Index Score', 'Alcohol':'Average Alcohol Consumption (L/Year)'}, trendline="ols", title='Alcohol Consumption vs Happiness Index')
print(df)
fig.show()

fig2 = px.scatter(df, x='GDP Per Capita', y='Alcohol', labels={'Alcohol':'Average Alcohol Consumption (L/Year)'}, trendline="ols", title='Alcohol Consumption vs GDP per Capita')
fig2.show()

fig3 = px.choropleth(df, locations='Iso', color='Alcohol', hover_name='Country', range_color=[0, 14], title='Alcohol Consumption by Country')
fig3.show()

fig4 = px.choropleth(df, locations='Iso', color='Happiness', hover_name='Country', range_color=[0, 8], title='Happiness Index by Country')
fig4.show()

fig5 = px.choropleth(df, locations='Iso', color='Legal Drinking Age', hover_name='Country', range_color=[0, 21], title='Legal Drinking Age by Country')
fig5.show()

fig6 = px.choropleth(df.sort_values(by=['Legal Drinking Age']), locations='Iso', color='Alcohol', hover_name='Country', animation_frame='Legal Drinking Age', range_color=[0, 14], title='Alcohol Consumption by Country for each Legal Drinking Age')
fig6.show()

fig7 = px.choropleth(df.sort_values(by=['Legal Drinking Age']), locations='Iso', color='Happiness', hover_name='Country', animation_frame='Legal Drinking Age', range_color=[0, 8], title='Happiness Index by Country for each Legal Drinking Age')
fig7.show()

fig8 = px.choropleth(df, locations='Iso', color='GDP Per Capita', hover_name='Country', range_color=[0, 1.7], title='GDP Per Capita by Country')
fig8.show()

fig9 = px.bar(df, x='Country', y='Alcohol', title='Alcohol Consumption by Country')
fig9.show()


# Embedding Graphs into HTML

# Figure 1 
fh = open('embed_fig.html', 'w')
fh.close()
pio.write_html(fig, file='embed_fig.html', auto_open=True, full_html=False)

# Figure 2
fh = open('embed_fig2.html', 'w')
fh.close()
pio.write_html(fig2, file='embed_fig2.html', auto_open=True, full_html=False)

# Figure 3
fh = open('embed_fig3.html', 'w')
fh.close()
pio.write_html(fig3, file='embed_fig3.html', auto_open=True, full_html=False)

# Figure 4
fh = open('embed_fig4.html', 'w')
fh.close()
pio.write_html(fig4, file='embed_fig4.html', auto_open=True, full_html=False)

# Figure 5
fh = open('embed_fig5.html', 'w')
fh.close()
pio.write_html(fig5, file='embed_fig5.html', auto_open=True, full_html=False)

# Figure 6
fh = open('embed_fig6.html', 'w')
fh.close()
pio.write_html(fig6, file='embed_fig6.html', auto_open=True, full_html=False)

# Figure 7
fh = open('embed_fig7.html', 'w')
fh.close()
pio.write_html(fig7, file='embed_fig7.html', auto_open=True, full_html=False)