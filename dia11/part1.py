import time

def main():
    t = time.time()
    with open('test.txt') as f:
        stones = [int(stone) for stone in f.read().split()]

    blinks = 25

    for blink in range(blinks):
        stones_post_blink = []       
        for stone in stones:
            if stone == 0:
                stones_post_blink.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                stones_post_blink.extend([int(stone[:len(stone)//2]), int(stone[len(stone)//2:])])
            else:
                stones_post_blink.append(stone * 2024)
        stones = stones_post_blink
            
    print(len(stones))

if __name__ == '__main__':
    main()
