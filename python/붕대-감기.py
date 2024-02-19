def solution(bandage, health, attacks):
    # t: 시전 시간, x: 초당 회복량, y: 추가 회복량
    t, x, y = bandage
    
    # 체력 범위
    min_health, max_health = 0, health 
    
    # 공격 시간
    attack_time = [int(attack[0]) for attack in attacks]
    
    # 연속 공격 횟수
    sequence_attack = 0
    
    for time in range(1, attack_time[-1] + 1):
        # 공격 
        if time in attack_time:
            health -= attacks[attack_time.index(time)][1]
            sequence_attack = 0
        # 회복
        else:
            sequence_attack += 1
            if sequence_attack // t >= 1:
                health += (sequence_attack // t) * y
            health += x

        # 체력 범위 체크 
        if health > max_health:
            health = max_health
        elif health <= min_health:
            health = -1
            break
        
    return health
