def main():

    with open('input.txt') as f:
        disk_map_compact = [int(block) for block in ''.join(f.read().splitlines())]

    block_id = 0
    disk_map = []
    num_blocks = 0

    disk_map_idx = 0
    empty_blocks_distribution = {}
    
    for i, block_size in enumerate(disk_map_compact):
        if i % 2 == 0:
            file_chunk = [str(block_id)] * block_size
            num_blocks += block_size 
            disk_map.extend(file_chunk)
            block_id += 1
            
            disk_map_idx += block_size
        else:
            empty_blocks_distribution[(disk_map_idx, disk_map_idx - 1 + block_size)] = block_size
            disk_map.extend(['.'] * block_size)
            disk_map_idx += block_size

    disk_size = len(disk_map)

    block_idx = 1
    while block_idx < disk_size and '.' in disk_map[:-block_idx]:

        if disk_map[-block_idx] != '.':
            block_start_idx = block_idx 
            while disk_map[-block_idx] == disk_map[-block_start_idx]:
                block_idx += 1

            block_size = block_idx - block_start_idx

            for empty_block_idx in range(0, disk_size - block_idx):
                if disk_map[empty_block_idx] == '.':
                    empty_block_start_idx = empty_block_idx
                    
                    while disk_map[empty_block_idx] == '.':
                        empty_block_idx += 1
                        
                    empty_size = empty_block_idx - empty_block_start_idx
                    
                    if block_size <= empty_size:
                        disk_map[empty_block_start_idx:empty_block_start_idx + block_size] = disk_map[-block_idx + 1 : disk_size - block_start_idx + 1]
                        disk_map[-block_idx + 1 : disk_size - block_start_idx + 1] = ['.'] * block_size 
                        break

        else:
            block_idx += 1

    print(sum(int(block) * i for i, block in enumerate(disk_map) if block != '.'))
    

if __name__ == '__main__':
    main()
