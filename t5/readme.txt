python t5.py write
python t5.py read_all
python t5.py read_where "city_id=962"
python t5.py execute 'UPDATE cities SET city="Shoto" WHERE city_id=962'
python t5.py read_where "city_id=962"