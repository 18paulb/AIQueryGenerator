# Project Description

My database models Superheroes, Powers, and keeps track of what powers goes to what superhero.

# Question Examples

## Question 1

### Question
"Show me the info for every single superhero"

### SQL Query 
```
SELECT SuperHero.id, SuperHero.name, SuperHero.real_name, SuperHero.universe, Group_Concat(Power.power_name) AS powers
FROM SuperHero
LEFT JOIN Superhero_Power ON SuperHero.id = Superhero_Power.superhero_id
LEFT JOIN Power ON Superhero_Power.power_id = Power.id
GROUP BY SuperHero.id;
```

### Response
1. Hero Name: Superman
   Real Name: Clark Kent
   Universe: DC
   Powers: Flight, Super Strength

2. Hero Name: Iron Man
   Real Name: Tony Stark
   Universe: Marvel
   Powers: Intelligence

3. Hero Name: Wonder Woman
   Real Name: Diana Prince
   Universe: DC
   Powers: Flight, Combat Skills

4. Hero Name: Spider-Man
   Real Name: Peter Parker
   Universe: Marvel
   Powers: Super Strength, Web-Slinging

5. Hero Name: Batman
   Real Name: Bruce Wayne
   Universe: DC
   Powers: Intelligence, Combat Skills

## Question 2

### Question 
"Give me the superheroes who are not part of a team."

### SQL Query
```
SELECT SuperHero.name FROM SuperHero
LEFT JOIN Superhero_Team ON SuperHero.id = Superhero_Team.superhero_id
WHERE Superhero_Team.team_id IS NULL;
```

### Response
The query successfully retrieved the following result: Spider-Man.

## Question 3

### Question 
"Give me the superheroes who are part of a team."

### SQL Query
```
SELECT DISTINCT SuperHero.id, SuperHero.name
FROM SuperHero
JOIN Superhero_Team ON SuperHero.id = Superhero_Team.superhero_id;
```

### Response
Here are the superheroes from the query result:
1. Superman
2. Iron Man
3. Wonder Woman
5. Batman

## Question 4

### Question 
"Give me all superhero teams"

### SQL Query
```
SELECT T.name AS team_name FROM Team AS T;
```

### Response
Here are the movie titles from the SQL query result:

1. The Avengers
2. Justice League

## Question 5

### Question 
"Give me all superheroes who are on the 'Justice League' and have 'Super Strength' as a power"

### SQL Query
```
SELECT sh.name 
FROM Superhero sh 
JOIN Superhero_Team sht ON sh.id = sht.superhero_id 
JOIN Team t ON sht.team_id = t.id 
JOIN Superhero_Power shp ON sh.id = shp.superhero_id 
JOIN Power p ON shp.power_id = p.id 
WHERE t.name = 'Justice League' AND p.power_name = 'Super Strength';
```

### Response
"The query result is: Superman."

## Question 6

### Question 
"Give me all superheroes on 'The Avengers' that have the power 'Laser Vision'"

### SQL Query
```
SELECT sh.name 
FROM SuperHero AS sh
JOIN Superhero_Team AS sht ON sh.id = sht.superhero_id
JOIN Team AS t ON sht.team_id = t.id
JOIN Superhero_Power AS shp ON sh.id = shp.superhero_id
JOIN Power AS p ON shp.power_id = p.id
WHERE t.name = 'The Avengers' AND p.power_name = 'Laser Vision';
```

### Response
"We couldn't find any matching entries in our database."