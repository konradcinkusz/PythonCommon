alphabet = ['F','Z','G','L']
cases = ['ZG','LG', 'LGZ']
watersides = [('F','Z','G','L'),('','','','')]
def main() :
    startState = State()
    startState.watersides = [('F','Z','G','L'),('','','','')]
    startState.is_used = True
    while True:
       #get last state
       last_state = State.all_state_array[-1]
       pass

class State :
    all_state_array = []
    def __init__(self, *args, **kwargs):
        self.is_used = False
        self.back_way = []
        import uuid
        self.guid = uuid.uuid4()
        State.all_state_array.append(self)

def state_mem_test() :
    s1 = State()
    s2 = State()
    print(s1.all_state_array)
    print(State.all_state_array)
    print(State.all_state_array is s1.all_state_array)

if __name__ == "__main__":
    main()
