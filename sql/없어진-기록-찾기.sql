SELECT outs.animal_id, outs.name
FROM animal_outs outs
    LEFT JOIN animal_ins ins
    ON outs.animal_id = ins.animal_id
WHERE ins.animal_id IS NULL;
