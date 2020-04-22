from main.models import db, User, Date, Record
import time

def get_user_data(user_id):
    records = User.query.filter_by(id=user_id).first().records
    return records

def get_day_members(date_id):
    records = Record.query.filter_by(date_id=date_id).all()
    print(records)
    return records

if __name__ == '__main__':
    start = time.time()
    #print(get_user_data(1))
    members = get_day_members(470)
    elapsed_time = time.time() - start
    print(elapsed_time)
    for member in members:
        print(member.user.name)
