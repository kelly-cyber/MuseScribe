import partitura as pt
from partitura.score import Score, Note
# https://kuzudb.com/docusaurus/cypher/
import kuzu
from pathlib import Path 

db = kuzu.Database('./musescribe')
conn = kuzu.Connection(db)

with open("setup.cypher") as f:
    for line in f:
        print(line)
        conn.execute(line)

def list_of_params(l: list):
    return [
        (str(key), value)
        for (key, value)
        in enumerate(l, 1)
    ]

def import_score(score: Score, path: Path):
    score_id = score.id or path.stem
    conn.execute('CREATE (s:Song {id: $1, title: $2, composer: $3})', list_of_params([score_id, score.title or '', score.composer or '']))

    for part in score:
        part_id = f"{score_id}::{part.id}"

        print(part.id)
        
        conn.execute(
            'CREATE (p:Part {id: $4, part_id: $1, song_id: $2, name: $3})',
            list_of_params([
                part.id,
                score_id,
                part.part_name or '',
                part_id,
            ])
        )
        conn.execute(
            "MATCH (p:Part), (s:Song) WHERE s.id = $1 AND p.id = $2 CREATE (p)-[:PartOf]->(s)",
            list_of_params([
                score_id,
                part_id,
            ])
        )

        point = part.first_point
        prev_notes = set()

        while point:
            notes = point.starting_objects[Note]

            note_ids = set()

            for i, note in enumerate(notes):
                note_id = f"{score_id}::{part.id}::{point.t}::{i}"
                note_ids.add(note_id)
                
                conn.execute(
                    'CREATE (n:Note {id: $1, part_id: $2, song_id: $3, time_point: $4, value: $5})',
                    list_of_params([
                        note_id,
                        part_id,
                        score_id,
                        point.t,
                        note.midi_pitch,
                    ])
                )

                conn.execute(
                    "MATCH (n:Note), (p:Part) WHERE n.id = $1 AND p.id = $2 CREATE (n)-[:NoteOf]->(p)",
                    list_of_params([
                        note_id,
                        part_id,
                    ])
                )

                for prev_note in prev_notes:
                    conn.execute(
                        "MATCH (n:Note), (n_prev:Note) WHERE n.id = $1 AND n_prev.id = $2 CREATE (n_prev)-[:NextNote]->(n)",
                        list_of_params([
                            note_id,
                            prev_note,
                        ])
                    )
            
            prev_notes = note_ids
            point = point.next

for path in Path("schema_annotation_data/data/mozart_sonatas/musicxml/").glob("*.xml"):
    score = pt.load_musicxml(path)
    import_score(score, path)
    