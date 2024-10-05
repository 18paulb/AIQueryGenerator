import sqlite3

def create_tables():
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()

    # Drop tables to reset the database
    cursor.execute('DROP TABLE IF EXISTS Superhero;')
    cursor.execute('DROP TABLE IF EXISTS Power;')
    cursor.execute('DROP TABLE IF EXISTS Superhero_Power;')

    # Create superheroes table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SuperHero (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        real_name TEXT,
        universe TEXT CHECK(universe IN ('DC', 'Marvel'))
    );
    ''')

    # Create powers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Power (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        power_name TEXT NOT NULL
    );
    ''')

    # Create superhero_powers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Superhero_Power (
        superhero_id INTEGER NOT NULL,
        power_id INTEGER NOT NULL,
        PRIMARY KEY (superhero_id, power_id),
        FOREIGN KEY (superhero_id) REFERENCES Superhero(id) ON DELETE CASCADE,
        FOREIGN KEY (power_id) REFERENCES Power(id) ON DELETE CASCADE
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Team (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Superhero_Team (
        superhero_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        PRIMARY KEY (superhero_id, team_id),
        FOREIGN KEY (superhero_id) REFERENCES Superhero(id) ON DELETE CASCADE,
        FOREIGN KEY (team_id) REFERENCES Team(id) ON DELETE CASCADE          
    );
    ''')
                   
    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def insert_data():
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()
    
    # Insert into SuperHero table
    cursor.execute('''
    INSERT INTO SuperHero (name, real_name, universe) 
    VALUES 
        ('Superman', 'Clark Kent', 'DC'),
        ('Iron Man', 'Tony Stark', 'Marvel'),
        ('Wonder Woman', 'Diana Prince', 'DC'),
        ('Spider-Man', 'Peter Parker', 'Marvel'),
        ('Batman', 'Bruce Wayne', 'DC');
    ''')

    # Insert into Power table
    cursor.execute('''
    INSERT INTO Power (power_name) 
    VALUES 
        ('Flight'),
        ('Super Strength'),
        ('Intelligence'),
        ('Web-Slinging'),
        ('Combat Skills');
    ''')

    # Insert into Superhero_Power table
    cursor.execute('''
    INSERT INTO Superhero_Power (superhero_id, power_id) 
    VALUES 
        (1, 1), (1, 2),  -- Superman has Flight and Super Strength
        (2, 3),          -- Iron Man has Intelligence
        (3, 1), (3, 5),  -- Wonder Woman has Flight and Combat Skills
        (4, 4), (4, 2),  -- Spider-Man has Web-Slinging and Super Strength
        (5, 5), (5, 3);  -- Batman has Combat Skills and Intelligence
    ''')

    # Insert into Team table
    cursor.execute('''
    INSERT INTO Team (name)
    VALUES
        ('The Avengers'),
        ('Justice League');
    ''')

    # Insert into Superhero_Team table
    cursor.execute('''
    INSERT INTO Superhero_Team (superhero_id, team_id)
    VALUES
        (1, 2),  -- Superman is in Justice League
        (2, 1),  -- Iron Man is in The Avengers
        (3, 2),  -- Wonder Woman is in Justice League
        (5, 2);  -- Batman is in Justice League
    ''')

    conn.commit()
    conn.close()


    

def getSchema():
    return """
    CREATE TABLE IF NOT EXISTS SuperHero (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        real_name TEXT,
        universe TEXT CHECK(universe IN ('DC', 'Marvel'))
    );

    CREATE TABLE IF NOT EXISTS Power (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        power_name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Superhero_Power (
        superhero_id INTEGER NOT NULL,
        power_id INTEGER NOT NULL,
        PRIMARY KEY (superhero_id, power_id),
        FOREIGN KEY (superhero_id) REFERENCES Superhero(id) ON DELETE CASCADE,
        FOREIGN KEY (power_id) REFERENCES Power(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS Team (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Superhero_Team (
        superhero_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        PRIMARY KEY (superhero_id, team_id),
        FOREIGN KEY (superhero_id) REFERENCES Superhero(id) ON DELETE CASCADE,
        FOREIGN KEY (team_id) REFERENCES Team(id) ON DELETE CASCADE          
    );
    """

def executeQuery(query):
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()

    response = []
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        for row in results:
            # print(row)
            response.append(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

    return response


# create_tables()

# insert_data()