from sys import exit

class WaterBuckets:
    def __init__(s, sizes, goal):
        assert len(sizes) == 3, 'Expected list of sizes of 3 buckets'
        s.water_buckets = {}
        sizes.sort(reverse=True)
        s.sizes = sizes
        for size in s.sizes:
            s.water_buckets[str(size)] = 0

        s.goal = goal
        
        s.display_string = ''

        s.high, s.mid, s.low = map(int, s.sizes)
        multiplier = 3
        for i in range(s.high):
            s.display_string = (str(i+1) + '|{}|  ') * multiplier + '\n' \
                                + s.display_string
            if s.low - 1 == i:
                multiplier -= 1
            if s.mid - 1== i:
                multiplier -= 1    
        
        s.display_string += ' +------+   +------+   +------+'
    
    def display_buckets(s):
        high_display = []
        for i in range(1, s.high + 1):
            if s.water_buckets[str(s.high)] < i:
                high_display.append('      ')
            else:
                high_display.append('wwwwww')
        
        mid_display = []
        for i in range(1, s.mid + 1):
            if s.water_buckets[str(s.mid)] < i:
                mid_display.append('      ')
            else:
                mid_display.append('wwwwww')
        
        low_display = []
        for i in range(1, s.low + 1):
            if s.water_buckets[str(s.low)] < i:
                low_display.append('      ')
            else:
                low_display.append('wwwwww')

        water_display = []
        water_display.extend(high_display[s.mid:])

        print(low_display)
        for i in range(s.mid - 1, s.low - 1, - 1):
            water_display.append(high_display[i])
            water_display.append(mid_display[i])
        
        for i in range(s.low - 1, -1 , - 1):
            water_display.append(high_display[i])
            water_display.append(mid_display[i])
            water_display.append(low_display[i])        

        print()
        print(s.display_string.format(*water_display))
        print()

    def empty_bucket(s, bucket_size_label):
        s.water_buckets[str(bucket_size_label)] = 0
    
    def fill_bucket(s, bucket_size_label):
        s.water_buckets[str(bucket_size_label)] = int(bucket_size_label)
    
    def pour_from_bucket(s, src_bucket_size_label, dst_bucket_size_label):
        space_in_dest = int(dst_bucket_size_label) -\
             s.water_buckets[str(dst_bucket_size_label)]
        amount_to_pour = \
            min(space_in_dest, s.water_buckets[str(src_bucket_size_label)])
        s.water_buckets[str(src_bucket_size_label)] -= amount_to_pour
        s.water_buckets[str(dst_bucket_size_label)] += amount_to_pour

    def reached_goal(s):
        for key in s.water_buckets.keys():
            if s.water_buckets[key] == s.goal:
                return True
        return False

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
        if buckets.reached_goal():
            buckets.display_buckets()
            exit('Good job! You solved it in {} steps'.format(steps))
        print('Try to get {}L of water into one of these buckets:'.format(
            goal
        ))
        buckets.display_buckets()

        action = get_action()
        bucket_to_perform_action = get_bucket(bucket_sizes)
        if action == 'F':
            buckets.fill_bucket(bucket_to_perform_action)
            steps += 1
        elif action == 'E':
            buckets.empty_bucket(bucket_to_perform_action)
            steps += 1
        elif action == 'P':
            dest_bucket = get_bucket(bucket_sizes)
            buckets.pour_from_bucket(bucket_to_perform_action, dest_bucket)
            steps += 1


if __name__ == '__main__':
    main()