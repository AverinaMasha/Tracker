from flask_back.DB.habits import Habits
from flask_back.DB.persons import Persons
from datetime import timedelta

#from habits import Habits
#from persons import Persons
from bson.objectid import ObjectId

def get_person_id(login='test', password='test'):
    '''
    Возвращает id полдьзователя по login, password.

    '''
    db_persons = Persons()
    
    person = db_persons.get_one({'login': login, 'password': password})
    _id = person['_id']

    return _id

def get_person_data(_id):
    '''
    Возвращает все привычки пользователя.
    
    '''
    db_habits = Habits()
    habits = []
    for habit in db_habits.get({'id_user': ObjectId(_id)}):    
        habits.append(habit)
    
    return habits
    
def add_person(login, password):
    '''
    Добовляет новую персону.
    
    '''
    if check_person(login):
        db_persons = Persons()
        db_persons.add({'login': str(login), 'password': str(password)})
        return True
    else:
        return False

def check_person(login):
    '''
    Проверяет наличие пользователя с такпим именем.
    
    '''
    db_persons = Persons()
    person = db_persons.get({'login': login})
    
    if person.count() == 1:
        return False
    else:
        return True
    
def add_person_habit(_id, name, start, end):
    '''
    Добавляет новую привычку пользователю.
    
    '''
    db_habits = Habits()
    db_habits.add(name, _id, start, end)
    
    return True

def add_check_for_person_habit(_id_habit, start, end):
    '''
    Добавляет информаци о выполнение привычки.
    
    '''
    db_habits = Habits()

    return db_habits.add_check( _id_habit, start, end)

def del_check_for_person_habit(_id_habit, data_del):
    '''
    Удаляет информаци о выполнение привычки.
    
    '''
    db_habits = Habits()

    return db_habits.delete_check(_id_habit, data_del)

def get_consecutive_days(_id_habit):
    '''
    Возвращает кол-во последних подряд идущих дней выполнения.

    '''
    db_habits = Habits()
    checks = db_habits.get_one(_id_habit)
    count_day = 0
    last_day = 0
    
    for check in checks['check']:
        day_now = check.day
        if last_day == 0:
            last_day = day_now
            count_day += 1
        elif last_day == (check - timedelta(days=1)).day:
            count_day += 1
        else:
            count_day = 0
            last_day = 0
    return count_day

#add_person_habit("5ee2258f2f9c980b83d39e07", "НЕ ГРЫЗТЬ МЕБЕЛЬ2!", "06-06-2019", "06-06-2021")
#add_check_for_person_habit("5ee2258f2f9c980b83d39e07", "НЕ ГРЫЗТЬ МЕБЕЛЬ2!", "06-06-2019", "06-06-2021")
#print(get_person_data("5ee2258f2f9c980b83d39e07"))
#del_check_for_person_habit("5ee2258f2f9c980b83d39e07", "НЕ ГРЫЗТЬ МЕБЕЛЬ2!", "06-06-2019", "06-06-2021", "21-06-2020")
#print(get_person_data("5ee2258f2f9c980b83d39e07"))