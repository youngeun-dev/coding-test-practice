SELECT ins.animal_id, ins.name
FROM animal_ins ins, animal_outs outs
WHERE ins.animal_id = outs.animal_id and ins.datetime > outs.datetime
ORDER BY ins.datetime
