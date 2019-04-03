#%% https://stackoverflow.com/a/2831242/4510954

#%% https://stackoverflow.com/q/55488946/4510954
def generate_id():
    random_id= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    return random_id

existing_ids = ['AAAAA', 'BBBBB', 'CCCCC']
for id in existing_ids:
    if not generate_id() == id:
        unique_id = generate_id()

#%% proces above - https://stackoverflow.com/a/55489022/4510954
while True:
    a = generate_id()
    if a not in set(existing_ids) : 
        break
