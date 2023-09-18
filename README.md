# MuseScribe
A structured search engine for sheet music.


## Inspiration

All of our team members have a passion for music and play or have played instruments. Oftentimes, we would find ourselves in a desperate hunt for the corresponding piece of sheet music to a melody we had stuck in our heads. Our search often leads nowhere as there is virtually no text to sheet music search engines. Moreover, audio to video searches were often unreliable, especially without a proper instrument on your hands.

Thus, we decided to create Musescribe, a music search engine that allows you to find sheet music to snippets of melodies that you remember.


## What it does
1. **Capture Your Melody:** Simply input the notes you have in mind using our intuitive interface that works similarly to how Lilypond, a text based music engraver takes in inputs. 

2. **Magic of Music Recognition:** Musescribe pattern matches the melody you've provided, no matter how simple or complex it may be.

3. **Find Your Music:** Within moments, Musescribe scours our database of sheet music, matching your melody to a wide array of musical compositions.

## How we built it
Overall, we created a project that can process user queries containing LilyPond-style musical notation, translate them into MIDI values and durations, and store and retrieve musical scores using a graph database. There are 5 main parts to our project:

1. Query Language with LilyPond Notation:
We defined a query language for processing musical notation using LilyPond notation. This query language allows users to input musical notations, including pitch, accidentals, and octaves, and we parse these inputs into note values and durations.

2. Kuzu Database:
We used the Kuzu database to store and manage music-related data. Kuzu is a graph database that we used to model our musical data, including songs, parts, and notes.

3. Importing Scores:
We created a function called import_score that takes a musical score object (in a standard format, MusicXML) and imports it into our Kuzu database. This function creates nodes and relationships in the database to represent songs, parts, and notes.

4. Database Schema Setup:
We defined the schema for our Kuzu database, including node types such as "Song," "Part," and "Note," and the relationships between them.

5. Processing and Storing Musical Data:
Our code processes and stores musical data in a structured way, allowing for efficient querying and retrieval of musical information based on user input.

## Challenges we ran into
1. Figuring out how to represent melodies into a text 
2. Implementing grammar for our query engine

## Accomplishments that we're proud of
Using Kuzu to elegantly find sequences of notes was satisfying especially since learning the Cypher query language took much effort.

## What we learned
1. Learned to use Kuzu database
2. Learned to write cypher query language
3. Learned to represent musical notes in strings


## What's next for Musescript

1. Integrate more music into the Musescript database:
It’s difficult to find large amounts of openly accessible sheet music on the internet. In order to fully test and exemplify the reliability of our search engine, we need to work with a greater amount of data from various genres of music. 
2. Add more functionality that incorporates musical elements beyond melodies:
We hope to add search functionality for rhythms, time signatures, chord progressions, and more. This will ideally make searches more refined. Lilypond-style inputs do support the writing of the above elements in a text-based manner.



## What languages, frameworks, platforms, cloud services, databases, APIs, or other technologies did you use?

1. Programming Languages:
- Python: We wrote primarily in Python, which is used for parsing LilyPond notation, working with the Kuzu graph database, and other project-related tasks.

2. Frameworks:
- Flask: We used Flask to build a web interface for our project.

3. Databases:
- Kuzu Database: We used the Kuzu graph database to store and manage musical data. Kuzu is the graph database solution that allows us to model and query our data as a graph.

4. Web Technologies:
- HTML: We wrote HTML code for the web interface. Designed Logo, animations, and drop-down features.

5. Cloud Environment:
- Repl.it: for writing code, collaboration, and deploying website

6. Music Notation Software:
- LilyPond: LilyPond is a music engraving program we used for rendering musical notation based on user inputs. It's a text-based music notation system.

7. IDEs/Editors:
- Repl.it to write and test our Python code.

8. MusicXML:
- MusicXML format for importing and working with musical scores

9. Query Language:
- We used Cypher, a highly graph-based data model, to represent the notes as nodes and the relationships between each note. This allows for more specific querying and filtering based on node and relationship types. 
- Cypher queries use a pattern-based approach to match and retrieve data from the graph. 
- We also chose Cypher for its readability as well as declarative Syntax (we specify what we want to retrieve from the database without specifying how to do it. The database engine optimizes the query execution.)
