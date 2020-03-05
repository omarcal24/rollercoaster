import pandas as pd
import matplotlib.pyplot as plt

wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
#print(wood.head())

steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#print(steel.head())

 

# write function to plot rankings over time for 1 roller coaster here:


def plot_coaster_ranking(coaster_name, park_name, material):
  if material == 'wood':
    select_all_coaster_datas = wood[(wood['Name'] == coaster_name) & (wood['Park'] == park_name)]
  if material == "steel":
    select_all_coaster_datas = steel[(steel['Name'] == coaster_name) & (steel['Park'] == park_name)]
  x_values = select_all_coaster_datas['Year of Rank']
  y_values = select_all_coaster_datas['Rank']
  plt.figure(figsize = (6,6))
  plt.plot(range(len(x_values)), y_values, marker = "o", linewidth = 3, color = "blue")
  ax = plt.subplot()
  ax.set_xticks(range(len(x_values)))
  ax.set_xticklabels(x_values)
  ax.invert_yaxis()
  plt.xlabel("Years Ranked")
  plt.ylabel("Ranking")
  plt.title("Ranking of " + coaster_name + "through these years")
  plt.show()
  

plot_coaster_ranking("El Toro", "Six Flags Great Adventure", "wood")







plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def plot_two_coasters_ranking(coaster_name_a, park_name_a, material_a, coaster_name_b, park_name_b, material_b):

 if material_a == 'wood':
    select_all_coaster_datas_a = wood[(wood['Name'] == coaster_name_a) & (wood['Park'] == park_name_a)]
 if material_b == "wood":
    select_all_coaster_datas_b = wood[(wood['Name'] == coaster_name_b) & (wood['Park'] == park_name_b)]
 if material_a == 'steel':
    select_all_coaster_datas_a = steel[(steel['Name'] == coaster_name_a) & (steel['Park'] == park_name_a)]
 if material_b == "steel":
    select_all_coaster_datas_b = steel[(steel['Name'] == coaster_name_b) & (steel['Park'] == park_name_b)]
 x_values_a = select_all_coaster_datas_a['Year of Rank']
 y_values_a = select_all_coaster_datas_a['Rank']
 plt.figure(figsize =(6,6))
 plt.plot(range(len(x_values_a)), y_values_a, marker='o', linewidth=3)
 ax = plt.subplot()
 ax.set_xticks(range(len(x_values_a)))
 ax.set_xticklabels(x_values_a)
 plt.xlabel('Yeas ranked')
 plt.ylabel('Ranking')
 plt.title('Comparing ' + coaster_name_a + ' vs ' + coaster_name_b)
                
 x_values_b = select_all_coaster_datas_b['Year of Rank']
 y_values_b = select_all_coaster_datas_b['Rank']
 plt.plot(range(len(x_values_b)), y_values_b, marker='o', linewidth=3)
    
 plt.legend([coaster_name_a, coaster_name_b])
 plt.show()

plot_two_coasters_ranking("El Toro", "Six Flags Great Adventure", "wood", "Boulder Dash", "Lake Compounce", "wood")








plt.clf()

# write function to plot top n rankings over time here:

def plot_top_n_rankings(material, n):
    top_n_rankings = material[material['Rank'] <= n]
    for rides in set(top_n_rankings['Name']):
        rides_rankings = top_n_rankings[top_n_rankings['Name'] == rides]
        plt.plot(rides_rankings['Year of Rank'], rides_rankings['Rank'], marker='o', label=rides)
    ax = plt.subplot()
    ax.invert_yaxis()
    plt.legend(loc=4)
    plt.title('Top ' + str(n) + ' Roller Coaster Rankings')
    plt.xlabel('Years')
    plt.ylabel('Rankings')
    plt.show()

plot_top_n_rankings(wood, 3)

plt.clf()

# load roller coaster data here:

roller_coasters = pd.read_csv("roller_coasters.csv")
print(roller_coasters.head(3))

# write function to plot histogram of column values here:

def plot_histogram(dataframe, column):
  data_of_column = dataframe[column]
  plt.hist(data_of_column.dropna(), normed = True)
  plt.title('Histogram of Roller Coaster {}'.format(column))
  plt.xlabel(column)
  plt.ylabel('Count')
  plt.show()
  
  
plot_histogram(roller_coasters, 'speed')
plot_histogram(roller_coasters, 'length')


plt.clf()

# write function to plot inversions by coaster at a park here:

def plot_bar_inversions(dataframe, park):
   park_data = dataframe[dataframe.park == park]
   data_inversions = park_data.num_inversions
   rollercoaster_name = park_data.park
   plt.bar(range(len(rollercoaster_name)), data_inversions)
   plt.title('Inversions')
   plt.xlabel('Roller Coaster')
   plt.ylabel('Inverions')
   ax = plt.subplot()
   ax.set_xticks(range(len(rollercoaster_name)))
   ax.set_xticklabels(rollercoaster_name, rotation=90)
   plt.show()
  
  

plot_bar_inversions(roller_coasters, 'Bobbejaanland')


plt.clf()
    
# write function to plot pie chart of operating status here:

def plot_pie_operating(dataframe):
   operative = dataframe.status == 'status.operating'
   closed = dataframe.status == 'status.closed.definitely'
  
   quantity_operative = len(operative)
   quantity_closed = len(closed)
   plt.pie([quantity_operative, quantity_closed], autopct='%1.1f%%', shadow=True)
   plt.axis("equal")
   plt.title("Operative vs Closed rides")
   plt.legend(["Operative", "Closed"])
   plt.show()
  
plot_pie_operating(roller_coasters)  

plt.clf()
  
# write function to create scatter plot of any two numeric columns here:

def scatter_plot(dataframe, column1, column2):
  data_column1 = dataframe[column1]
  data_column2 = dataframe[column2]
  plt.scatter(data_column1, data_column2)
  plt.title("Scatter plot of " + column1 + " and " + column2)
  plt.xlabel(column1)
  plt.ylabel(column2)
  plt.show()


scatter_plot(roller_coasters, "speed", "height")

plt.clf()