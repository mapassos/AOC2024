
def main():

    with open('input.txt') as f:
        disk_map_compact = [int(block) for block in ''.join(f.read().splitlines())]

    block_id = 0
    disk_map = []
    num_blocks = 0

    
    for i, block_size in enumerate(disk_map_compact):
        if i % 2 == 0:
            file_chunk = [str(block_id)] * block_size
            num_blocks += len(file_chunk) 
            disk_map.extend(file_chunk)
            block_id += 1
        else:
            disk_map.extend(['.'] * block_size)

    disk_size = len(disk_map)

    empty_block_idx = 0
    block_idx = 0
    while '.' in disk_map[:num_blocks]:
        if disk_map[empty_block_idx] == '.':
            for block_idx in range(block_idx, disk_size):
                if disk_map[-(block_idx + 1)].isdigit():
                    disk_map[empty_block_idx], disk_map[-(block_idx + 1)] = disk_map[-(block_idx + 1)], disk_map[empty_block_idx]
                    break
        empty_block_idx += 1

    print(sum(int(block) * i for i, block in enumerate(disk_map[:num_blocks])))
        

if __name__ == '__main__':
    main()
