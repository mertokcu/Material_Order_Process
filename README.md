# Material_Order_Process

Part 0: Preparations

For this project, our task was to process a table of orders to a 3D printing company. We got the orders as a CSV file, each row is an individual order for printing one kind of 3D shape and we had to make a table of required material for each week of orders.

First, we installed the necessary packages and read the dataset and examined it.

We used the function below to list the data in the "due by" column in the weekly format we wanted.

In this way, we will be able to make the classification we want with the "due week" column in our new "order" table.

Since we will record the materials specifically on a weekly basis, we stored each unique material and week in the data set as a list in a separate variable with the "unique" and “toList” function.

We then created a dataframe with this unique list of materials. Last but not least, we created an empty dictionary to store weekly material volume table.

There are orders of different shapes in the dataset. Since the volume of each of these shapes will be calculated with different formulations, we wrote a separate volume calculation function for each specific shape.


Part1: Execution

Using the relevant functions, we processed each order to add volumes to the material table that we created. 

Finally, we completed the project by creating separate csv files on a weekly basis.
