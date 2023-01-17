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

def get_action():
    print('You can:')
    print('     (F)ill in the bucket')
    print('     (E)mpty the bucket.')
    print('     (P)our one bucket into another.')
    print('     (Q)uit.')
    while True:
        response = input('> ').upper().strip()

        if response == 'QUIT' or response == 'Q':
            exit('Thanks for playing!')
        
        elif response in ('F', 'E', 'P'):
            return response
        
        print('Enter one of "F", "E", or "P"')
    
def main():
    print('Water Bucket Puzzle')
    print()
    goal = 4
    steps = 0
    bucket_sizes = ['8', '5', '3']
    buckets = WaterBuckets(bucket_sizes, goal)
    while True:
        print('Try to get {}L of water into one of these buckets:'.format(
            goal
        ))
        buckets.display_buckets()

        action = get_action()
        bucket_to_perform_action = get_bucket()
        if action == 'F':
            buckets.fill_bucket(bucket_to_perform_action)
            steps += 1
        elif action == 'E':
            buckets.empty_bucket(bucket_to_perform_action)
            steps += 1
        elif action == 'P':
            dest_bucket = get_bucket()
            buckets.pour_from_bucket(bucket_to_perform_action, dest_bucket)
            steps += 1
            

if __name__ == '__main__':
    main()