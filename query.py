from typing import List, Tuple
# https://lilypond.org/
# https://lilypond.org/text-input.html
import re

NOTE_GRAMMAR = r"(?P<pitch>a|b|c|d|e|f|g)(?P<accidental>((?:is){1,2}|(?:es){1,2}))?(?P<octave>('+|,+))?(?P<duration>1|2|4|8|16|32|64)?"

def translate_query(query: str) -> List[Tuple[int, int]]:
    """
    First member of pair: MIDI Note value (see https://en.wikipedia.org/wiki/Piano_key_frequencies)
    Second of pair: Note duration
    """

    notes = []

    for match in re.finditer(NOTE_GRAMMAR, query):
        print(match.group(0))
      
        # get duration
        duration_str = match.group('duration')
        if duration_str != None:
            duration = int(duration_str)
        else:
            duration = notes[-1][1]
    
        # get MIDI note value
        midi = 48        # start at middle C
        
        # add pitch
        pitch = match.group('pitch')
        pitches = 'c d ef g a b'
        midi += pitches.index(pitch)

        # add octaves
        if match.group('octave'):
            if match.group('octave')[0] == "'":
                direc = 1
            else:
                direc = -1
            numOctaves = len(match.group('octave'))
            midi += 12*direc*numOctaves
    
        # add accidentals
        accidentals = match.group('accidental')
        if accidentals:
            direction = 1 if 'is' in accidentals else -1
            midi += direction * (len(accidentals) // 2)
            
        notes.append((midi, duration))
    
    return notes

import kuzu

db = kuzu.Database('./musescribe')
conn = kuzu.Connection(db)

def list_of_params(l: list):
    return [
        (str(key), value)
        for (key, value)
        in enumerate(l, 1)
    ]

def all_results(result):
    l = []
    columns = result.get_column_names()
    while result.has_next():
        l.append(dict(zip(columns, result.get_next())))
    return l

def search(query: str):
    notes = translate_query(query)

    note_chain = "-[:NextNote]->".join(f'(n{i}:Note)' for i in range(1, len(notes) + 1))
    note_where = " AND ".join(f'n{i}.value = ${i}' for i in range(1, len(notes) + 1))
    query = f"""MATCH {note_chain}, (n1)-[:NoteOf]->(p:Part)-[:PartOf]->(s:Song)
WHERE {note_where}
RETURN n1.time_point, p.name, s.title, s.composer, s.id"""
    return all_results(
        conn.execute(
            query,
            list_of_params(value for value, duration in notes)
        )
    )
