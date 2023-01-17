from sys import exit

class WaterBuckets:
    def __init__(s, sizes, goal):
        assert len(sizes) == 3, 'Expected list of sizes of 3 buckets'
        s.water_buckets = {}
        for size in sizes:
            s.water_buckets[str(size)] = size
        s.goal = goal
    
    def display_buckets(s):
        pass

    def empty_bucket(s, bucket_size_label):
        pass
    
    def fill_bucket(s, bucket_size_label):
        pass
    
    def pour_from_bucket(s, src_bucket_size_label, dst_bucket_size_label):
        pass

    def reached_goal(s):
        pass

def get_bucket(bucket_sizes):
    assert len(bucket_sizes) == 3, 'Expected list of sizes of 3 buckets'
    print('Select a bucket {} or QUIT'.format(', '.join(bucket_sizes)))
    while True:
        response = input('> ').upper().strip()
        if response == 'QUIT':
            exit('Thanks for playing!')
        elif response in bucket_sizes:
            return response
        print('Please enter one of "{}" or QUIT'.format('", "'.join(bucket_sizes)))

if __name__ == '__main__':
    main()