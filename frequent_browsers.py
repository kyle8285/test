import sqlite3

conn = sqlite3.connect('db/testdb.db')
c = conn.cursor()

c.execute('DELETE FROM frequent_browsers')

query = """
    WITH ranked_visitors AS (
        SELECT
            personId,
            count(DISTINCT siteId) as num_sites_visited,
            rank() over (ORDER BY count(DISTINCT siteId) DESC) AS rank
        FROM visits
        GROUP BY personId
        ORDER BY num_sites_visited DESC
    )
    INSERT INTO frequent_browsers (person_id, num_sites_visited)
        SELECT personId, num_sites_visited
        FROM ranked_visitors
        WHERE rank <= 10;
"""

c.execute(query)

c.execute('SELECT * FROM frequent_browsers')

for row in c.fetchall():
    print('person_id: {}, num_sites_visited: {}'.format(row[0], row[1]))

conn.commit()
c.close()
