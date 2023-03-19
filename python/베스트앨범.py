from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_genres = defaultdict(int) # 장르별 재생횟수
    song_plays = defaultdict(list) # {재생횟수, 고유번호} 리스트
    
    # 각 장르별로 노래 정보를 저장
    for i in range(len(genres)):
        total_genres[genres[i]] += plays[i]
        song_plays[genres[i]].append((plays[i], i))
        
    # 장르별 정렬
    total_genres = dict(sorted(total_genres.items(), key=lambda x: x[1], reverse=True))

    for genre in total_genres:
        # 장르 내에서 많이 재생된 노래순으로 정렬
        song_plays[genre] = sorted(song_plays[genre], key=lambda x: (-x[0], x[1]))
        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
        for i in range(min(len(song_plays[genre]), 2)):
                answer.append(song_plays[genre][i][1])
        
    return answer
