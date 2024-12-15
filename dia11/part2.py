from functools import lru_cache

def main():
    t = time.time()
    with open('input.txt') as f:
        stones = [int(stone) for stone in f.read().split()]

    blinks = 75
    new_stones = {new_stone:1 for stone in stones for new_stone in apply_rule(stone)}
    for blink in range(blinks - 1):
        stones = new_stones
        new_stones = {}
        for stone in stones:
            stone_count = stones[stone]
            for new_stone in apply_rule(stone):
                if new_stone in new_stones:
                    new_stones[new_stone] += stone_count
                else:
                    new_stones[new_stone] = stone_count

    print(sum(count for count in new_stones.values()))

        
@lru_cache(maxsize=None)
def apply_rule(stone):
    if stone == 0:
        return (1, )
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        half_idx = len(stone) // 2
        return (int(stone[:half_idx]), int(stone[half_idx:]))
    else:
        return (stone * 2024, )
            
        
    
if __name__ == '__main__':
    main()
