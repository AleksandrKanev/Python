from datetime import datetime

def logger(data, values, user, file_path='home_work_10/log.csv',):
    time = datetime.now()
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'{time}; {user}; {values}={data};\n')