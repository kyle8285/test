This is a demonstration working with SQL, Docker and Python. The purpose is to take an existing collection of data in a sqlite database and populate a new table. In this case, we want to find the ten people who have visited the most sites and list them in a table called `frequent_browsers`, in descending order based on the number of sites the respective person has visited.

Here are some implementation considerations and decisions:
- Are we concerned with the total number of visits across *all* sites or the total number of visits across *distinct* sites? 
    - This question (and answer) would lead to different results. My assumption is that we are more concerned with visits across *distinct* sites. I could see an argument for or against this depending on the use case. 

- How do we define the "top ten"? Is there a hard limit or requirement to only have ten results? What if there is a tie?
    - We can use window functions like `row_number`, `rank` and `dense_rank` to get a better idea of how these results would stack up. I went with the `rank` function to find the top ten visitors. Without more information it feels like the best compromise, as it will return at least ten results, but will also return the minimum number of results (up to and above ten) in the case of a tie. As you will see, there are actually 11 results in the table.

- The use of Docker was mostly an exercise to become more familiar with it. 

To run the solution utilizing a Docker container:

Clone or download the repository. Make sure you have Docker installed.

Run `docker build -t test .`

Run `docker run -v $(pwd)/db:/app/db test`

Note that the database we use for running the example is in the `./db` directory!

The results should be printed to the screen once the container has been run. I decided to use the volume so any updates made to the database would persist once the container had been shut down. With this in mind, you can now access the mounted database and verify that the table was in fact populated.

From the host current working directory:

`sqlite3 db/testdb.db`

will bring you into an interactive sqlite3 shell. Then you can run:

`SELECT * FROM frequent_browsers;` to view the contents of the table which was just populated.