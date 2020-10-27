# Map-Expansion-and-Contraction
Title of Project :- Contraction and expansion of map and derive nearby locations/cities between two locations.

Brief Description Of Project :-

UI Part :- We had designed a UI which had the following components :-

1. Source :- Here we will take the source vertex.

2. Destination :- Here we will take the destination vertex.

3. Show Button :- On clicking it shows the source and destination vertex on to the console and opens and saves the map in the location specified.

4. Zoom in(+) Button :- On clicking it we zoom in to the map so the number of cities increases between the source and destination vertex.

5. Zoom Out(-) Button :- On clicking it we zoom out of the map so the number of cities decreases between the source and destination vertex.

6. Quit Button :- On clicking it the GUI closes.

Libraries Used :-

1. Folium :- We Used it to get the map and uses its inbuilt methods such as Map , Marker for implementing the desired result i.e. to get the map and plot the source and destination vertex on the map and to plot other cities which lies between them on zooming in and out from the  map .

2. CSV :- It is basically used to acces a dataset which has approximately 220 cities with their longitude and latitude coordinates which helps us to plot the cities by getting the coordinates of the city and plotting it on the map using the Folium library.

3. Tkinter :- It is used for making the desired User Interface which has the components defined earlier .

4. Webbrowser :- It is used to open the new tab with applied changes

Functioning :- We are going to take the source and destination vertices and then click on the show button which shows the input cities in the console and opens the saved map . Then when we click the zoom in button the number of cities between the input cities increases as we plot the cities within a specific range related to the cities and same goes with the zoom out button , the number of cities decreases as we then plot the cities with the changed range . But to apply change we had to reload the html page in order to get the updated map . On the other hand when we click the zoom in or zoom out button , an array is created with the name of nearby cities between the input cities and gets displayed on the UI.
